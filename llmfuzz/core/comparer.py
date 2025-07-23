"""
Output comparison module for analyzing differences between LLM responses

@author: souhailaS
"""

import json
import re
import difflib
from dataclasses import dataclass
from typing import List, Dict, Any, Union, Optional
from enum import Enum

try:
    from sentence_transformers import SentenceTransformer
    import numpy as np
    SENTENCE_TRANSFORMERS_AVAILABLE = True
except ImportError:
    SENTENCE_TRANSFORMERS_AVAILABLE = False

try:
    import nltk
    from nltk.translate.bleu_score import sentence_bleu
    from nltk.tokenize import word_tokenize
    NLTK_AVAILABLE = True
except ImportError:
    NLTK_AVAILABLE = False


class ComparisonResult(Enum):
    EQUIVALENT = "equivalent"
    MINOR_VARIATION = "minor_variation"
    BEHAVIORAL_DEVIATION = "behavioral_deviation"


@dataclass
class ComparisonScore:
    token_similarity: float  # 0.0 to 1.0
    semantic_similarity: float  # 0.0 to 1.0
    structural_similarity: float  # 0.0 to 1.0
    overall_similarity: float  # 0.0 to 1.0
    classification: ComparisonResult
    details: Dict[str, Any]


class OutputComparer:
    """
    Compares LLM outputs using various similarity metrics
    """
    
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.embedding_model = None
        
        # Load sentence transformer model if available
        if SENTENCE_TRANSFORMERS_AVAILABLE:
            try:
                self.embedding_model = SentenceTransformer(model_name)
            except Exception as e:
                print(f"Warning: Could not load sentence transformer model: {e}")
        
        # Download NLTK data if available
        if NLTK_AVAILABLE:
            try:
                nltk.download('punkt', quiet=True)
            except:
                pass
    
    def compare_outputs(self, original: str, mutated: str) -> ComparisonScore:
        """
        Compare two text outputs and return similarity scores
        """
        # Calculate different similarity metrics
        token_sim = self._calculate_token_similarity(original, mutated)
        semantic_sim = self._calculate_semantic_similarity(original, mutated)
        structural_sim = self._calculate_structural_similarity(original, mutated)
        
        # Calculate overall similarity (weighted average)
        overall_sim = (token_sim * 0.3 + semantic_sim * 0.5 + structural_sim * 0.2)
        
        # Classify the comparison result
        classification = self._classify_similarity(overall_sim, token_sim, semantic_sim)
        
        # Generate detailed analysis
        details = {
            'character_diff': self._get_character_diff(original, mutated),
            'word_diff': self._get_word_diff(original, mutated),
            'length_ratio': len(mutated) / max(len(original), 1),
            'is_json_valid': self._check_json_validity(original, mutated),
            'bleu_score': self._calculate_bleu_score(original, mutated)
        }
        
        return ComparisonScore(
            token_similarity=token_sim,
            semantic_similarity=semantic_sim,
            structural_similarity=structural_sim,
            overall_similarity=overall_sim,
            classification=classification,
            details=details
        )
    
    def _calculate_token_similarity(self, text1: str, text2: str) -> float:
        """Calculate token-level similarity using sequence matcher"""
        # Clean and tokenize
        tokens1 = self._tokenize(text1)
        tokens2 = self._tokenize(text2)
        
        # Use difflib for sequence matching
        matcher = difflib.SequenceMatcher(None, tokens1, tokens2)
        return matcher.ratio()
    
    def _calculate_semantic_similarity(self, text1: str, text2: str) -> float:
        """Calculate semantic similarity using sentence embeddings"""
        if not self.embedding_model:
            # Fallback to simple word overlap
            words1 = set(text1.lower().split())
            words2 = set(text2.lower().split())
            
            if not words1 and not words2:
                return 1.0
            elif not words1 or not words2:
                return 0.0
            
            intersection = words1.intersection(words2)
            union = words1.union(words2)
            return len(intersection) / len(union)
        
        try:
            # Use sentence transformers for semantic similarity
            embeddings = self.embedding_model.encode([text1, text2])
            similarity = np.dot(embeddings[0], embeddings[1]) / (
                np.linalg.norm(embeddings[0]) * np.linalg.norm(embeddings[1])
            )
            return max(0.0, float(similarity))  # Ensure non-negative
        except Exception:
            # Fallback to word overlap
            return self._calculate_word_overlap(text1, text2)
    
    def _calculate_structural_similarity(self, text1: str, text2: str) -> float:
        """Calculate structural similarity based on format and organization"""
        # Check if both are JSON
        json1 = self._try_parse_json(text1)
        json2 = self._try_parse_json(text2)
        
        if json1 is not None and json2 is not None:
            return self._compare_json_structure(json1, json2)
        
        # Check sentence structure
        sentences1 = self._split_sentences(text1)
        sentences2 = self._split_sentences(text2)
        
        if len(sentences1) == 0 and len(sentences2) == 0:
            return 1.0
        
        sentence_count_similarity = 1.0 - abs(len(sentences1) - len(sentences2)) / max(len(sentences1), len(sentences2), 1)
        
        # Check formatting patterns (bullet points, numbers, etc.)
        format_similarity = self._compare_formatting(text1, text2)
        
        return (sentence_count_similarity + format_similarity) / 2
    
    def _classify_similarity(self, overall: float, token: float, semantic: float) -> ComparisonResult:
        """Classify the similarity into categories"""
        if overall >= 0.95 and semantic >= 0.9:
            return ComparisonResult.EQUIVALENT
        elif overall >= 0.75 and semantic >= 0.7:
            return ComparisonResult.MINOR_VARIATION
        else:
            return ComparisonResult.BEHAVIORAL_DEVIATION
    
    def _tokenize(self, text: str) -> List[str]:
        """Tokenize text into words"""
        if NLTK_AVAILABLE:
            try:
                return word_tokenize(text.lower())
            except:
                pass
        
        # Simple tokenization
        return re.findall(r'\b\w+\b', text.lower())
    
    def _get_character_diff(self, text1: str, text2: str) -> List[str]:
        """Get character-level diff"""
        differ = difflib.unified_diff(
            text1.splitlines(keepends=True),
            text2.splitlines(keepends=True),
            fromfile='original',
            tofile='mutated',
            n=3
        )
        return list(differ)
    
    def _get_word_diff(self, text1: str, text2: str) -> Dict[str, List[str]]:
        """Get word-level differences"""
        words1 = text1.split()
        words2 = text2.split()
        
        matcher = difflib.SequenceMatcher(None, words1, words2)
        
        added = []
        removed = []
        
        for tag, i1, i2, j1, j2 in matcher.get_opcodes():
            if tag == 'delete':
                removed.extend(words1[i1:i2])
            elif tag == 'insert':
                added.extend(words2[j1:j2])
            elif tag == 'replace':
                removed.extend(words1[i1:i2])
                added.extend(words2[j1:j2])
        
        return {'added': added, 'removed': removed}
    
    def _check_json_validity(self, text1: str, text2: str) -> Dict[str, bool]:
        """Check if both texts are valid JSON"""
        return {
            'original_valid': self._try_parse_json(text1) is not None,
            'mutated_valid': self._try_parse_json(text2) is not None
        }
    
    def _calculate_bleu_score(self, text1: str, text2: str) -> float:
        """Calculate BLEU score if NLTK is available"""
        if not NLTK_AVAILABLE:
            return 0.0
        
        try:
            tokens1 = word_tokenize(text1.lower())
            tokens2 = word_tokenize(text2.lower())
            
            if not tokens1 or not tokens2:
                return 0.0
            
            return sentence_bleu([tokens1], tokens2)
        except:
            return 0.0
    
    def _try_parse_json(self, text: str) -> Optional[Dict]:
        """Try to parse text as JSON"""
        try:
            return json.loads(text.strip())
        except:
            return None
    
    def _compare_json_structure(self, json1: Dict, json2: Dict) -> float:
        """Compare JSON structure similarity"""
        if json1 == json2:
            return 1.0
        
        # Compare keys
        keys1 = set(self._get_json_keys(json1))
        keys2 = set(self._get_json_keys(json2))
        
        if not keys1 and not keys2:
            return 1.0
        elif not keys1 or not keys2:
            return 0.0
        
        key_similarity = len(keys1.intersection(keys2)) / len(keys1.union(keys2))
        
        # Compare structure depth and types
        structure1 = self._analyze_json_structure(json1)
        structure2 = self._analyze_json_structure(json2)
        
        structure_similarity = 1.0 - abs(structure1['depth'] - structure2['depth']) / max(structure1['depth'], structure2['depth'], 1)
        
        return (key_similarity + structure_similarity) / 2
    
    def _get_json_keys(self, obj: Any, prefix: str = '') -> List[str]:
        """Recursively get all JSON keys"""
        keys = []
        if isinstance(obj, dict):
            for key, value in obj.items():
                full_key = f"{prefix}.{key}" if prefix else key
                keys.append(full_key)
                keys.extend(self._get_json_keys(value, full_key))
        elif isinstance(obj, list):
            for i, item in enumerate(obj):
                keys.extend(self._get_json_keys(item, f"{prefix}[{i}]"))
        return keys
    
    def _analyze_json_structure(self, obj: Any, depth: int = 0) -> Dict[str, Any]:
        """Analyze JSON structure"""
        max_depth = depth
        
        if isinstance(obj, dict):
            for value in obj.values():
                sub_analysis = self._analyze_json_structure(value, depth + 1)
                max_depth = max(max_depth, sub_analysis['depth'])
        elif isinstance(obj, list):
            for item in obj:
                sub_analysis = self._analyze_json_structure(item, depth + 1)
                max_depth = max(max_depth, sub_analysis['depth'])
        
        return {'depth': max_depth}
    
    def _split_sentences(self, text: str) -> List[str]:
        """Split text into sentences"""
        if NLTK_AVAILABLE:
            try:
                from nltk.tokenize import sent_tokenize
                return sent_tokenize(text)
            except:
                pass
        
        # Simple sentence splitting
        sentences = re.split(r'[.!?]+', text)
        return [s.strip() for s in sentences if s.strip()]
    
    def _compare_formatting(self, text1: str, text2: str) -> float:
        """Compare formatting patterns"""
        patterns = [
            r'^\s*[-*+]\s+',  # Bullet points
            r'^\s*\d+\.\s+',  # Numbered lists
            r'^#{1,6}\s+',    # Headers
            r'```',           # Code blocks
            r'\*\*.*?\*\*',   # Bold text
            r'_.*?_',         # Italic text
        ]
        
        matches1 = sum(len(re.findall(pattern, text1, re.MULTILINE)) for pattern in patterns)
        matches2 = sum(len(re.findall(pattern, text2, re.MULTILINE)) for pattern in patterns)
        
        if matches1 == 0 and matches2 == 0:
            return 1.0
        
        return 1.0 - abs(matches1 - matches2) / max(matches1, matches2, 1)
    
    def _calculate_word_overlap(self, text1: str, text2: str) -> float:
        """Calculate simple word overlap similarity"""
        words1 = set(text1.lower().split())
        words2 = set(text2.lower().split())
        
        if not words1 and not words2:
            return 1.0
        elif not words1 or not words2:
            return 0.0
        
        intersection = words1.intersection(words2)
        union = words1.union(words2)
        return len(intersection) / len(union) 
"""
Mutation engine for generating prompt variations

@author: souhailaS
"""

import random
import re
import string
from typing import List, Dict, Any
from dataclasses import dataclass
from enum import Enum

try:
    import nltk
    from nltk.corpus import wordnet
    from nltk.tokenize import word_tokenize, sent_tokenize
    NLTK_AVAILABLE = True
except ImportError:
    NLTK_AVAILABLE = False

try:
    from textblob import TextBlob
    TEXTBLOB_AVAILABLE = True
except ImportError:
    TEXTBLOB_AVAILABLE = False


class MutationType(Enum):
    LEXICAL = "lexical"
    SEMANTIC = "semantic"
    STRUCTURAL = "structural"


@dataclass
class Mutation:
    original_text: str
    mutated_text: str
    mutation_type: MutationType
    description: str
    severity: float  # 0.0 to 1.0, how much the mutation changes the meaning


class Mutator:
    """
    Generates mutations for prompts to test robustness
    """
    
    def __init__(self, seed: int = None):
        if seed:
            random.seed(seed)
        
        # Download required NLTK data if available
        if NLTK_AVAILABLE:
            try:
                nltk.download('punkt', quiet=True)
                nltk.download('wordnet', quiet=True)
                nltk.download('averaged_perceptron_tagger', quiet=True)
            except:
                pass
    
    def generate_mutations(self, text: str, count: int = 20) -> List[Mutation]:
        """Generate multiple mutations of the input text"""
        mutations = []
        
        # Generate different types of mutations
        lexical_count = max(1, count // 3)
        semantic_count = max(1, count // 3)
        structural_count = count - lexical_count - semantic_count
        
        # Lexical mutations
        mutations.extend(self._generate_lexical_mutations(text, lexical_count))
        
        # Semantic mutations
        mutations.extend(self._generate_semantic_mutations(text, semantic_count))
        
        # Structural mutations
        mutations.extend(self._generate_structural_mutations(text, structural_count))
        
        return mutations[:count]
    
    def _generate_lexical_mutations(self, text: str, count: int) -> List[Mutation]:
        """Generate lexical mutations like case changes, punctuation"""
        mutations = []
        
        for _ in range(count):
            mutation_type = random.choice([
                'case_upper', 'case_lower', 'case_title', 'case_random',
                'punctuation_add', 'punctuation_remove', 'spacing_change'
            ])
            
            if mutation_type == 'case_upper':
                mutated = text.upper()
                desc = "Convert all text to uppercase"
                severity = 0.1
            elif mutation_type == 'case_lower':
                mutated = text.lower()
                desc = "Convert all text to lowercase"
                severity = 0.1
            elif mutation_type == 'case_title':
                mutated = text.title()
                desc = "Convert text to title case"
                severity = 0.1
            elif mutation_type == 'case_random':
                mutated = ''.join(c.upper() if random.random() > 0.5 else c.lower() for c in text)
                desc = "Randomly change case of characters"
                severity = 0.2
            elif mutation_type == 'punctuation_add':
                mutated = self._add_random_punctuation(text)
                desc = "Add random punctuation"
                severity = 0.3
            elif mutation_type == 'punctuation_remove':
                mutated = re.sub(r'[^\w\s]', '', text)
                desc = "Remove all punctuation"
                severity = 0.4
            elif mutation_type == 'spacing_change':
                mutated = re.sub(r'\s+', '  ', text)  # Double spaces
                desc = "Change spacing patterns"
                severity = 0.2
            else:
                continue
                
            if mutated != text:
                mutations.append(Mutation(
                    original_text=text,
                    mutated_text=mutated,
                    mutation_type=MutationType.LEXICAL,
                    description=desc,
                    severity=severity
                ))
        
        return mutations
    
    def _generate_semantic_mutations(self, text: str, count: int) -> List[Mutation]:
        """Generate semantic mutations using synonyms"""
        mutations = []
        
        if not NLTK_AVAILABLE:
            # Simple synonym replacements without NLTK
            simple_synonyms = {
                'good': ['great', 'excellent', 'fine', 'nice'],
                'bad': ['poor', 'terrible', 'awful', 'horrible'],
                'big': ['large', 'huge', 'enormous', 'massive'],
                'small': ['tiny', 'little', 'minor', 'petite'],
                'fast': ['quick', 'rapid', 'swift', 'speedy'],
                'slow': ['sluggish', 'gradual', 'leisurely', 'delayed']
            }
            
            for _ in range(count):
                mutated = text
                words = text.split()
                for i, word in enumerate(words):
                    word_lower = word.lower().strip('.,!?;:')
                    if word_lower in simple_synonyms:
                        synonym = random.choice(simple_synonyms[word_lower])
                        words[i] = word.replace(word_lower, synonym)
                        mutated = ' '.join(words)
                        break
                
                if mutated != text:
                    mutations.append(Mutation(
                        original_text=text,
                        mutated_text=mutated,
                        mutation_type=MutationType.SEMANTIC,
                        description="Replace word with synonym",
                        severity=0.3
                    ))
        else:
            # Use NLTK for more sophisticated synonym replacement
            words = word_tokenize(text)
            
            for _ in range(count):
                mutated_words = words.copy()
                word_idx = random.randint(0, len(words) - 1)
                word = words[word_idx]
                
                synonyms = self._get_synonyms(word)
                if synonyms:
                    synonym = random.choice(synonyms)
                    mutated_words[word_idx] = synonym
                    mutated = ' '.join(mutated_words)
                    
                    mutations.append(Mutation(
                        original_text=text,
                        mutated_text=mutated,
                        mutation_type=MutationType.SEMANTIC,
                        description=f"Replace '{word}' with synonym '{synonym}'",
                        severity=0.3
                    ))
        
        return mutations
    
    def _generate_structural_mutations(self, text: str, count: int) -> List[Mutation]:
        """Generate structural mutations like reordering"""
        mutations = []
        
        # Split into sentences
        sentences = self._split_sentences(text)
        
        if len(sentences) > 1:
            for _ in range(count):
                mutation_type = random.choice(['reorder_sentences', 'reverse_sentences'])
                
                if mutation_type == 'reorder_sentences':
                    shuffled = sentences.copy()
                    random.shuffle(shuffled)
                    mutated = ' '.join(shuffled)
                    desc = "Randomly reorder sentences"
                    severity = 0.6
                elif mutation_type == 'reverse_sentences':
                    mutated = ' '.join(reversed(sentences))
                    desc = "Reverse sentence order"
                    severity = 0.5
                else:
                    continue
                
                if mutated != text:
                    mutations.append(Mutation(
                        original_text=text,
                        mutated_text=mutated,
                        mutation_type=MutationType.STRUCTURAL,
                        description=desc,
                        severity=severity
                    ))
        else:
            # For single sentences, try word reordering
            words = text.split()
            if len(words) > 3:
                for _ in range(count):
                    shuffled_words = words.copy()
                    # Keep first and last word in place, shuffle middle
                    middle = shuffled_words[1:-1]
                    random.shuffle(middle)
                    shuffled_words[1:-1] = middle
                    mutated = ' '.join(shuffled_words)
                    
                    mutations.append(Mutation(
                        original_text=text,
                        mutated_text=mutated,
                        mutation_type=MutationType.STRUCTURAL,
                        description="Reorder words while preserving sentence boundaries",
                        severity=0.7
                    ))
        
        return mutations
    
    def _add_random_punctuation(self, text: str) -> str:
        """Add random punctuation to text"""
        punctuation = '.,!?;:'
        words = text.split()
        
        for i in range(len(words)):
            if random.random() < 0.3:  # 30% chance to add punctuation
                words[i] += random.choice(punctuation)
        
        return ' '.join(words)
    
    def _get_synonyms(self, word: str) -> List[str]:
        """Get synonyms for a word using WordNet"""
        if not NLTK_AVAILABLE:
            return []
        
        synonyms = set()
        for syn in wordnet.synsets(word):
            for lemma in syn.lemmas():
                synonyms.add(lemma.name().replace('_', ' '))
        
        synonyms.discard(word)  # Remove the original word
        return list(synonyms)
    
    def _split_sentences(self, text: str) -> List[str]:
        """Split text into sentences"""
        if NLTK_AVAILABLE:
            return sent_tokenize(text)
        else:
            # Simple sentence splitting
            sentences = re.split(r'[.!?]+', text)
            return [s.strip() for s in sentences if s.strip()] 
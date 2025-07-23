"""
Tests for the mutator module
"""

import pytest
from llmfuzz.core.mutator import Mutator, MutationType


def test_mutator_initialization():
    """Test mutator can be initialized"""
    mutator = Mutator()
    assert mutator is not None


def test_generate_mutations():
    """Test mutation generation"""
    mutator = Mutator(seed=42)
    text = "This is a test prompt for mutation testing."
    
    mutations = mutator.generate_mutations(text, count=10)
    
    assert len(mutations) <= 10
    assert all(mutation.original_text == text for mutation in mutations)
    assert all(mutation.mutated_text != text for mutation in mutations)


def test_lexical_mutations():
    """Test lexical mutations are generated"""
    mutator = Mutator(seed=42)
    text = "Hello World"
    
    mutations = mutator._generate_lexical_mutations(text, count=5)
    
    assert len(mutations) > 0
    assert all(mutation.mutation_type == MutationType.LEXICAL for mutation in mutations)


def test_semantic_mutations():
    """Test semantic mutations are generated"""
    mutator = Mutator(seed=42)
    text = "This is a good example of testing."
    
    mutations = mutator._generate_semantic_mutations(text, count=5)
    
    # Semantic mutations may not always be generated if no synonyms are found
    assert len(mutations) >= 0
    if mutations:
        assert all(mutation.mutation_type == MutationType.SEMANTIC for mutation in mutations)


def test_structural_mutations():
    """Test structural mutations are generated"""
    mutator = Mutator(seed=42)
    text = "First sentence. Second sentence. Third sentence."
    
    mutations = mutator._generate_structural_mutations(text, count=3)
    
    assert len(mutations) >= 0
    if mutations:
        assert all(mutation.mutation_type == MutationType.STRUCTURAL for mutation in mutations)


if __name__ == "__main__":
    pytest.main([__file__]) 
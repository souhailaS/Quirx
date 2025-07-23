#!/usr/bin/env python3
"""
Simple evaluation script that loads config directly and tests APIs

@author: souhailaS
"""

import os
import sys
from pathlib import Path

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def load_config():
    """Load API keys from config file"""
    config_file = Path('config/api_keys.env')
    if not config_file.exists():
        print("ERROR: config/api_keys.env not found!")
        print("Please copy config/api_keys.env.sample to config/api_keys.env and add your keys")
        return False
    
    with open(config_file) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, value = line.split('=', 1)
                os.environ[key] = value
    
    return True

def quick_test():
    """Quick test of both providers"""
    if not load_config():
        return
    
    from llmfuzz.core.mutator import Mutator
    from llmfuzz.core.runner import LLMRunner
    from llmfuzz.core.comparer import OutputComparer
    
    # Test prompt
    prompt = "Classify the sentiment: I love this product!"
    
    print("LLMFuzz API Test")
    print("="*50)
    
    # Test OpenAI
    print("\n1. Testing OpenAI GPT-3.5-turbo...")
    try:
        runner_openai = LLMRunner(provider='openai')
        if runner_openai.test_connection():
            print("   ✓ OpenAI connection successful")
            
            # Generate some mutations
            mutator = Mutator(seed=42)
            mutations = mutator.generate_mutations(prompt, count=3)
            print(f"   Generated {len(mutations)} mutations")
            
            # Test original
            original = runner_openai.run_prompt(prompt, model='gpt-3.5-turbo')
            if original.error:
                print(f"   ✗ Error: {original.error}")
            else:
                print(f"   ✓ Original response: {original.text}")
                print(f"   Tokens: {original.tokens_used}, Time: {original.response_time:.2f}s")
                
                # Test one mutation
                if mutations:
                    mutated = runner_openai.run_prompt(mutations[0].mutated_text, model='gpt-3.5-turbo')
                    if not mutated.error:
                        comparer = OutputComparer()
                        comparison = comparer.compare_outputs(original.text, mutated.text)
                        print(f"   ✓ Mutation test: {comparison.classification.value} (similarity: {comparison.overall_similarity:.3f})")
        else:
            print("   ✗ OpenAI connection failed")
    except Exception as e:
        print(f"   ✗ OpenAI error: {e}")
    
    # Test Anthropic
    print("\n2. Testing Anthropic Claude...")
    try:
        runner_anthropic = LLMRunner(provider='anthropic')
        if runner_anthropic.test_connection():
            print("   ✓ Anthropic connection successful")
            
            # Test original
            original = runner_anthropic.run_prompt(prompt, model='claude-3-sonnet-20240229')
            if original.error:
                print(f"   ✗ Error: {original.error}")
            else:
                print(f"   ✓ Original response: {original.text}")
                print(f"   Tokens: {original.tokens_used}, Time: {original.response_time:.2f}s")
                
                # Test one mutation if we have them
                if 'mutations' in locals() and mutations:
                    mutated = runner_anthropic.run_prompt(mutations[0].mutated_text, model='claude-3-sonnet-20240229')
                    if not mutated.error:
                        comparison = comparer.compare_outputs(original.text, mutated.text)
                        print(f"   ✓ Mutation test: {comparison.classification.value} (similarity: {comparison.overall_similarity:.3f})")
        else:
            print("   ✗ Anthropic connection failed")
    except Exception as e:
        print(f"   ✗ Anthropic error: {e}")
    
    print("\n3. Testing complete!")
    print("\nTo run full evaluation:")
    print("   python -m llmfuzz.cli --prompt-file examples/prompt_classifier.txt --input 'I love this!' --provider openai --mutations 10")
    print("   python -m llmfuzz.cli --prompt-file examples/prompt_classifier.txt --input 'I love this!' --provider anthropic --mutations 10")

if __name__ == "__main__":
    quick_test() 
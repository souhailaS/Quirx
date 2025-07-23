#!/usr/bin/env python3
"""
Test Claude with Quirx

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
    with open(config_file) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, value = line.split('=', 1)
                os.environ[key] = value

def test_claude():
    """Test Claude with Quirx"""
    load_config()
    
    from quirx.core.mutator import Mutator
    from quirx.core.runner import LLMRunner
    from quirx.core.comparer import OutputComparer
    
    print("Testing Claude with Quirx")
    print("="*40)
    
    # Use the working model name we found
    model_name = 'claude-3-5-sonnet-20241022'  # Update based on what works
    
    try:
        runner = LLMRunner(provider='anthropic')
        
        # Test connection
        if not runner.test_connection():
            print("Connection failed")
            return
        
        print("Claude connection successful!")
        
        # Simple test
        prompt = "Classify the sentiment: I love this product!"
        
        response = runner.run_prompt(prompt, model=model_name)
        
        if response.error:
            print(f"Error: {response.error}")
        else:
            print(f"Response: {response.text}")
            print(f"Tokens: {response.tokens_used}, Time: {response.response_time:.2f}s")
            
            # Test with one mutation
            mutator = Mutator(seed=42)
            mutations = mutator.generate_mutations(prompt, count=1)
            
            if mutations:
                print(f"\nTesting mutation: {mutations[0].description}")
                mutated_response = runner.run_prompt(mutations[0].mutated_text, model=model_name)
                
                if not mutated_response.error:
                    comparer = OutputComparer()
                    comparison = comparer.compare_outputs(response.text, mutated_response.text)
                    print(f"Mutation result: {comparison.classification.value} (similarity: {comparison.overall_similarity:.3f})")
                    print(f"Mutated response: {mutated_response.text}")
    
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_claude() 
#!/usr/bin/env python3
"""
Test script for summarization task evaluation

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
        return False
    
    with open(config_file) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, value = line.split('=', 1)
                os.environ[key] = value
    
    return True

def test_summarization():
    """Test the summarization task specifically"""
    if not load_config():
        return
    
    from quirx.core.mutator import Mutator
    from quirx.core.runner import LLMRunner
    from quirx.core.comparer import OutputComparer
    from quirx.core.reporter import Reporter, FuzzingResult, FuzzingReport
    
    print("Testing Summarization Task")
    print("="*50)
    
    # Summarization test case
    test_case = {
        'name': 'Text Summarization',
        'prompt_file': 'examples/prompt_summarizer.txt',
        'input': 'The quarterly earnings report reveals strong performance across all business segments. Revenue increased by 15% compared to the previous quarter, driven primarily by robust sales in the technology division and expanded international operations. Operating margins improved from 18% to 22%, reflecting successful cost optimization initiatives and improved operational efficiency. The company also announced plans to invest $50 million in research and development over the next fiscal year, focusing on artificial intelligence and sustainable technology solutions. Customer satisfaction scores reached an all-time high of 94%, while employee retention rates improved by 8%. Looking ahead, management expects continued growth momentum with projected revenue increases of 12-18% for the upcoming quarter.',
        'mutations': 4
    }
    
    # Test with one model for quick verification
    provider = 'openai'
    model = 'gpt-3.5-turbo'
    
    print(f"Testing {provider} - {model}")
    print(f"Input: {test_case['input'][:100]}...")
    
    try:
        # Load prompt
        with open(test_case['prompt_file'], 'r') as f:
            prompt = f.read().strip()
        
        full_prompt = f"{prompt}\n\n{test_case['input']}"
        print(f"Full prompt length: {len(full_prompt)} characters")
        
        # Initialize components
        mutator = Mutator(seed=42)
        runner = LLMRunner(provider=provider)
        comparer = OutputComparer()
        
        # Test connection
        if not runner.test_connection():
            print(f"Connection failed for {provider}")
            return
        
        print(f"Connected to {provider}")
        
        # Generate mutations
        mutations = mutator.generate_mutations(full_prompt, count=test_case['mutations'])
        print(f"Generated {len(mutations)} mutations:")
        for i, mutation in enumerate(mutations):
            print(f"  {i+1}. {mutation.description}")
        
        # Get original response
        print("\nGetting original response...")
        original_response = runner.run_prompt(full_prompt, model=model)
        
        if original_response.error:
            print(f"Original request failed: {original_response.error}")
            return
        
        print(f"Original response: {original_response.text}")
        print(f"Tokens: {original_response.tokens_used}, Time: {original_response.response_time:.2f}s")
        
        # Process mutations
        print(f"\nProcessing {len(mutations)} mutations...")
        results = []
        
        for i, mutation in enumerate(mutations):
            print(f"\nMutation {i+1}: {mutation.description}")
            
            mutated_response = runner.run_prompt(
                mutation.mutated_text, 
                model=model,
                rate_limit_delay=1.0  # Be respectful
            )
            
            if mutated_response.error:
                print(f"  Error: {mutated_response.error}")
                continue
            
            comparison = comparer.compare_outputs(
                original_response.text,
                mutated_response.text
            )
            
            print(f"  Response: {mutated_response.text}")
            print(f"  Classification: {comparison.classification.value}")
            print(f"  Similarity: {comparison.overall_similarity:.3f}")
            print(f"  Token similarity: {comparison.token_similarity:.3f}")
            print(f"  Semantic similarity: {comparison.semantic_similarity:.3f}")
            print(f"  Structural similarity: {comparison.structural_similarity:.3f}")
            
            results.append({
                'mutation': mutation,
                'response': mutated_response,
                'comparison': comparison
            })
        
        # Calculate summary
        if results:
            equivalent = sum(1 for r in results if r['comparison'].classification.value == 'equivalent')
            minor = sum(1 for r in results if r['comparison'].classification.value == 'minor_variation')
            deviation = sum(1 for r in results if r['comparison'].classification.value == 'behavioral_deviation')
            
            robustness = (equivalent * 1.0 + minor * 0.7) / len(results)
            
            print(f"\n" + "="*50)
            print(f"SUMMARIZATION TASK RESULTS:")
            print(f"  Robustness Score: {robustness:.2f}/1.00")
            print(f"  Equivalent: {equivalent}/{len(results)} ({equivalent/len(results)*100:.1f}%)")
            print(f"  Minor Variations: {minor}/{len(results)} ({minor/len(results)*100:.1f}%)")
            print(f"  Behavioral Deviations: {deviation}/{len(results)} ({deviation/len(results)*100:.1f}%)")
            
            # Expected results from paper: 0.52 robustness, 75% minor, 25% deviation
            print(f"\nExpected from paper: 0.52 robustness, 75% minor variations, 25% deviations")
            
            if abs(robustness - 0.52) < 0.1:
                print("✓ Robustness score matches expected range")
            else:
                print(f"⚠ Robustness score differs from expected (got {robustness:.2f}, expected ~0.52)")
        
        print(f"\nSummarization task test completed successfully!")
        
    except Exception as e:
        print(f"Test failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_summarization() 
#!/usr/bin/env python3
"""
Evaluation script for testing Quirx with OpenAI and Claude APIs

@author: souhailaS
"""

import os
import sys
from datetime import datetime

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from quirx.core.mutator import Mutator
from quirx.core.runner import LLMRunner
from quirx.core.comparer import OutputComparer
from quirx.core.reporter import Reporter, FuzzingResult, FuzzingReport


def test_provider(provider_name, model_name, prompt_file, input_text, mutations_count=5):
    """Test a specific provider with the given parameters"""
    print(f"\n{'='*60}")
    print(f"Testing {provider_name.upper()} - {model_name}")
    print(f"{'='*60}")
    
    try:
        # Load prompt
        with open(prompt_file, 'r') as f:
            prompt = f.read().strip()
        
        if input_text:
            full_prompt = f"{prompt}\n\n{input_text}"
        else:
            full_prompt = prompt
        
        print(f"Prompt file: {prompt_file}")
        print(f"Input: {input_text}")
        print(f"Mutations: {mutations_count}")
        
        # Initialize components
        print("\n1. Initializing components...")
        mutator = Mutator(seed=42)  # Use seed for reproducible results
        runner = LLMRunner(provider=provider_name)
        comparer = OutputComparer()
        reporter = Reporter()
        
        # Test connection
        print("2. Testing API connection...")
        if not runner.test_connection():
            print(f"   ERROR: Could not connect to {provider_name}")
            return False
        print(f"   Connected to {provider_name} successfully!")
        
        # Generate mutations
        print("3. Generating mutations...")
        mutations = mutator.generate_mutations(full_prompt, count=mutations_count)
        print(f"   Generated {len(mutations)} mutations")
        
        # Get original response
        print("4. Getting original response...")
        original_response = runner.run_prompt(full_prompt, model=model_name)
        
        if original_response.error:
            print(f"   ERROR: {original_response.error}")
            return False
        
        print(f"   Original response: {original_response.text[:100]}...")
        print(f"   Tokens used: {original_response.tokens_used}")
        print(f"   Response time: {original_response.response_time:.2f}s")
        
        # Process mutations
        print("5. Processing mutations...")
        results = []
        
        for i, mutation in enumerate(mutations):
            print(f"   Processing mutation {i+1}/{len(mutations)}: {mutation.description}")
            
            mutated_response = runner.run_prompt(
                mutation.mutated_text, 
                model=model_name,
                rate_limit_delay=1.0  # Be respectful to APIs
            )
            
            if mutated_response.error:
                print(f"     ERROR: {mutated_response.error}")
                continue
            
            comparison = comparer.compare_outputs(
                original_response.text,
                mutated_response.text
            )
            
            result = FuzzingResult(
                mutation=mutation,
                original_response=original_response,
                mutated_response=mutated_response,
                comparison=comparison
            )
            results.append(result)
            
            print(f"     Classification: {comparison.classification.value}")
            print(f"     Similarity: {comparison.overall_similarity:.3f}")
        
        # Generate report
        print("6. Generating report...")
        summary = reporter.calculate_summary(results)
        
        report = FuzzingReport(
            timestamp=datetime.now().isoformat(),
            prompt_file=prompt_file,
            input_text=input_text,
            model=model_name,
            total_mutations=len(mutations),
            results=results,
            summary=summary
        )
        
        # Save reports in both formats
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        base_filename = f"evaluation_{provider_name}_{model_name.replace('-', '_')}_{timestamp}"
        
        md_report_path = reporter.save_report(report, f"{base_filename}.md", format="markdown")
        json_report_path = reporter.save_report(report, f"{base_filename}.json", format="json")
        
        print(f"\nRESULTS SUMMARY for {provider_name.upper()}:")
        print(f"   Robustness Score: {summary['robustness_score']:.2f}/1.00")
        print(f"   Equivalent: {summary['equivalent_count']} ({summary['equivalent_percentage']:.1f}%)")
        print(f"   Minor Variations: {summary['minor_variation_count']} ({summary['minor_variation_percentage']:.1f}%)")
        print(f"   Behavioral Deviations: {summary['behavioral_deviation_count']} ({summary['behavioral_deviation_percentage']:.1f}%)")
        print(f"   Average Response Time: {summary['avg_response_time']:.2f}s")
        print(f"   MD Report: {md_report_path}")
        print(f"   JSON Report: {json_report_path}")
        
        return True
        
    except Exception as e:
        print(f"   ERROR: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Main evaluation function"""
    print("Quirx API Evaluation")
    print("=" * 50)
    
    # Check if API keys are set
    if not os.getenv('OPENAI_API_KEY'):
        print("ERROR: OPENAI_API_KEY not set. Run: source config/api_keys.env")
        return
    
    if not os.getenv('ANTHROPIC_API_KEY'):
        print("ERROR: ANTHROPIC_API_KEY not set. Run: source config/api_keys.env")
        return
    
    print("API keys loaded successfully!")
    
    # Test configuration
    test_cases = [
        {
            'prompt_file': 'examples/prompt_classifier.txt',
            'input_text': 'I absolutely love this new product! It works perfectly and exceeded my expectations.',
            'mutations': 5
        },
        {
            'prompt_file': 'examples/prompt_sql.txt', 
            'input_text': 'Show me all users who registered in the last 30 days',
            'mutations': 3
        }
    ]
    
    # API providers to test
    providers = [
        {'name': 'openai', 'model': 'gpt-3.5-turbo'},
        {'name': 'openai', 'model': 'gpt-4o-mini'},
        {'name': 'anthropic', 'model': 'claude-3-5-sonnet-20241022'},
        {'name': 'anthropic', 'model': 'claude-sonnet-4-20250514'}
    ]
    
    results = {}
    
    for test_case in test_cases:
        print(f"\n\nTEST CASE: {test_case['prompt_file']}")
        print(f"   Input: {test_case['input_text'][:50]}...")
        
        for provider in providers:
            success = test_provider(
                provider['name'],
                provider['model'], 
                test_case['prompt_file'],
                test_case['input_text'],
                test_case['mutations']
            )
            
            key = f"{provider['name']}_{provider['model']}"
            results[key] = success
    
    # Final summary
    print(f"\n\nEVALUATION COMPLETE")
    print("=" * 50)
    for provider, success in results.items():
        status = "SUCCESS" if success else "FAILED"
        print(f"   {provider}: {status}")
    
    print(f"\nCheck the 'reports/' directory for detailed analysis reports.")


if __name__ == "__main__":
    main() 
#!/usr/bin/env python3
"""
Evaluation script for Quirx with OpenAI and Claude

@author: souhailaS
"""

import os
import sys
from pathlib import Path
from datetime import datetime

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

def run_comprehensive_test():
    """Run comprehensive evaluation"""
    if not load_config():
        return
    
    from quirx.core.mutator import Mutator
    from quirx.core.runner import LLMRunner
    from quirx.core.comparer import OutputComparer
    from quirx.core.reporter import Reporter, FuzzingResult, FuzzingReport
    
    print("Quirx Comprehensive Evaluation")
    print("="*60)
    
    # Test cases
    test_cases = [
        {
            'name': 'Sentiment Classification',
            'prompt_file': 'examples/prompt_classifier.txt',
            'input': 'I absolutely love this new product! It works perfectly and exceeded all my expectations.',
            'mutations': 8
        },
        {
            'name': 'SQL Generation',
            'prompt_file': 'examples/prompt_sql.txt', 
            'input': 'Show me all users who registered in the last 30 days and have made at least one purchase',
            'mutations': 5
        }
    ]
    
    # Models to test
    models_to_test = [
        {'provider': 'openai', 'model': 'gpt-3.5-turbo'},
        {'provider': 'openai', 'model': 'gpt-4o-mini'},  # More cost-effective GPT-4 variant
        {'provider': 'anthropic', 'model': 'claude-3-5-sonnet-20241022'},  # Claude 3.5 Sonnet
        {'provider': 'anthropic', 'model': 'claude-sonnet-4-20250514'},  # Claude Sonnet 4
    ]
    
    results_summary = {}
    
    for test_case in test_cases:
        print(f"\n\nTEST CASE: {test_case['name']}")
        print(f"   Input: {test_case['input'][:60]}...")
        print("   " + "="*50)
        
        # Load prompt
        with open(test_case['prompt_file'], 'r') as f:
            prompt = f.read().strip()
        
        full_prompt = f"{prompt}\n\n{test_case['input']}"
        
        for model_config in models_to_test:
            provider = model_config['provider']
            model = model_config['model']
            
            print(f"\n   Testing {provider.upper()} - {model}")
            print("   " + "-"*40)
            
            try:
                # Initialize components
                mutator = Mutator(seed=42)
                runner = LLMRunner(provider=provider)
                comparer = OutputComparer()
                reporter = Reporter()
                
                # Test connection
                if not runner.test_connection():
                    print(f"   Connection failed for {provider}")
                    continue
                
                print(f"   Connected to {provider}")
                
                # Generate mutations
                mutations = mutator.generate_mutations(full_prompt, count=test_case['mutations'])
                print(f"   Generated {len(mutations)} mutations")
                
                # Get original response
                original_response = runner.run_prompt(full_prompt, model=model)
                
                if original_response.error:
                    print(f"   Original request failed: {original_response.error}")
                    continue
                
                print(f"   Original response: {original_response.text[:80]}...")
                print(f"   Tokens: {original_response.tokens_used}, Time: {original_response.response_time:.2f}s")
                
                # Process mutations
                test_results = []
                equivalent_count = 0
                minor_count = 0
                deviation_count = 0
                
                for i, mutation in enumerate(mutations):
                    print(f"   Mutation {i+1}/{len(mutations)}: {mutation.description}")
                    
                    mutated_response = runner.run_prompt(
                        mutation.mutated_text, 
                        model=model,
                        rate_limit_delay=0.5  # Be respectful to APIs
                    )
                    
                    if mutated_response.error:
                        print(f"      Error: {mutated_response.error}")
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
                    test_results.append(result)
                    
                    # Count classifications
                    if comparison.classification.value == 'equivalent':
                        equivalent_count += 1
                        status = "PASSED"
                    elif comparison.classification.value == 'minor_variation':
                        minor_count += 1
                        status = "WARNING"
                    else:  # behavioral_deviation
                        deviation_count += 1
                        status = "FAILED"
                    
                    print(f"      {status} {comparison.classification.value} (similarity: {comparison.overall_similarity:.3f})")
                    print(f"      Response: {mutated_response.text[:60]}...")
                
                # Calculate summary
                total_tests = len(test_results)
                if total_tests > 0:
                    robustness_score = (equivalent_count * 1.0 + minor_count * 0.7) / total_tests
                    
                    print(f"\n   RESULTS SUMMARY:")
                    print(f"      Robustness Score: {robustness_score:.2f}/1.00")
                    print(f"      Equivalent: {equivalent_count}/{total_tests} ({equivalent_count/total_tests*100:.1f}%)")
                    print(f"      Minor Variations: {minor_count}/{total_tests} ({minor_count/total_tests*100:.1f}%)")
                    print(f"      Behavioral Deviations: {deviation_count}/{total_tests} ({deviation_count/total_tests*100:.1f}%)")
                    
                    # Save detailed report
                    summary = reporter.calculate_summary(test_results)
                    report = FuzzingReport(
                        timestamp=datetime.now().isoformat(),
                        prompt_file=test_case['prompt_file'],
                        input_text=test_case['input'],
                        model=model,
                        total_mutations=len(mutations),
                        results=test_results,
                        summary=summary
                    )
                    
                    safe_name = test_case['name'].lower().replace(' ', '_')
                    safe_model = model.replace('-', '_').replace('.', '_')
                    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                    base_filename = f"evaluation_{provider}_{safe_model}_{safe_name}_{timestamp}"
                    
                    # Save both markdown and JSON reports
                    md_report_path = reporter.save_report(report, f"{base_filename}.md", format="markdown")
                    json_report_path = reporter.save_report(report, f"{base_filename}.json", format="json")
                    print(f"      MD Report: {md_report_path}")
                    print(f"      JSON Report: {json_report_path}")
                    
                    # Store for final summary
                    key = f"{provider}_{model}_{safe_name}"
                    results_summary[key] = {
                        'robustness_score': robustness_score,
                        'equivalent': equivalent_count,
                        'minor': minor_count,
                        'deviation': deviation_count,
                        'total': total_tests,
                        'success': True
                    }
                
            except Exception as e:
                print(f"   Test failed: {e}")
                results_summary[f"{provider}_{model}_{test_case['name'].lower().replace(' ', '_')}"] = {
                    'success': False,
                    'error': str(e)
                }
    
    # Final summary
    print(f"\n\nEVALUATION COMPLETE")
    print("="*60)
    
    for test_key, result in results_summary.items():
        if result.get('success'):
            print(f"PASSED {test_key}: Score {result['robustness_score']:.2f} "
                  f"({result['equivalent']}/{result['total']} equivalent)")
        else:
            print(f"FAILED {test_key}: FAILED - {result.get('error', 'Unknown error')}")
    
    print(f"\nCheck the 'reports/' directory for detailed analysis reports.")
    print(f"To test individual cases, use:")
    print(f"   python -m quirx.cli --prompt-file examples/prompt_classifier.txt --input 'test' --provider openai --mutations 10")

if __name__ == "__main__":
    run_comprehensive_test() 
#!/usr/bin/env python3
"""
Final comprehensive evaluation of Quirx with OpenAI and Claude

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
    with open(config_file) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, value = line.split('=', 1)
                os.environ[key] = value

def run_final_evaluation():
    """Run final comprehensive evaluation"""
    load_config()
    
    from quirx.core.mutator import Mutator
    from quirx.core.runner import LLMRunner
    from quirx.core.comparer import OutputComparer
    from quirx.core.reporter import Reporter, FuzzingResult, FuzzingReport
    
    print("Quirx Final Evaluation - OpenAI vs Claude")
    print("="*70)
    
    # Test configuration
    test_case = {
        'name': 'Sentiment Classification Comparison',
        'prompt_file': 'examples/prompt_classifier.txt',
        'input': 'I absolutely love this new product! It works perfectly and exceeded all my expectations.',
        'mutations': 6
    }
    
    # Models to test
    models = [
        {'provider': 'openai', 'model': 'gpt-3.5-turbo', 'name': 'OpenAI GPT-3.5-turbo'},
        {'provider': 'openai', 'model': 'gpt-4o-mini', 'name': 'OpenAI GPT-4o-mini'},
        {'provider': 'anthropic', 'model': 'claude-3-5-sonnet-20241022', 'name': 'Anthropic Claude-3.5-Sonnet'},
        {'provider': 'anthropic', 'model': 'claude-sonnet-4-20250514', 'name': 'Anthropic Claude-Sonnet-4'},
    ]
    
    # Load prompt
    with open(test_case['prompt_file'], 'r') as f:
        prompt = f.read().strip()
    
    full_prompt = f"{prompt}\n\n{test_case['input']}"
    
    print(f"Test Case: {test_case['name']}")
    print(f"   Input: {test_case['input'][:60]}...")
    print(f"   Mutations: {test_case['mutations']}")
    
    results_comparison = {}
    all_reports = []
    
    for model_config in models:
        provider = model_config['provider']
        model = model_config['model']
        name = model_config['name']
        
        print(f"\nTesting: {name}")
        print("   " + "="*50)
        
        try:
            # Initialize
            mutator = Mutator(seed=42)  # Same seed for fair comparison
            runner = LLMRunner(provider=provider)
            comparer = OutputComparer()
            reporter = Reporter()
            
            # Generate mutations
            mutations = mutator.generate_mutations(full_prompt, count=test_case['mutations'])
            print(f"   Generated {len(mutations)} mutations")
            
            # Get original response
            original_response = runner.run_prompt(full_prompt, model=model)
            
            if original_response.error:
                print(f"   Failed: {original_response.error}")
                continue
            
            print(f"   Original: {original_response.text}")
            print(f"   Tokens: {original_response.tokens_used}, Time: {original_response.response_time:.2f}s")
            
            # Process mutations
            test_results = []
            classifications = {'equivalent': 0, 'minor_variation': 0, 'behavioral_deviation': 0}
            
            for i, mutation in enumerate(mutations):
                print(f"   Mutation {i+1}: {mutation.description}")
                
                mutated_response = runner.run_prompt(
                    mutation.mutated_text, 
                    model=model,
                    rate_limit_delay=0.3
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
                
                # Track classification
                classifications[comparison.classification.value] += 1
                
                # Status icon
                if comparison.classification.value == 'equivalent':
                    status = "PASSED"
                elif comparison.classification.value == 'minor_variation':
                    status = "WARNING"
                else:
                    status = "FAILED"
                
                print(f"      {status} {comparison.classification.value} (similarity: {comparison.overall_similarity:.3f})")
                print(f"      Response: {mutated_response.text}")
            
            # Calculate results
            total = len(test_results)
            if total > 0:
                robustness = (classifications['equivalent'] * 1.0 + classifications['minor_variation'] * 0.7) / total
                
                print(f"\n   RESULTS:")
                print(f"      Robustness Score: {robustness:.2f}/1.00")
                print(f"      Equivalent: {classifications['equivalent']}/{total} ({classifications['equivalent']/total*100:.1f}%)")
                print(f"      Minor: {classifications['minor_variation']}/{total} ({classifications['minor_variation']/total*100:.1f}%)")
                print(f"      Deviations: {classifications['behavioral_deviation']}/{total} ({classifications['behavioral_deviation']/total*100:.1f}%)")
                
                # Store results
                results_comparison[name] = {
                    'robustness_score': robustness,
                    'equivalent': classifications['equivalent'],
                    'minor': classifications['minor_variation'],
                    'deviation': classifications['behavioral_deviation'],
                    'total': total,
                    'avg_time': sum(r.original_response.response_time + r.mutated_response.response_time for r in test_results) / (total * 2),
                    'avg_tokens': sum(r.original_response.tokens_used + r.mutated_response.tokens_used for r in test_results) / (total * 2)
                }
                
                # Generate detailed report
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
                
                safe_name = name.lower().replace(' ', '_').replace('-', '_').replace('.', '_')
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                base_filename = f"final_evaluation_{safe_name}_{timestamp}"
                
                # Save both markdown and JSON reports
                md_report_path = reporter.save_report(report, f"{base_filename}.md", format="markdown")
                json_report_path = reporter.save_report(report, f"{base_filename}.json", format="json")
                print(f"      MD Report: {md_report_path}")
                print(f"      JSON Report: {json_report_path}")
                
                all_reports.append(md_report_path)
                all_reports.append(json_report_path)
        
        except Exception as e:
            print(f"   Failed: {e}")
            results_comparison[name] = {'error': str(e)}
    
    # Final comparison
    print(f"\n\nFINAL COMPARISON")
    print("="*70)
    
    # Sort by robustness score
    sorted_results = sorted(
        [(name, data) for name, data in results_comparison.items() if 'robustness_score' in data],
        key=lambda x: x[1]['robustness_score'],
        reverse=True
    )
    
    print("ROBUSTNESS RANKING:")
    for i, (name, data) in enumerate(sorted_results):
        rank = f"{i+1}."
        print(f"   {rank} {name}: {data['robustness_score']:.2f}/1.00")
        print(f"      {data['equivalent']}/{data['total']} equivalent ({data['equivalent']/data['total']*100:.1f}%)")
        print(f"      Avg time: {data['avg_time']:.2f}s, Avg tokens: {data['avg_tokens']:.0f}")
        print()
    
    print("KEY INSIGHTS:")
    if sorted_results:
        best = sorted_results[0]
        print(f"   • Most robust: {best[0]} ({best[1]['robustness_score']:.2f}/1.00)")
        
        if len(sorted_results) > 1:
            fastest = min(sorted_results, key=lambda x: x[1]['avg_time'])
            print(f"   • Fastest: {fastest[0]} ({fastest[1]['avg_time']:.2f}s avg)")
    
    print(f"\nDetailed reports saved:")
    for report in all_reports:
        print(f"   • {report}")
    
    print(f"\nCONCLUSION: Quirx successfully evaluated prompt robustness across multiple LLM providers!")
    print(f"   Use these insights to choose the most robust model for your use case.")

if __name__ == "__main__":
    run_final_evaluation() 
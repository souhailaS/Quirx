#!/usr/bin/env python3
"""
Simple test script for Quirx
"""

import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from quirx.core.mutator import Mutator
from quirx.core.runner import LLMRunner
from quirx.core.comparer import OutputComparer
from quirx.core.reporter import Reporter, FuzzingResult, FuzzingReport
from datetime import datetime

def test_basic_functionality():
    """Test basic Quirx functionality"""
    print("Testing Quirx Basic Functionality")
    print("=" * 50)
    
    # Test prompt
    prompt = """Classify the sentiment of the following text as either POSITIVE, NEGATIVE, or NEUTRAL.

Guidelines:
- Consider the overall tone and emotion
- Look for sentiment indicators like adjectives and context
- Return only one word: POSITIVE, NEGATIVE, or NEUTRAL
- Be objective in your assessment

Text to classify: I love this new product! It works perfectly."""
    
    try:
        # Initialize components
        print("1. Initializing components...")
        mutator = Mutator(seed=42)
        runner = LLMRunner(provider='mock', mock_responses=[
            "POSITIVE",
            "POSITIVE", 
            "POSITIVE",
            "NEGATIVE",  # One different response to test comparison
            "POSITIVE"
        ])
        comparer = OutputComparer()
        reporter = Reporter()
        print("   All components initialized successfully")
        
        # Generate mutations
        print("\n2. Generating mutations...")
        mutations = mutator.generate_mutations(prompt, count=5)
        print(f"   Generated {len(mutations)} mutations")
        for i, mutation in enumerate(mutations):
            print(f"   - Mutation {i+1}: {mutation.description} (severity: {mutation.severity:.2f})")
        
        # Get original response
        print("\n3. Getting original response...")
        original_response = runner.run_prompt(prompt)
        print(f"   Original response: {original_response.text}")
        
        # Process mutations
        print("\n4. Processing mutations and comparing responses...")
        results = []
        
        for i, mutation in enumerate(mutations):
            mutated_response = runner.run_prompt(mutation.mutated_text)
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
            
            print(f"   - Mutation {i+1}: {comparison.classification.value} "
                  f"(similarity: {comparison.overall_similarity:.3f})")
        
        # Generate report
        print("\n5. Generating report...")
        summary = reporter.calculate_summary(results)
        
        report = FuzzingReport(
            timestamp=datetime.now().isoformat(),
            prompt_file="test_prompt.txt",
            input_text="I love this new product! It works perfectly.",
            model="mock-model",
            total_mutations=len(mutations),
            results=results,
            summary=summary
        )
        
        print(f"   Robustness Score: {summary['robustness_score']:.2f}/1.00")
        print(f"   - Equivalent: {summary['equivalent_count']} ({summary['equivalent_percentage']:.1f}%)")
        print(f"   - Minor Variations: {summary['minor_variation_count']} ({summary['minor_variation_percentage']:.1f}%)")
        print(f"   - Behavioral Deviations: {summary['behavioral_deviation_count']} ({summary['behavioral_deviation_percentage']:.1f}%)")
        
        # Save report
        print("\n6. Saving report...")
        report_path = reporter.save_report(report, "test_report.md")
        print(f"   Report saved to: {report_path}")
        
        print("\nAll tests completed successfully!")
        return True
        
    except Exception as e:
        print(f"\nTest failed with error: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_cli_import():
    """Test that CLI can be imported"""
    try:
        print("\nTesting CLI Import")
        print("=" * 30)
        from quirx.cli import main
        print("   CLI module imported successfully")
        return True
    except Exception as e:
        print(f"   CLI import failed: {e}")
        return False

if __name__ == "__main__":
    print("Quirx Test Suite")
    print("==================")
    
    success = True
    success &= test_basic_functionality()
    success &= test_cli_import()
    
    if success:
        print("\nAll tests passed!")
        sys.exit(0)
    else:
        print("\nSome tests failed!")
        sys.exit(1) 
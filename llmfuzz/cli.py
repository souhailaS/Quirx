"""
Command-line interface for LLMFuzz

@author: souhailaS
"""

import argparse
import sys
import os
from datetime import datetime
from typing import Optional

from .core.mutator import Mutator
from .core.runner import LLMRunner
from .core.comparer import OutputComparer
from .core.reporter import Reporter, FuzzingResult, FuzzingReport


def load_prompt_file(filepath: str) -> str:
    """Load prompt from file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read().strip()
    except FileNotFoundError:
        print(f"Error: Prompt file '{filepath}' not found")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading prompt file: {e}")
        sys.exit(1)


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description="LLMFuzz - A Mutation-Based Fuzzer for Evaluating Prompt Robustness",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  llmfuzz --prompt-file prompt.txt --input "Generate a SQL query" --model gpt-4
  llmfuzz --prompt-file prompt.txt --mutations 50 --output results.md
  llmfuzz --prompt-file prompt.txt --ci-mode --format json
        """
    )
    
    # Required arguments
    parser.add_argument(
        '--prompt-file',
        required=True,
        help='File containing the base prompt to test'
    )
    
    # Optional arguments
    parser.add_argument(
        '--input',
        default='',
        help='Input query or instruction (optional)'
    )
    
    parser.add_argument(
        '--model',
        default='gpt-3.5-turbo',
        help='LLM model to query (default: gpt-3.5-turbo)'
    )
    
    parser.add_argument(
        '--provider',
        choices=['openai', 'anthropic', 'mock'],
        default='openai',
        help='LLM provider (default: openai)'
    )
    
    parser.add_argument(
        '--mutations',
        type=int,
        default=20,
        help='Number of mutations to generate (default: 20)'
    )
    
    parser.add_argument(
        '--output',
        help='Output file path for results (auto-generated if not specified)'
    )
    
    parser.add_argument(
        '--format',
        choices=['markdown', 'json', 'html'],
        default='markdown',
        help='Output format (default: markdown)'
    )
    
    parser.add_argument(
        '--ci-mode',
        action='store_true',
        help='Enable CI mode with minimal output and exit codes'
    )
    
    parser.add_argument(
        '--seed',
        type=int,
        help='Random seed for reproducible mutations'
    )
    
    parser.add_argument(
        '--api-key',
        help='API key for the LLM provider (can also use environment variables)'
    )
    
    parser.add_argument(
        '--rate-limit',
        type=float,
        default=1.0,
        help='Delay between API calls in seconds (default: 1.0)'
    )
    
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Enable verbose output'
    )
    
    args = parser.parse_args()
    
    # Validate arguments
    if not os.path.exists(args.prompt_file):
        print(f"Error: Prompt file '{args.prompt_file}' does not exist")
        sys.exit(1)
    
    if args.mutations <= 0:
        print("Error: Number of mutations must be positive")
        sys.exit(1)
    
    # Load prompt
    prompt = load_prompt_file(args.prompt_file)
    
    # Combine prompt with input if provided
    full_prompt = f"{prompt}\n\n{args.input}" if args.input else prompt
    
    if args.verbose:
        print(f"LLMFuzz - Starting analysis with {args.mutations} mutations")
        print(f"Prompt file: {args.prompt_file}")
        print(f"Model: {args.model}")
        print(f"Provider: {args.provider}")
    
    try:
        # Initialize components
        mutator = Mutator(seed=args.seed)
        runner = LLMRunner(
            provider=args.provider,
            api_key=args.api_key,
            mock_responses=["Mock response 1", "Mock response 2"] if args.provider == 'mock' else None
        )
        comparer = OutputComparer()
        reporter = Reporter()
        
        # Test connection (skip for mock provider)
        if args.provider != 'mock':
            if args.verbose:
                print("Testing LLM connection...")
            
            if not runner.test_connection():
                print("Error: Could not connect to LLM provider. Check your API key and network connection.")
                sys.exit(1)
        
        # Generate mutations
        if args.verbose:
            print("Generating mutations...")
        
        mutations = mutator.generate_mutations(full_prompt, args.mutations)
        
        if not mutations:
            print("Error: Could not generate any mutations")
            sys.exit(1)
        
        # Get original response
        if args.verbose:
            print("Getting original response...")
        
        original_response = runner.run_prompt(full_prompt, model=args.model)
        
        if original_response.error:
            print(f"Error getting original response: {original_response.error}")
            sys.exit(1)
        
        # Process mutations
        results = []
        
        for i, mutation in enumerate(mutations):
            if args.verbose:
                print(f"Processing mutation {i+1}/{len(mutations)}: {mutation.description}")
            
            # Get mutated response
            mutated_response = runner.run_prompt(
                mutation.mutated_text,
                model=args.model,
                rate_limit_delay=args.rate_limit
            )
            
            # Compare responses
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
        
        # Generate report
        summary = reporter.calculate_summary(results)
        
        report = FuzzingReport(
            timestamp=datetime.now().isoformat(),
            prompt_file=args.prompt_file,
            input_text=args.input,
            model=args.model,
            total_mutations=len(mutations),
            results=results,
            summary=summary
        )
        
        # Save or print report
        if args.output:
            filepath = reporter.save_report(
                report,
                filename=args.output,
                format=args.format,
                ci_mode=args.ci_mode
            )
            print(f"Report saved to: {filepath}")
        else:
            # Print to stdout
            content = reporter.generate_report(report, args.format, args.ci_mode)
            print(content)
        
        # CI mode exit codes
        if args.ci_mode:
            if summary['behavioral_deviation_count'] > 0:
                if args.verbose:
                    print("CI: FAILED - Behavioral deviations detected")
                sys.exit(1)
            elif summary['minor_variation_count'] > summary['total_mutations'] * 0.5:
                if args.verbose:
                    print("CI: WARNING - High variation rate")
                sys.exit(2)
            else:
                if args.verbose:
                    print("CI: PASSED - Prompt appears robust")
                sys.exit(0)
    
    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
        sys.exit(130)
    
    except Exception as e:
        print(f"Error: {e}")
        if args.verbose:
            import traceback
            traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main() 
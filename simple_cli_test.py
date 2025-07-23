#!/usr/bin/env python3
"""
Simple CLI test for LLMFuzz
"""

import sys
import os

# Add the current directory to Python path  
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Create a test argument list
test_args = [
    'llmfuzz',
    '--prompt-file', 'examples/prompt_classifier.txt',
    '--input', 'I love this product!',
    '--provider', 'mock',
    '--mutations', '3',
    '--output', 'cli_test_report.md',
    '--verbose'
]

# Set sys.argv to our test arguments
sys.argv = test_args

try:
    from llmfuzz.cli import main
    print("Testing CLI with mock provider...")
    main()
    print("CLI test completed successfully!")
    
    # Check if report was generated
    if os.path.exists('cli_test_report.md'):
        print("Report file generated successfully!")
        
        # Show first few lines of the report
        with open('cli_test_report.md', 'r') as f:
            lines = f.readlines()[:10]
            print("\nReport preview:")
            for line in lines:
                print(f"   {line.rstrip()}")
    else:
        print("Report file not found")
        
except Exception as e:
    print(f"CLI test failed: {e}")
    import traceback
    traceback.print_exc() 
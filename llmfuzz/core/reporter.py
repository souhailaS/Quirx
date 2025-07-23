"""
Report generation module for LLMFuzz results

@author: souhailaS
"""

import json
import os
from datetime import datetime
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, asdict

from .mutator import Mutation, MutationType
from .runner import LLMResponse
from .comparer import ComparisonScore, ComparisonResult


@dataclass
class FuzzingResult:
    mutation: Mutation
    original_response: LLMResponse
    mutated_response: LLMResponse
    comparison: ComparisonScore


@dataclass
class FuzzingReport:
    timestamp: str
    prompt_file: str
    input_text: str
    model: str
    total_mutations: int
    results: List[FuzzingResult]
    summary: Dict[str, Any]


class Reporter:
    """
    Generates reports in various formats
    """
    
    def __init__(self, output_dir: str = "reports"):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
    
    def generate_report(self, report: FuzzingReport, format: str = "markdown", 
                       ci_mode: bool = False) -> str:
        """
        Generate a report in the specified format
        """
        if format == "markdown":
            return self._generate_markdown_report(report, ci_mode)
        elif format == "json":
            return self._generate_json_report(report)
        elif format == "html":
            return self._generate_html_report(report)
        else:
            raise ValueError(f"Unsupported format: {format}")
    
    def save_report(self, report: FuzzingReport, filename: str = None, 
                   format: str = "markdown", ci_mode: bool = False) -> str:
        """
        Save report to file
        """
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"llmfuzz_report_{timestamp}.{format}"
        
        filepath = os.path.join(self.output_dir, filename)
        
        content = self.generate_report(report, format, ci_mode)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return filepath
    
    def _generate_markdown_report(self, report: FuzzingReport, ci_mode: bool = False) -> str:
        """Generate a markdown report"""
        md = []
        
        # Header
        md.append("# LLMFuzz Report")
        md.append("")
        
        # Metadata
        md.append("## Test Configuration")
        md.append(f"- **Timestamp:** {report.timestamp}")
        md.append(f"- **Prompt File:** {report.prompt_file}")
        md.append(f"- **Input Text:** {report.input_text}")
        md.append(f"- **Model:** {report.model}")
        md.append(f"- **Total Mutations:** {report.total_mutations}")
        md.append("")
        
        # Summary
        md.append("## Summary")
        summary = report.summary
        md.append(f"- **Robustness Score:** {summary['robustness_score']:.2f}/1.00")
        md.append(f"- **Equivalent Responses:** {summary['equivalent_count']} ({summary['equivalent_percentage']:.1f}%)")
        md.append(f"- **Minor Variations:** {summary['minor_variation_count']} ({summary['minor_variation_percentage']:.1f}%)")
        md.append(f"- **Behavioral Deviations:** {summary['behavioral_deviation_count']} ({summary['behavioral_deviation_percentage']:.1f}%)")
        md.append(f"- **Average Response Time:** {summary['avg_response_time']:.2f}s")
        md.append(f"- **Failed Mutations:** {summary['failed_mutations']}")
        md.append("")
        
        if ci_mode:
            # CI mode: minimal output
            md.append("## CI Summary")
            if summary['behavioral_deviation_count'] > 0:
                md.append("**FAILED**: Behavioral deviations detected")
            elif summary['minor_variation_count'] > summary['total_mutations'] * 0.5:
                md.append("**WARNING**: High variation rate")
            else:
                md.append("**PASSED**: Prompt appears robust")
        else:
            # Full mode: detailed results
            self._add_detailed_results(md, report)
        
        return "\n".join(md)
    
    def _add_detailed_results(self, md: List[str], report: FuzzingReport):
        """Add detailed results to markdown report"""
        md.append("## Detailed Results")
        md.append("")
        
        # Group by mutation type
        by_type = {}
        for result in report.results:
            mut_type = result.mutation.mutation_type.value
            if mut_type not in by_type:
                by_type[mut_type] = []
            by_type[mut_type].append(result)
        
        for mut_type, results in by_type.items():
            md.append(f"### {mut_type.title()} Mutations")
            md.append("")
            
            for i, result in enumerate(results):
                md.append(f"#### Mutation {i+1}: {result.mutation.description}")
                md.append("")
                md.append(f"**Severity:** {result.mutation.severity:.2f}")
                md.append(f"**Classification:** {result.comparison.classification.value}")
                md.append(f"**Overall Similarity:** {result.comparison.overall_similarity:.3f}")
                md.append("")
                
                # Show mutation
                md.append("**Original Prompt:**")
                md.append(f"```")
                md.append(result.mutation.original_text)
                md.append("```")
                md.append("")
                
                md.append("**Mutated Prompt:**")
                md.append(f"```")
                md.append(result.mutation.mutated_text)
                md.append("```")
                md.append("")
                
                # Show responses if significantly different
                if result.comparison.classification != ComparisonResult.EQUIVALENT:
                    md.append("**Original Response:**")
                    md.append(f"```")
                    md.append(result.original_response.text[:500] + ("..." if len(result.original_response.text) > 500 else ""))
                    md.append("```")
                    md.append("")
                    
                    md.append("**Mutated Response:**")
                    md.append(f"```")
                    md.append(result.mutated_response.text[:500] + ("..." if len(result.mutated_response.text) > 500 else ""))
                    md.append("```")
                    md.append("")
                
                md.append("---")
                md.append("")
    
    def _generate_json_report(self, report: FuzzingReport) -> str:
        """Generate a JSON report"""
        # Convert dataclasses to dictionaries for JSON serialization
        report_dict = asdict(report)
        
        # Convert enums to strings
        for result in report_dict['results']:
            result['mutation']['mutation_type'] = result['mutation']['mutation_type']
            result['comparison']['classification'] = result['comparison']['classification']
        
        return json.dumps(report_dict, indent=2, ensure_ascii=False)
    
    def _generate_html_report(self, report: FuzzingReport) -> str:
        """Generate an HTML report with basic visualization"""
        summary = report.summary
        
        html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LLMFuzz Report</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        .summary {{ background: #f5f5f5; padding: 20px; border-radius: 5px; margin-bottom: 20px; }}
        .metric {{ display: inline-block; margin: 10px; padding: 10px; background: white; border-radius: 3px; }}
        .equivalent {{ color: #28a745; }}
        .minor {{ color: #ffc107; }}
        .deviation {{ color: #dc3545; }}
        .result {{ border: 1px solid #ddd; margin: 10px 0; padding: 15px; border-radius: 5px; }}
        .mutation-text {{ background: #f8f9fa; padding: 10px; border-left: 3px solid #007bff; margin: 10px 0; }}
        pre {{ white-space: pre-wrap; word-wrap: break-word; }}
    </style>
</head>
<body>
    <h1>LLMFuzz Report</h1>
    
    <div class="summary">
        <h2>Summary</h2>
        <div class="metric">
            <strong>Robustness Score:</strong> {summary['robustness_score']:.2f}/1.00
        </div>
        <div class="metric">
            <strong>Total Mutations:</strong> {report.total_mutations}
        </div>
        <div class="metric equivalent">
            <strong>Equivalent:</strong> {summary['equivalent_count']} ({summary['equivalent_percentage']:.1f}%)
        </div>
        <div class="metric minor">
            <strong>Minor Variations:</strong> {summary['minor_variation_count']} ({summary['minor_variation_percentage']:.1f}%)
        </div>
        <div class="metric deviation">
            <strong>Behavioral Deviations:</strong> {summary['behavioral_deviation_count']} ({summary['behavioral_deviation_percentage']:.1f}%)
        </div>
    </div>
    
    <h2>Configuration</h2>
    <ul>
        <li><strong>Timestamp:</strong> {report.timestamp}</li>
        <li><strong>Prompt File:</strong> {report.prompt_file}</li>
        <li><strong>Model:</strong> {report.model}</li>
        <li><strong>Input:</strong> {report.input_text}</li>
    </ul>
    
    <h2>Results</h2>
"""
        
        for i, result in enumerate(report.results):
            classification_class = result.comparison.classification.value.replace('_', ' ')
            
            html += f"""
    <div class="result {result.comparison.classification.value}">
        <h3>Mutation {i+1}: {result.mutation.description}</h3>
        <p><strong>Type:</strong> {result.mutation.mutation_type.value.title()}</p>
        <p><strong>Severity:</strong> {result.mutation.severity:.2f}</p>
        <p><strong>Classification:</strong> {classification_class.title()}</p>
        <p><strong>Similarity:</strong> {result.comparison.overall_similarity:.3f}</p>
        
        <div class="mutation-text">
            <strong>Original:</strong><br>
            <pre>{result.mutation.original_text}</pre>
        </div>
        
        <div class="mutation-text">
            <strong>Mutated:</strong><br>
            <pre>{result.mutation.mutated_text}</pre>
        </div>
    </div>
"""
        
        html += """
</body>
</html>
"""
        return html
    
    def calculate_summary(self, results: List[FuzzingResult]) -> Dict[str, Any]:
        """Calculate summary statistics"""
        if not results:
            return {
                'robustness_score': 0.0,
                'equivalent_count': 0,
                'minor_variation_count': 0,
                'behavioral_deviation_count': 0,
                'equivalent_percentage': 0.0,
                'minor_variation_percentage': 0.0,
                'behavioral_deviation_percentage': 0.0,
                'avg_response_time': 0.0,
                'failed_mutations': 0,
                'total_mutations': 0
            }
        
        total = len(results)
        equivalent = sum(1 for r in results if r.comparison.classification == ComparisonResult.EQUIVALENT)
        minor = sum(1 for r in results if r.comparison.classification == ComparisonResult.MINOR_VARIATION)
        deviation = sum(1 for r in results if r.comparison.classification == ComparisonResult.BEHAVIORAL_DEVIATION)
        
        # Calculate robustness score (higher is better)
        robustness_score = (equivalent * 1.0 + minor * 0.7 + deviation * 0.0) / total
        
        # Calculate average response time
        valid_responses = [r for r in results if r.original_response.error is None and r.mutated_response.error is None]
        avg_time = 0.0
        if valid_responses:
            avg_time = sum(r.original_response.response_time + r.mutated_response.response_time 
                          for r in valid_responses) / (len(valid_responses) * 2)
        
        failed = sum(1 for r in results if r.original_response.error or r.mutated_response.error)
        
        return {
            'robustness_score': robustness_score,
            'equivalent_count': equivalent,
            'minor_variation_count': minor,
            'behavioral_deviation_count': deviation,
            'equivalent_percentage': (equivalent / total) * 100,
            'minor_variation_percentage': (minor / total) * 100,
            'behavioral_deviation_percentage': (deviation / total) * 100,
            'avg_response_time': avg_time,
            'failed_mutations': failed,
            'total_mutations': total
        } 
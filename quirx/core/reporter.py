"""
Report generation module for Quirx results

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
            filename = f"quirx_report_{timestamp}.{format}"
        
        filepath = os.path.join(self.output_dir, filename)
        
        content = self.generate_report(report, format, ci_mode)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return filepath
    
    def _generate_markdown_report(self, report: FuzzingReport, ci_mode: bool = False) -> str:
        """Generate a markdown report"""
        md = []
        
        # Header
        md.append("# Quirx Report")
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
            result['mutation']['mutation_type'] = result['mutation']['mutation_type'].value
            result['comparison']['classification'] = result['comparison']['classification'].value
        
        return json.dumps(report_dict, indent=2, ensure_ascii=False)
    
    def _generate_html_report(self, report: FuzzingReport) -> str:
        """Generate an HTML report with ECharts visualization"""
        summary = report.summary
        
        # Prepare data for charts
        classification_data = [
            {'value': summary['equivalent_count'], 'name': 'Equivalent'},
            {'value': summary['minor_variation_count'], 'name': 'Minor Variations'},
            {'value': summary['behavioral_deviation_count'], 'name': 'Behavioral Deviations'}
        ]
        
        # Mutation type analysis
        mutation_type_data = {}
        for result in report.results:
            mut_type = result.mutation.mutation_type.value.title()
            if mut_type not in mutation_type_data:
                mutation_type_data[mut_type] = {'total': 0, 'avg_similarity': 0, 'similarities': []}
            mutation_type_data[mut_type]['total'] += 1
            mutation_type_data[mut_type]['similarities'].append(result.comparison.overall_similarity)
        
        # Calculate averages
        for mut_type in mutation_type_data:
            similarities = mutation_type_data[mut_type]['similarities']
            mutation_type_data[mut_type]['avg_similarity'] = sum(similarities) / len(similarities)
        
        mutation_type_categories = list(mutation_type_data.keys())
        mutation_type_values = [mutation_type_data[cat]['avg_similarity'] for cat in mutation_type_categories]
        
        html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Quirx Report</title>
    <script src="https://cdn.jsdelivr.net/npm/echarts@5.4.3/dist/echarts.min.js"></script>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; background-color: #f8f9fa; }}
        .container {{ max-width: 1200px; margin: 0 auto; }}
        .header {{ text-align: center; margin-bottom: 20px; }}
        .summary {{ background: #ffffff; padding: 20px; border-radius: 10px; margin-bottom: 20px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
        .metric {{ display: inline-block; margin: 8px; padding: 12px 16px; background: #f8f9fa; border-radius: 8px; min-width: 120px; text-align: center; }}
        .metric strong {{ display: block; font-size: 1em; margin-bottom: 4px; }}
        .metric span {{ font-size: 1.2em; }}
        .equivalent {{ color: #28a745; border-left: 4px solid #28a745; }}
        .minor {{ color: #ffc107; border-left: 4px solid #ffc107; }}
        .deviation {{ color: #dc3545; border-left: 4px solid #dc3545; }}
        .charts-section {{ background: #ffffff; padding: 20px; border-radius: 10px; margin-bottom: 20px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
        .charts-row {{ display: flex; flex-wrap: wrap; gap: 20px; }}
        .chart-container {{ flex: 1; min-width: 300px; }}
        .chart {{ width: 100%; height: 300px; }}
        .config-section {{ background: #ffffff; padding: 20px; border-radius: 10px; margin-bottom: 20px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
        .results-section {{ background: #ffffff; padding: 20px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
        .result {{ border: 1px solid #e9ecef; margin: 15px 0; padding: 20px; border-radius: 8px; }}
        .mutation-text {{ background: #f8f9fa; padding: 15px; border-left: 4px solid #007bff; margin: 15px 0; border-radius: 5px; }}
        pre {{ white-space: pre-wrap; word-wrap: break-word; font-size: 0.9em; }}
        h1 {{ color: #2c3e50; }}
        h2 {{ color: #34495e; border-bottom: 2px solid #3498db; padding-bottom: 8px; margin-bottom: 15px; }}
        h3 {{ color: #7f8c8d; margin-bottom: 10px; }}
        @media (max-width: 768px) {{
            .charts-row {{ flex-direction: column; }}
            .metric {{ min-width: 100px; margin: 5px; padding: 8px 12px; }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Quirx Robustness Analysis Report</h1>
            <p style="color: #7f8c8d; font-size: 1.1em;"> Prompt Mutation Testing Results</p>
        </div>
        
        <div class="summary">
            <h2>Executive Summary</h2>
            <div style="display: flex; flex-wrap: wrap; justify-content: center;">
                <div class="metric">
                    <strong style="color: #3498db;">Robustness Score</strong>
                    <span style="font-size: 1.6em; color: #2c3e50;">{summary['robustness_score']:.2f}/1.00</span>
                </div>
                <div class="metric">
                    <strong style="color: #9b59b6;">Total Mutations</strong>
                    <span style="font-size: 1.6em; color: #2c3e50;">{report.total_mutations}</span>
                </div>
                <div class="metric equivalent">
                    <strong>Equivalent</strong>
                    <span>{summary['equivalent_count']} ({summary['equivalent_percentage']:.1f}%)</span>
                </div>
                <div class="metric minor">
                    <strong>Minor Variations</strong>
                    <span>{summary['minor_variation_count']} ({summary['minor_variation_percentage']:.1f}%)</span>
                </div>
                <div class="metric deviation">
                    <strong>Behavioral Deviations</strong>
                    <span>{summary['behavioral_deviation_count']} ({summary['behavioral_deviation_percentage']:.1f}%)</span>
                </div>
            </div>
        </div>
        
        <div class="charts-section">
            <h2>Visual Analytics</h2>
            <div class="charts-row">
                <div class="chart-container">
                    <h3>Robustness Score</h3>
                    <div id="robustnessGauge" class="chart"></div>
                </div>
                
                <div class="chart-container">
                    <h3>Classification Distribution</h3>
                    <div id="classificationPie" class="chart"></div>
                </div>
                
                <div class="chart-container">
                    <h3>Mutation Type Performance</h3>
                    <div id="mutationTypeBar" class="chart"></div>
                </div>
            </div>
        </div>
        
        <div class="config-section">
            <h2>Configuration</h2>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 15px;">
                <div><strong>Timestamp:</strong> {report.timestamp}</div>
                <div><strong>Prompt File:</strong> {report.prompt_file}</div>
                <div><strong>Model:</strong> {report.model}</div>
                <div><strong>Input:</strong> {report.input_text}</div>
            </div>
        </div>
        
        <div class="results-section">
            <h2>Detailed Results</h2>
"""
        
        for i, result in enumerate(report.results):
            classification_class = result.comparison.classification.value.replace('_', ' ')
            
            html += f"""
            <div class="result {result.comparison.classification.value}">
                <h3>Mutation {i+1}: {result.mutation.description}</h3>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px; margin: 15px 0;">
                    <div><strong>Type:</strong> {result.mutation.mutation_type.value.title()}</div>
                    <div><strong>Severity:</strong> {result.mutation.severity:.2f}</div>
                    <div><strong>Classification:</strong> {classification_class.title()}</div>
                    <div><strong>Similarity:</strong> {result.comparison.overall_similarity:.3f}</div>
                </div>
                
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
        
        html += f"""
        </div>
    </div>
    
    <script>
        // Robustness Score Gauge
        var robustnessChart = echarts.init(document.getElementById('robustnessGauge'));
        var robustnessOption = {{
            tooltip: {{
                formatter: '{{a}} <br/>{{b}} : {{c}}%'
            }},
            series: [
                {{
                    name: 'Robustness',
                    type: 'gauge',
                    startAngle: 180,
                    endAngle: 0,
                    center: ['50%', '75%'],
                    radius: '90%',
                    min: 0,
                    max: 1,
                    splitNumber: 8,
                    axisLine: {{
                        lineStyle: {{
                            width: 6,
                            color: [
                                [0.3, '#ff4757'],
                                [0.7, '#ffa502'],
                                [1, '#2ed573']
                            ]
                        }}
                    }},
                    pointer: {{
                        icon: 'path://M12.8,0.7l12,40.1H0.7L12.8,0.7z',
                        length: '12%',
                        width: 20,
                        offsetCenter: [0, '-60%'],
                        itemStyle: {{
                            color: 'auto'
                        }}
                    }},
                    axisTick: {{
                        length: 12,
                        lineStyle: {{
                            color: 'auto',
                            width: 2
                        }}
                    }},
                    splitLine: {{
                        length: 20,
                        lineStyle: {{
                            color: 'auto',
                            width: 5
                        }}
                    }},
                    axisLabel: {{
                        color: '#464646',
                        fontSize: 16,
                        distance: -50,
                        formatter: function (value) {{
                            return value.toFixed(1);
                        }}
                    }},
                    title: {{
                        offsetCenter: [0, '-20%'],
                        fontSize: 16
                    }},
                    detail: {{
                        fontSize: 24,
                        offsetCenter: [0, '-35%'],
                        valueAnimation: true,
                        formatter: function (value) {{
                            return Math.round(value * 100) + '%';
                        }},
                        color: 'auto'
                    }},
                    data: [
                        {{
                            value: {summary['robustness_score']:.3f},
                            name: 'Score'
                        }}
                    ]
                }}
            ]
        }};
        robustnessChart.setOption(robustnessOption);
        
        // Classification Pie Chart
        var pieChart = echarts.init(document.getElementById('classificationPie'));
        var pieOption = {{
            tooltip: {{
                trigger: 'item',
                formatter: '{{a}} <br/>{{b}}: {{c}} ({{d}}%)'
            }},
            legend: {{
                orient: 'horizontal',
                bottom: '0%',
                left: 'center'
            }},
            series: [
                {{
                    name: 'Classifications',
                    type: 'pie',
                    radius: ['30%', '60%'],
                    center: ['50%', '45%'],
                    data: {json.dumps(classification_data)},
                    itemStyle: {{
                        borderRadius: 8,
                        borderColor: '#fff',
                        borderWidth: 2
                    }},
                    emphasis: {{
                        itemStyle: {{
                            shadowBlur: 10,
                            shadowOffsetX: 0,
                            shadowColor: 'rgba(0, 0, 0, 0.5)'
                        }}
                    }},
                    color: ['#2ed573', '#ffa502', '#ff4757']
                }}
            ]
        }};
        pieChart.setOption(pieOption);
        
        // Mutation Type Bar Chart
        var barChart = echarts.init(document.getElementById('mutationTypeBar'));
        var barOption = {{
            tooltip: {{
                trigger: 'axis',
                axisPointer: {{
                    type: 'shadow'
                }}
            }},
            grid: {{
                left: '3%',
                right: '4%',
                bottom: '3%',
                containLabel: true
            }},
            xAxis: [
                {{
                    type: 'category',
                    data: {json.dumps(mutation_type_categories)},
                    axisTick: {{
                        alignWithLabel: true
                    }},
                    axisLabel: {{
                        fontSize: 12
                    }}
                }}
            ],
            yAxis: [
                {{
                    type: 'value',
                    max: 1,
                    axisLabel: {{
                        formatter: '{{value}}',
                        fontSize: 12
                    }}
                }}
            ],
            series: [
                {{
                    name: 'Average Similarity',
                    type: 'bar',
                    barWidth: '60%',
                    data: {json.dumps(mutation_type_values)},
                    itemStyle: {{
                        borderRadius: [4, 4, 0, 0],
                        color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                            {{ offset: 0, color: '#83bff6' }},
                            {{ offset: 0.5, color: '#188df0' }},
                            {{ offset: 1, color: '#188df0' }}
                        ])
                    }}
                }}
            ]
        }};
        barChart.setOption(barOption);
        
        // Make charts responsive
        window.addEventListener('resize', function() {{
            robustnessChart.resize();
            pieChart.resize();
            barChart.resize();
        }});
    </script>
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
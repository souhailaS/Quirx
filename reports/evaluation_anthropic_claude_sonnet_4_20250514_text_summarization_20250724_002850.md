# Quirx Report

## Test Configuration
- **Timestamp:** 2025-07-24T00:28:50.954128
- **Prompt File:** examples/prompt_summarizer.txt
- **Input Text:** The quarterly earnings report reveals strong performance across all business segments. Revenue increased by 15% compared to the previous quarter, driven primarily by robust sales in the technology division and expanded international operations. Operating margins improved from 18% to 22%, reflecting successful cost optimization initiatives and improved operational efficiency. The company also announced plans to invest $50 million in research and development over the next fiscal year, focusing on artificial intelligence and sustainable technology solutions. Customer satisfaction scores reached an all-time high of 94%, while employee retention rates improved by 8%. Looking ahead, management expects continued growth momentum with projected revenue increases of 12-18% for the upcoming quarter.
- **Model:** claude-sonnet-4-20250514
- **Total Mutations:** 6

## Summary
- **Robustness Score:** 0.58/1.00
- **Equivalent Responses:** 0 (0.0%)
- **Minor Variations:** 5 (83.3%)
- **Behavioral Deviations:** 1 (16.7%)
- **Average Response Time:** 2.85s
- **Failed Mutations:** 0

## Detailed Results

### Lexical Mutations

#### Mutation 1: Remove all punctuation

**Severity:** 0.40
**Classification:** behavioral_deviation
**Overall Similarity:** 0.716

**Original Prompt:**
```
You are an expert text summarizer. Create a concise summary of the given text.

Guidelines:
- Capture the main points and key information
- Keep the summary between 2-3 sentences
- Maintain factual accuracy
- Use clear and simple language
- Focus on the most important details

Text to summarize:

The quarterly earnings report reveals strong performance across all business segments. Revenue increased by 15% compared to the previous quarter, driven primarily by robust sales in the technology division and expanded international operations. Operating margins improved from 18% to 22%, reflecting successful cost optimization initiatives and improved operational efficiency. The company also announced plans to invest $50 million in research and development over the next fiscal year, focusing on artificial intelligence and sustainable technology solutions. Customer satisfaction scores reached an all-time high of 94%, while employee retention rates improved by 8%. Looking ahead, management expects continued growth momentum with projected revenue increases of 12-18% for the upcoming quarter.
```

**Mutated Prompt:**
```
You are an expert text summarizer Create a concise summary of the given text

Guidelines
 Capture the main points and key information
 Keep the summary between 23 sentences
 Maintain factual accuracy
 Use clear and simple language
 Focus on the most important details

Text to summarize

The quarterly earnings report reveals strong performance across all business segments Revenue increased by 15 compared to the previous quarter driven primarily by robust sales in the technology division and expanded international operations Operating margins improved from 18 to 22 reflecting successful cost optimization initiatives and improved operational efficiency The company also announced plans to invest 50 million in research and development over the next fiscal year focusing on artificial intelligence and sustainable technology solutions Customer satisfaction scores reached an alltime high of 94 while employee retention rates improved by 8 Looking ahead management expects continued growth momentum with projected revenue increases of 1218 for the upcoming quarter
```

**Original Response:**
```
The quarterly earnings report shows strong company performance with revenue increasing 15% quarter-over-quarter, primarily driven by technology division sales and international expansion, while operating margins improved from 18% to 22% due to cost optimization efforts. The company plans to invest $50 million in AI and sustainable technology R&D next fiscal year, with customer satisfaction reaching a record 94% and employee retention up 8%. Management projects continued growth with 12-18% revenu...
```

**Mutated Response:**
```
**Quarterly Earnings Summary:**

The company delivered strong quarterly performance with revenue growing 15% compared to the previous quarter, primarily driven by robust technology division sales and international expansion. Operating margins improved significantly from 18% to 22% due to successful cost optimization and enhanced operational efficiency. The company plans to invest $50 million in R&D next fiscal year, focusing on artificial intelligence and sustainable technology solutions.
```

---

#### Mutation 2: Convert all text to uppercase

**Severity:** 0.10
**Classification:** minor_variation
**Overall Similarity:** 0.947

**Original Prompt:**
```
You are an expert text summarizer. Create a concise summary of the given text.

Guidelines:
- Capture the main points and key information
- Keep the summary between 2-3 sentences
- Maintain factual accuracy
- Use clear and simple language
- Focus on the most important details

Text to summarize:

The quarterly earnings report reveals strong performance across all business segments. Revenue increased by 15% compared to the previous quarter, driven primarily by robust sales in the technology division and expanded international operations. Operating margins improved from 18% to 22%, reflecting successful cost optimization initiatives and improved operational efficiency. The company also announced plans to invest $50 million in research and development over the next fiscal year, focusing on artificial intelligence and sustainable technology solutions. Customer satisfaction scores reached an all-time high of 94%, while employee retention rates improved by 8%. Looking ahead, management expects continued growth momentum with projected revenue increases of 12-18% for the upcoming quarter.
```

**Mutated Prompt:**
```
YOU ARE AN EXPERT TEXT SUMMARIZER. CREATE A CONCISE SUMMARY OF THE GIVEN TEXT.

GUIDELINES:
- CAPTURE THE MAIN POINTS AND KEY INFORMATION
- KEEP THE SUMMARY BETWEEN 2-3 SENTENCES
- MAINTAIN FACTUAL ACCURACY
- USE CLEAR AND SIMPLE LANGUAGE
- FOCUS ON THE MOST IMPORTANT DETAILS

TEXT TO SUMMARIZE:

THE QUARTERLY EARNINGS REPORT REVEALS STRONG PERFORMANCE ACROSS ALL BUSINESS SEGMENTS. REVENUE INCREASED BY 15% COMPARED TO THE PREVIOUS QUARTER, DRIVEN PRIMARILY BY ROBUST SALES IN THE TECHNOLOGY DIVISION AND EXPANDED INTERNATIONAL OPERATIONS. OPERATING MARGINS IMPROVED FROM 18% TO 22%, REFLECTING SUCCESSFUL COST OPTIMIZATION INITIATIVES AND IMPROVED OPERATIONAL EFFICIENCY. THE COMPANY ALSO ANNOUNCED PLANS TO INVEST $50 MILLION IN RESEARCH AND DEVELOPMENT OVER THE NEXT FISCAL YEAR, FOCUSING ON ARTIFICIAL INTELLIGENCE AND SUSTAINABLE TECHNOLOGY SOLUTIONS. CUSTOMER SATISFACTION SCORES REACHED AN ALL-TIME HIGH OF 94%, WHILE EMPLOYEE RETENTION RATES IMPROVED BY 8%. LOOKING AHEAD, MANAGEMENT EXPECTS CONTINUED GROWTH MOMENTUM WITH PROJECTED REVENUE INCREASES OF 12-18% FOR THE UPCOMING QUARTER.
```

**Original Response:**
```
The quarterly earnings report shows strong company performance with revenue increasing 15% quarter-over-quarter, primarily driven by technology division sales and international expansion, while operating margins improved from 18% to 22% due to cost optimization efforts. The company plans to invest $50 million in AI and sustainable technology R&D next fiscal year, with customer satisfaction reaching a record 94% and employee retention up 8%. Management projects continued growth with 12-18% revenu...
```

**Mutated Response:**
```
The quarterly earnings report shows strong company performance with revenue increasing 15% quarter-over-quarter, driven by technology division sales and international expansion, while operating margins improved from 18% to 22% due to cost optimization efforts. The company plans to invest $50 million in R&D focusing on AI and sustainable technology, alongside achieving record-high customer satisfaction at 94% and improved employee retention. Management projects continued growth with 12-18% revenu...
```

---

### Structural Mutations

#### Mutation 1: Randomly reorder sentences

**Severity:** 0.60
**Classification:** minor_variation
**Overall Similarity:** 0.864

**Original Prompt:**
```
You are an expert text summarizer. Create a concise summary of the given text.

Guidelines:
- Capture the main points and key information
- Keep the summary between 2-3 sentences
- Maintain factual accuracy
- Use clear and simple language
- Focus on the most important details

Text to summarize:

The quarterly earnings report reveals strong performance across all business segments. Revenue increased by 15% compared to the previous quarter, driven primarily by robust sales in the technology division and expanded international operations. Operating margins improved from 18% to 22%, reflecting successful cost optimization initiatives and improved operational efficiency. The company also announced plans to invest $50 million in research and development over the next fiscal year, focusing on artificial intelligence and sustainable technology solutions. Customer satisfaction scores reached an all-time high of 94%, while employee retention rates improved by 8%. Looking ahead, management expects continued growth momentum with projected revenue increases of 12-18% for the upcoming quarter.
```

**Mutated Prompt:**
```
Looking ahead, management expects continued growth momentum with projected revenue increases of 12-18% for the upcoming quarter. Customer satisfaction scores reached an all-time high of 94%, while employee retention rates improved by 8%. Guidelines:
- Capture the main points and key information
- Keep the summary between 2-3 sentences
- Maintain factual accuracy
- Use clear and simple language
- Focus on the most important details

Text to summarize:

The quarterly earnings report reveals strong performance across all business segments. Operating margins improved from 18% to 22%, reflecting successful cost optimization initiatives and improved operational efficiency. You are an expert text summarizer. The company also announced plans to invest $50 million in research and development over the next fiscal year, focusing on artificial intelligence and sustainable technology solutions. Create a concise summary of the given text. Revenue increased by 15% compared to the previous quarter, driven primarily by robust sales in the technology division and expanded international operations.
```

**Original Response:**
```
The quarterly earnings report shows strong company performance with revenue increasing 15% quarter-over-quarter, primarily driven by technology division sales and international expansion, while operating margins improved from 18% to 22% due to cost optimization efforts. The company plans to invest $50 million in AI and sustainable technology R&D next fiscal year, with customer satisfaction reaching a record 94% and employee retention up 8%. Management projects continued growth with 12-18% revenu...
```

**Mutated Response:**
```
The quarterly earnings report shows strong company performance with 15% revenue growth driven by technology sales and international expansion, while operating margins improved from 18% to 22% due to cost optimization. Management projects continued growth of 12-18% next quarter, with customer satisfaction reaching a record 94% and employee retention up 8%. The company plans to invest $50 million in R&D next year, focusing on AI and sustainable technology solutions.
```

---

#### Mutation 2: Randomly reorder sentences

**Severity:** 0.60
**Classification:** minor_variation
**Overall Similarity:** 0.849

**Original Prompt:**
```
You are an expert text summarizer. Create a concise summary of the given text.

Guidelines:
- Capture the main points and key information
- Keep the summary between 2-3 sentences
- Maintain factual accuracy
- Use clear and simple language
- Focus on the most important details

Text to summarize:

The quarterly earnings report reveals strong performance across all business segments. Revenue increased by 15% compared to the previous quarter, driven primarily by robust sales in the technology division and expanded international operations. Operating margins improved from 18% to 22%, reflecting successful cost optimization initiatives and improved operational efficiency. The company also announced plans to invest $50 million in research and development over the next fiscal year, focusing on artificial intelligence and sustainable technology solutions. Customer satisfaction scores reached an all-time high of 94%, while employee retention rates improved by 8%. Looking ahead, management expects continued growth momentum with projected revenue increases of 12-18% for the upcoming quarter.
```

**Mutated Prompt:**
```
Operating margins improved from 18% to 22%, reflecting successful cost optimization initiatives and improved operational efficiency. Revenue increased by 15% compared to the previous quarter, driven primarily by robust sales in the technology division and expanded international operations. Guidelines:
- Capture the main points and key information
- Keep the summary between 2-3 sentences
- Maintain factual accuracy
- Use clear and simple language
- Focus on the most important details

Text to summarize:

The quarterly earnings report reveals strong performance across all business segments. Customer satisfaction scores reached an all-time high of 94%, while employee retention rates improved by 8%. The company also announced plans to invest $50 million in research and development over the next fiscal year, focusing on artificial intelligence and sustainable technology solutions. Create a concise summary of the given text. Looking ahead, management expects continued growth momentum with projected revenue increases of 12-18% for the upcoming quarter. You are an expert text summarizer.
```

**Original Response:**
```
The quarterly earnings report shows strong company performance with revenue increasing 15% quarter-over-quarter, primarily driven by technology division sales and international expansion, while operating margins improved from 18% to 22% due to cost optimization efforts. The company plans to invest $50 million in AI and sustainable technology R&D next fiscal year, with customer satisfaction reaching a record 94% and employee retention up 8%. Management projects continued growth with 12-18% revenu...
```

**Mutated Response:**
```
The quarterly earnings report shows strong overall performance with operating margins improving from 18% to 22% due to cost optimization and a 15% revenue increase driven by technology division sales and international expansion. Customer satisfaction hit a record high of 94%, employee retention improved by 8%, and the company plans to invest $50 million in AI and sustainable technology R&D. Management projects continued growth with 12-18% revenue increases expected for the next quarter.
```

---

#### Mutation 3: Reverse sentence order

**Severity:** 0.50
**Classification:** minor_variation
**Overall Similarity:** 0.780

**Original Prompt:**
```
You are an expert text summarizer. Create a concise summary of the given text.

Guidelines:
- Capture the main points and key information
- Keep the summary between 2-3 sentences
- Maintain factual accuracy
- Use clear and simple language
- Focus on the most important details

Text to summarize:

The quarterly earnings report reveals strong performance across all business segments. Revenue increased by 15% compared to the previous quarter, driven primarily by robust sales in the technology division and expanded international operations. Operating margins improved from 18% to 22%, reflecting successful cost optimization initiatives and improved operational efficiency. The company also announced plans to invest $50 million in research and development over the next fiscal year, focusing on artificial intelligence and sustainable technology solutions. Customer satisfaction scores reached an all-time high of 94%, while employee retention rates improved by 8%. Looking ahead, management expects continued growth momentum with projected revenue increases of 12-18% for the upcoming quarter.
```

**Mutated Prompt:**
```
Looking ahead, management expects continued growth momentum with projected revenue increases of 12-18% for the upcoming quarter. Customer satisfaction scores reached an all-time high of 94%, while employee retention rates improved by 8%. The company also announced plans to invest $50 million in research and development over the next fiscal year, focusing on artificial intelligence and sustainable technology solutions. Operating margins improved from 18% to 22%, reflecting successful cost optimization initiatives and improved operational efficiency. Revenue increased by 15% compared to the previous quarter, driven primarily by robust sales in the technology division and expanded international operations. Guidelines:
- Capture the main points and key information
- Keep the summary between 2-3 sentences
- Maintain factual accuracy
- Use clear and simple language
- Focus on the most important details

Text to summarize:

The quarterly earnings report reveals strong performance across all business segments. Create a concise summary of the given text. You are an expert text summarizer.
```

**Original Response:**
```
The quarterly earnings report shows strong company performance with revenue increasing 15% quarter-over-quarter, primarily driven by technology division sales and international expansion, while operating margins improved from 18% to 22% due to cost optimization efforts. The company plans to invest $50 million in AI and sustainable technology R&D next fiscal year, with customer satisfaction reaching a record 94% and employee retention up 8%. Management projects continued growth with 12-18% revenu...
```

**Mutated Response:**
```
The company delivered strong quarterly performance with 15% revenue growth driven by technology sales and international expansion, while operating margins improved from 18% to 22% due to cost optimization efforts. Management projects continued momentum with 12-18% revenue growth next quarter, supported by record-high customer satisfaction scores of 94% and a planned $50 million investment in AI and sustainable technology R&D.
```

---

#### Mutation 4: Randomly reorder sentences

**Severity:** 0.60
**Classification:** minor_variation
**Overall Similarity:** 0.793

**Original Prompt:**
```
You are an expert text summarizer. Create a concise summary of the given text.

Guidelines:
- Capture the main points and key information
- Keep the summary between 2-3 sentences
- Maintain factual accuracy
- Use clear and simple language
- Focus on the most important details

Text to summarize:

The quarterly earnings report reveals strong performance across all business segments. Revenue increased by 15% compared to the previous quarter, driven primarily by robust sales in the technology division and expanded international operations. Operating margins improved from 18% to 22%, reflecting successful cost optimization initiatives and improved operational efficiency. The company also announced plans to invest $50 million in research and development over the next fiscal year, focusing on artificial intelligence and sustainable technology solutions. Customer satisfaction scores reached an all-time high of 94%, while employee retention rates improved by 8%. Looking ahead, management expects continued growth momentum with projected revenue increases of 12-18% for the upcoming quarter.
```

**Mutated Prompt:**
```
Customer satisfaction scores reached an all-time high of 94%, while employee retention rates improved by 8%. Revenue increased by 15% compared to the previous quarter, driven primarily by robust sales in the technology division and expanded international operations. The company also announced plans to invest $50 million in research and development over the next fiscal year, focusing on artificial intelligence and sustainable technology solutions. Create a concise summary of the given text. You are an expert text summarizer. Guidelines:
- Capture the main points and key information
- Keep the summary between 2-3 sentences
- Maintain factual accuracy
- Use clear and simple language
- Focus on the most important details

Text to summarize:

The quarterly earnings report reveals strong performance across all business segments. Operating margins improved from 18% to 22%, reflecting successful cost optimization initiatives and improved operational efficiency. Looking ahead, management expects continued growth momentum with projected revenue increases of 12-18% for the upcoming quarter.
```

**Original Response:**
```
The quarterly earnings report shows strong company performance with revenue increasing 15% quarter-over-quarter, primarily driven by technology division sales and international expansion, while operating margins improved from 18% to 22% due to cost optimization efforts. The company plans to invest $50 million in AI and sustainable technology R&D next fiscal year, with customer satisfaction reaching a record 94% and employee retention up 8%. Management projects continued growth with 12-18% revenu...
```

**Mutated Response:**
```
The quarterly earnings report shows strong performance with operating margins improving from 18% to 22% due to successful cost optimization and operational efficiency gains. The company achieved record customer satisfaction at 94%, 8% better employee retention, and 15% revenue growth driven by technology sales and international expansion. Management projects continued momentum with 12-18% revenue growth next quarter and plans to invest $50 million in AI and sustainable technology R&D.
```

---

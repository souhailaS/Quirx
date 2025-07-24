# Quirx Report

## Test Configuration
- **Timestamp:** 2025-07-24T00:27:32.985636
- **Prompt File:** examples/prompt_summarizer.txt
- **Input Text:** The quarterly earnings report reveals strong performance across all business segments. Revenue increased by 15% compared to the previous quarter, driven primarily by robust sales in the technology division and expanded international operations. Operating margins improved from 18% to 22%, reflecting successful cost optimization initiatives and improved operational efficiency. The company also announced plans to invest $50 million in research and development over the next fiscal year, focusing on artificial intelligence and sustainable technology solutions. Customer satisfaction scores reached an all-time high of 94%, while employee retention rates improved by 8%. Looking ahead, management expects continued growth momentum with projected revenue increases of 12-18% for the upcoming quarter.
- **Model:** gpt-3.5-turbo
- **Total Mutations:** 6

## Summary
- **Robustness Score:** 0.35/1.00
- **Equivalent Responses:** 0 (0.0%)
- **Minor Variations:** 3 (50.0%)
- **Behavioral Deviations:** 3 (50.0%)
- **Average Response Time:** 0.99s
- **Failed Mutations:** 0

## Detailed Results

### Lexical Mutations

#### Mutation 1: Remove all punctuation

**Severity:** 0.40
**Classification:** minor_variation
**Overall Similarity:** 0.813

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
The quarterly earnings report shows strong performance with a 15% revenue increase driven by technology sales and international expansion. Operating margins improved from 18% to 22% due to cost optimization efforts. The company plans to invest $50 million in AI and sustainable technology, with high customer satisfaction and improved employee retention rates. Management anticipates 12-18% revenue growth in the next quarter.
```

**Mutated Response:**
```
The quarterly earnings report showed strong performance with a 15 revenue increase, driven by technology sales and international operations. Operating margins improved from 18 to 22 due to cost optimization and operational efficiency. The company plans to invest 50 million in R&D for artificial intelligence and sustainable technology. Customer satisfaction is at 94, and employee retention improved by 8. Management expects continued growth with projected revenue increases of 1218 for the next qua...
```

---

#### Mutation 2: Convert all text to uppercase

**Severity:** 0.10
**Classification:** minor_variation
**Overall Similarity:** 0.890

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
The quarterly earnings report shows strong performance with a 15% revenue increase driven by technology sales and international expansion. Operating margins improved from 18% to 22% due to cost optimization efforts. The company plans to invest $50 million in AI and sustainable technology, with high customer satisfaction and improved employee retention rates. Management anticipates 12-18% revenue growth in the next quarter.
```

**Mutated Response:**
```
The company's quarterly earnings report shows strong performance with a 15% increase in revenue driven by technology sales and international expansion. Operating margins improved from 18% to 22%, and plans to invest $50 million in research and development for AI and sustainable technology were announced. Customer satisfaction reached 94%, and employee retention rates improved by 8%. Management anticipates continued growth with projected revenue increases of 12-18% for the next quarter.
```

---

### Structural Mutations

#### Mutation 1: Randomly reorder sentences

**Severity:** 0.60
**Classification:** behavioral_deviation
**Overall Similarity:** 0.726

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
The quarterly earnings report shows strong performance with a 15% revenue increase driven by technology sales and international expansion. Operating margins improved from 18% to 22% due to cost optimization efforts. The company plans to invest $50 million in AI and sustainable technology, with high customer satisfaction and improved employee retention rates. Management anticipates 12-18% revenue growth in the next quarter.
```

**Mutated Response:**
```
The company saw a 15% revenue increase in the last quarter, with operating margins rising from 18% to 22% due to cost optimization efforts. Plans for a $50 million investment in research and development, focusing on AI and sustainable technology, were also announced.
```

---

#### Mutation 2: Randomly reorder sentences

**Severity:** 0.60
**Classification:** minor_variation
**Overall Similarity:** 0.779

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
The quarterly earnings report shows strong performance with a 15% revenue increase driven by technology sales and international expansion. Operating margins improved from 18% to 22% due to cost optimization efforts. The company plans to invest $50 million in AI and sustainable technology, with high customer satisfaction and improved employee retention rates. Management anticipates 12-18% revenue growth in the next quarter.
```

**Mutated Response:**
```
The company's quarterly earnings report shows improved operating margins and a 15% increase in revenue, driven by strong sales in the technology division and international expansion. Customer satisfaction scores and employee retention rates reached record highs, and the company plans to invest $50 million in research and development focusing on artificial intelligence and sustainable technology. Management expects continued growth momentum with projected revenue increases of 12-18% for the upcom...
```

---

#### Mutation 3: Reverse sentence order

**Severity:** 0.50
**Classification:** behavioral_deviation
**Overall Similarity:** 0.708

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
The quarterly earnings report shows strong performance with a 15% revenue increase driven by technology sales and international expansion. Operating margins improved from 18% to 22% due to cost optimization efforts. The company plans to invest $50 million in AI and sustainable technology, with high customer satisfaction and improved employee retention rates. Management anticipates 12-18% revenue growth in the next quarter.
```

**Mutated Response:**
```
The company reported a 15% increase in revenue, driven by growth in the technology division and international operations. Customer satisfaction scores hit 94%, while employee retention rates rose by 8%. Management projects revenue to grow by 12-18% in the upcoming quarter, with plans to invest $50 million in research and development, focusing on artificial intelligence and sustainable technology solutions. Operating margins improved from 18% to 22% due to successful cost optimization initiatives...
```

---

#### Mutation 4: Randomly reorder sentences

**Severity:** 0.60
**Classification:** behavioral_deviation
**Overall Similarity:** 0.725

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
The quarterly earnings report shows strong performance with a 15% revenue increase driven by technology sales and international expansion. Operating margins improved from 18% to 22% due to cost optimization efforts. The company plans to invest $50 million in AI and sustainable technology, with high customer satisfaction and improved employee retention rates. Management anticipates 12-18% revenue growth in the next quarter.
```

**Mutated Response:**
```
The company achieved record-high customer satisfaction and improved employee retention rates. Revenue increased by 15% driven by strong sales in the technology division and international expansion. Plans to invest $50 million in research and development focusing on AI and sustainable technology were also announced. Operating margins improved to 22%, with projected revenue growth of 12-18% for the next quarter.
```

---

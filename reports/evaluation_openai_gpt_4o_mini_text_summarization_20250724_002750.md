# Quirx Report

## Test Configuration
- **Timestamp:** 2025-07-24T00:27:50.434270
- **Prompt File:** examples/prompt_summarizer.txt
- **Input Text:** The quarterly earnings report reveals strong performance across all business segments. Revenue increased by 15% compared to the previous quarter, driven primarily by robust sales in the technology division and expanded international operations. Operating margins improved from 18% to 22%, reflecting successful cost optimization initiatives and improved operational efficiency. The company also announced plans to invest $50 million in research and development over the next fiscal year, focusing on artificial intelligence and sustainable technology solutions. Customer satisfaction scores reached an all-time high of 94%, while employee retention rates improved by 8%. Looking ahead, management expects continued growth momentum with projected revenue increases of 12-18% for the upcoming quarter.
- **Model:** gpt-4o-mini
- **Total Mutations:** 6

## Summary
- **Robustness Score:** 0.23/1.00
- **Equivalent Responses:** 0 (0.0%)
- **Minor Variations:** 2 (33.3%)
- **Behavioral Deviations:** 4 (66.7%)
- **Average Response Time:** 1.95s
- **Failed Mutations:** 0

## Detailed Results

### Lexical Mutations

#### Mutation 1: Remove all punctuation

**Severity:** 0.40
**Classification:** minor_variation
**Overall Similarity:** 0.795

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
The quarterly earnings report highlights a 15% revenue increase, driven by strong sales in technology and international expansion. Operating margins rose from 18% to 22%, and the company plans to invest $50 million in R&D for AI and sustainable technology. Customer satisfaction reached 94%, and employee retention improved by 8%, with management projecting a 12-18% revenue growth for the next quarter.
```

**Mutated Response:**
```
The quarterly earnings report shows strong performance, with a 15% revenue increase driven by sales in the technology division and expanded international operations. Operating margins improved from 18% to 22% due to successful cost optimization and operational efficiency. The company plans to invest $50 million in research and development, focusing on artificial intelligence and sustainable technology. Customer satisfaction reached an all-time high of 94%, and employee retention improved by 8%. ...
```

---

#### Mutation 2: Convert all text to uppercase

**Severity:** 0.10
**Classification:** minor_variation
**Overall Similarity:** 0.841

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
The quarterly earnings report highlights a 15% revenue increase, driven by strong sales in technology and international expansion. Operating margins rose from 18% to 22%, and the company plans to invest $50 million in R&D for AI and sustainable technology. Customer satisfaction reached 94%, and employee retention improved by 8%, with management projecting a 12-18% revenue growth for the next quarter.
```

**Mutated Response:**
```
The quarterly earnings report highlights strong performance with a 15% revenue increase, primarily due to sales growth in the technology division and expanded international operations. Operating margins rose from 18% to 22%, and the company plans to invest $50 million in research and development focused on artificial intelligence and sustainable technology. Customer satisfaction reached a record high of 94%, and management anticipates continued growth, projecting a revenue increase of 12-18% for...
```

---

### Structural Mutations

#### Mutation 1: Randomly reorder sentences

**Severity:** 0.60
**Classification:** behavioral_deviation
**Overall Similarity:** 0.673

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
The quarterly earnings report highlights a 15% revenue increase, driven by strong sales in technology and international expansion. Operating margins rose from 18% to 22%, and the company plans to invest $50 million in R&D for AI and sustainable technology. Customer satisfaction reached 94%, and employee retention improved by 8%, with management projecting a 12-18% revenue growth for the next quarter.
```

**Mutated Response:**
```
The quarterly earnings report indicates strong overall performance, with revenue increasing by 15% and operating margins rising from 18% to 22%. The company plans to invest $50 million in research and development in the upcoming fiscal year, focusing on artificial intelligence and sustainable technology.
```

---

#### Mutation 2: Randomly reorder sentences

**Severity:** 0.60
**Classification:** behavioral_deviation
**Overall Similarity:** 0.680

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
The quarterly earnings report highlights a 15% revenue increase, driven by strong sales in technology and international expansion. Operating margins rose from 18% to 22%, and the company plans to invest $50 million in R&D for AI and sustainable technology. Customer satisfaction reached 94%, and employee retention improved by 8%, with management projecting a 12-18% revenue growth for the next quarter.
```

**Mutated Response:**
```
The quarterly earnings report highlights strong overall performance, with customer satisfaction scores at a record high of 94% and an 8% improvement in employee retention. The company plans to invest $50 million in research and development, focusing on artificial intelligence and sustainable technology, while projecting revenue growth of 12-18% for the next quarter.
```

---

#### Mutation 3: Reverse sentence order

**Severity:** 0.50
**Classification:** behavioral_deviation
**Overall Similarity:** 0.727

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
The quarterly earnings report highlights a 15% revenue increase, driven by strong sales in technology and international expansion. Operating margins rose from 18% to 22%, and the company plans to invest $50 million in R&D for AI and sustainable technology. Customer satisfaction reached 94%, and employee retention improved by 8%, with management projecting a 12-18% revenue growth for the next quarter.
```

**Mutated Response:**
```
The company projects revenue growth of 12-18% for the upcoming quarter, bolstered by a 15% revenue increase from the previous quarter, driven by strong sales in the technology division and expanded international operations. Customer satisfaction reached a record high of 94%, while employee retention improved by 8%. Additionally, the company plans to invest $50 million in research and development focused on artificial intelligence and sustainable technology, with operating margins rising from 18%...
```

---

#### Mutation 4: Randomly reorder sentences

**Severity:** 0.60
**Classification:** behavioral_deviation
**Overall Similarity:** 0.619

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
The quarterly earnings report highlights a 15% revenue increase, driven by strong sales in technology and international expansion. Operating margins rose from 18% to 22%, and the company plans to invest $50 million in R&D for AI and sustainable technology. Customer satisfaction reached 94%, and employee retention improved by 8%, with management projecting a 12-18% revenue growth for the next quarter.
```

**Mutated Response:**
```
The quarterly earnings report highlights strong performance, with operating margins rising from 18% to 22% due to effective cost optimization and operational efficiency. Management anticipates continued growth, projecting revenue increases of 12-18% for the next quarter.
```

---

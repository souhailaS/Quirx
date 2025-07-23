# Quirx Report

## Test Configuration
- **Timestamp:** 2025-07-23T21:37:01.674053
- **Prompt File:** examples/prompt_classifier.txt
- **Input Text:** I absolutely love this new product! It works perfectly and exceeded all my expectations.
- **Model:** claude-3-5-sonnet-20241022
- **Total Mutations:** 6

## Summary
- **Robustness Score:** 1.00/1.00
- **Equivalent Responses:** 6 (100.0%)
- **Minor Variations:** 0 (0.0%)
- **Behavioral Deviations:** 0 (0.0%)
- **Average Response Time:** 1.19s
- **Failed Mutations:** 0

## Detailed Results

### Lexical Mutations

#### Mutation 1: Remove all punctuation

**Severity:** 0.40
**Classification:** equivalent
**Overall Similarity:** 1.000

**Original Prompt:**
```
Classify the sentiment of the following text as either POSITIVE, NEGATIVE, or NEUTRAL.

Guidelines:
- Consider the overall tone and emotion
- Look for sentiment indicators like adjectives and context
- Return only one word: POSITIVE, NEGATIVE, or NEUTRAL
- Be objective in your assessment

Text to classify:

I absolutely love this new product! It works perfectly and exceeded all my expectations.
```

**Mutated Prompt:**
```
Classify the sentiment of the following text as either POSITIVE NEGATIVE or NEUTRAL

Guidelines
 Consider the overall tone and emotion
 Look for sentiment indicators like adjectives and context
 Return only one word POSITIVE NEGATIVE or NEUTRAL
 Be objective in your assessment

Text to classify

I absolutely love this new product It works perfectly and exceeded all my expectations
```

---

#### Mutation 2: Convert all text to uppercase

**Severity:** 0.10
**Classification:** equivalent
**Overall Similarity:** 1.000

**Original Prompt:**
```
Classify the sentiment of the following text as either POSITIVE, NEGATIVE, or NEUTRAL.

Guidelines:
- Consider the overall tone and emotion
- Look for sentiment indicators like adjectives and context
- Return only one word: POSITIVE, NEGATIVE, or NEUTRAL
- Be objective in your assessment

Text to classify:

I absolutely love this new product! It works perfectly and exceeded all my expectations.
```

**Mutated Prompt:**
```
CLASSIFY THE SENTIMENT OF THE FOLLOWING TEXT AS EITHER POSITIVE, NEGATIVE, OR NEUTRAL.

GUIDELINES:
- CONSIDER THE OVERALL TONE AND EMOTION
- LOOK FOR SENTIMENT INDICATORS LIKE ADJECTIVES AND CONTEXT
- RETURN ONLY ONE WORD: POSITIVE, NEGATIVE, OR NEUTRAL
- BE OBJECTIVE IN YOUR ASSESSMENT

TEXT TO CLASSIFY:

I ABSOLUTELY LOVE THIS NEW PRODUCT! IT WORKS PERFECTLY AND EXCEEDED ALL MY EXPECTATIONS.
```

---

### Structural Mutations

#### Mutation 1: Randomly reorder sentences

**Severity:** 0.60
**Classification:** equivalent
**Overall Similarity:** 1.000

**Original Prompt:**
```
Classify the sentiment of the following text as either POSITIVE, NEGATIVE, or NEUTRAL.

Guidelines:
- Consider the overall tone and emotion
- Look for sentiment indicators like adjectives and context
- Return only one word: POSITIVE, NEGATIVE, or NEUTRAL
- Be objective in your assessment

Text to classify:

I absolutely love this new product! It works perfectly and exceeded all my expectations.
```

**Mutated Prompt:**
```
Classify the sentiment of the following text as either POSITIVE, NEGATIVE, or NEUTRAL Guidelines:
- Consider the overall tone and emotion
- Look for sentiment indicators like adjectives and context
- Return only one word: POSITIVE, NEGATIVE, or NEUTRAL
- Be objective in your assessment

Text to classify:

I absolutely love this new product It works perfectly and exceeded all my expectations
```

---

#### Mutation 2: Randomly reorder sentences

**Severity:** 0.60
**Classification:** equivalent
**Overall Similarity:** 1.000

**Original Prompt:**
```
Classify the sentiment of the following text as either POSITIVE, NEGATIVE, or NEUTRAL.

Guidelines:
- Consider the overall tone and emotion
- Look for sentiment indicators like adjectives and context
- Return only one word: POSITIVE, NEGATIVE, or NEUTRAL
- Be objective in your assessment

Text to classify:

I absolutely love this new product! It works perfectly and exceeded all my expectations.
```

**Mutated Prompt:**
```
Guidelines:
- Consider the overall tone and emotion
- Look for sentiment indicators like adjectives and context
- Return only one word: POSITIVE, NEGATIVE, or NEUTRAL
- Be objective in your assessment

Text to classify:

I absolutely love this new product It works perfectly and exceeded all my expectations Classify the sentiment of the following text as either POSITIVE, NEGATIVE, or NEUTRAL
```

---

#### Mutation 3: Randomly reorder sentences

**Severity:** 0.60
**Classification:** equivalent
**Overall Similarity:** 1.000

**Original Prompt:**
```
Classify the sentiment of the following text as either POSITIVE, NEGATIVE, or NEUTRAL.

Guidelines:
- Consider the overall tone and emotion
- Look for sentiment indicators like adjectives and context
- Return only one word: POSITIVE, NEGATIVE, or NEUTRAL
- Be objective in your assessment

Text to classify:

I absolutely love this new product! It works perfectly and exceeded all my expectations.
```

**Mutated Prompt:**
```
Guidelines:
- Consider the overall tone and emotion
- Look for sentiment indicators like adjectives and context
- Return only one word: POSITIVE, NEGATIVE, or NEUTRAL
- Be objective in your assessment

Text to classify:

I absolutely love this new product Classify the sentiment of the following text as either POSITIVE, NEGATIVE, or NEUTRAL It works perfectly and exceeded all my expectations
```

---

#### Mutation 4: Reverse sentence order

**Severity:** 0.50
**Classification:** equivalent
**Overall Similarity:** 1.000

**Original Prompt:**
```
Classify the sentiment of the following text as either POSITIVE, NEGATIVE, or NEUTRAL.

Guidelines:
- Consider the overall tone and emotion
- Look for sentiment indicators like adjectives and context
- Return only one word: POSITIVE, NEGATIVE, or NEUTRAL
- Be objective in your assessment

Text to classify:

I absolutely love this new product! It works perfectly and exceeded all my expectations.
```

**Mutated Prompt:**
```
It works perfectly and exceeded all my expectations Guidelines:
- Consider the overall tone and emotion
- Look for sentiment indicators like adjectives and context
- Return only one word: POSITIVE, NEGATIVE, or NEUTRAL
- Be objective in your assessment

Text to classify:

I absolutely love this new product Classify the sentiment of the following text as either POSITIVE, NEGATIVE, or NEUTRAL
```

---

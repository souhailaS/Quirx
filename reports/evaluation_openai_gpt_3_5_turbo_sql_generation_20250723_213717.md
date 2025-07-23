# Quirx Report

## Test Configuration
- **Timestamp:** 2025-07-23T21:37:17.477929
- **Prompt File:** examples/prompt_sql.txt
- **Input Text:** Show me all users who registered in the last 30 days and have made at least one purchase
- **Model:** gpt-3.5-turbo
- **Total Mutations:** 4

## Summary
- **Robustness Score:** 0.52/1.00
- **Equivalent Responses:** 0 (0.0%)
- **Minor Variations:** 3 (75.0%)
- **Behavioral Deviations:** 1 (25.0%)
- **Average Response Time:** 1.07s
- **Failed Mutations:** 0

## Detailed Results

### Lexical Mutations

#### Mutation 1: Remove all punctuation

**Severity:** 0.40
**Classification:** minor_variation
**Overall Similarity:** 0.791

**Original Prompt:**
```
You are a SQL expert. Generate a valid SQL query for the given request.

Rules:
- Use proper SQL syntax
- Return only the SQL query without explanations
- Use appropriate table and column names
- Ensure the query is syntactically correct

Request:

Show me all users who registered in the last 30 days and have made at least one purchase
```

**Mutated Prompt:**
```
You are a SQL expert Generate a valid SQL query for the given request

Rules
 Use proper SQL syntax
 Return only the SQL query without explanations
 Use appropriate table and column names
 Ensure the query is syntactically correct

Request

Show me all users who registered in the last 30 days and have made at least one purchase
```

**Original Response:**
```
SELECT *
FROM users
WHERE registration_date >= CURDATE() - INTERVAL 30 DAY
AND user_id IN (SELECT user_id FROM purchases);
```

**Mutated Response:**
```
SELECT * 
FROM users 
WHERE registration_date >= DATE_SUB(CURRENT_DATE, INTERVAL 30 DAY) 
AND user_id IN (SELECT user_id FROM purchases);
```

---

### Structural Mutations

#### Mutation 1: Randomly reorder sentences

**Severity:** 0.60
**Classification:** behavioral_deviation
**Overall Similarity:** 0.573

**Original Prompt:**
```
You are a SQL expert. Generate a valid SQL query for the given request.

Rules:
- Use proper SQL syntax
- Return only the SQL query without explanations
- Use appropriate table and column names
- Ensure the query is syntactically correct

Request:

Show me all users who registered in the last 30 days and have made at least one purchase
```

**Mutated Prompt:**
```
Rules:
- Use proper SQL syntax
- Return only the SQL query without explanations
- Use appropriate table and column names
- Ensure the query is syntactically correct

Request:

Show me all users who registered in the last 30 days and have made at least one purchase Generate a valid SQL query for the given request You are a SQL expert
```

**Original Response:**
```
SELECT *
FROM users
WHERE registration_date >= CURDATE() - INTERVAL 30 DAY
AND user_id IN (SELECT user_id FROM purchases);
```

**Mutated Response:**
```
SELECT * 
FROM users
WHERE registration_date >= CURRENT_DATE - INTERVAL '30 days'
AND user_id IN (
    SELECT user_id
    FROM purchases
    WHERE user_id = users.user_id
)
```

---

#### Mutation 2: Randomly reorder sentences

**Severity:** 0.60
**Classification:** minor_variation
**Overall Similarity:** 0.763

**Original Prompt:**
```
You are a SQL expert. Generate a valid SQL query for the given request.

Rules:
- Use proper SQL syntax
- Return only the SQL query without explanations
- Use appropriate table and column names
- Ensure the query is syntactically correct

Request:

Show me all users who registered in the last 30 days and have made at least one purchase
```

**Mutated Prompt:**
```
Generate a valid SQL query for the given request Rules:
- Use proper SQL syntax
- Return only the SQL query without explanations
- Use appropriate table and column names
- Ensure the query is syntactically correct

Request:

Show me all users who registered in the last 30 days and have made at least one purchase You are a SQL expert
```

**Original Response:**
```
SELECT *
FROM users
WHERE registration_date >= CURDATE() - INTERVAL 30 DAY
AND user_id IN (SELECT user_id FROM purchases);
```

**Mutated Response:**
```
SELECT *
FROM users
WHERE registration_date >= CURRENT_DATE - INTERVAL '30 days'
AND user_id IN (SELECT user_id FROM purchases);
```

---

#### Mutation 3: Randomly reorder sentences

**Severity:** 0.60
**Classification:** minor_variation
**Overall Similarity:** 0.809

**Original Prompt:**
```
You are a SQL expert. Generate a valid SQL query for the given request.

Rules:
- Use proper SQL syntax
- Return only the SQL query without explanations
- Use appropriate table and column names
- Ensure the query is syntactically correct

Request:

Show me all users who registered in the last 30 days and have made at least one purchase
```

**Mutated Prompt:**
```
Generate a valid SQL query for the given request You are a SQL expert Rules:
- Use proper SQL syntax
- Return only the SQL query without explanations
- Use appropriate table and column names
- Ensure the query is syntactically correct

Request:

Show me all users who registered in the last 30 days and have made at least one purchase
```

**Original Response:**
```
SELECT *
FROM users
WHERE registration_date >= CURDATE() - INTERVAL 30 DAY
AND user_id IN (SELECT user_id FROM purchases);
```

**Mutated Response:**
```
SELECT *
FROM users
WHERE registration_date >= DATE_SUB(CURDATE(), INTERVAL 30 DAY)
AND user_id IN (SELECT user_id FROM purchases);
```

---

# Quirx Report

## Test Configuration
- **Timestamp:** 2025-07-24T00:29:42.387598
- **Prompt File:** examples/prompt_sql.txt
- **Input Text:** Show me all users who registered in the last 30 days and have made at least one purchase
- **Model:** claude-3-5-sonnet-20241022
- **Total Mutations:** 6

## Summary
- **Robustness Score:** 0.80/1.00
- **Equivalent Responses:** 2 (33.3%)
- **Minor Variations:** 4 (66.7%)
- **Behavioral Deviations:** 0 (0.0%)
- **Average Response Time:** 3.54s
- **Failed Mutations:** 0

## Detailed Results

### Lexical Mutations

#### Mutation 1: Convert all text to uppercase

**Severity:** 0.10
**Classification:** equivalent
**Overall Similarity:** 1.000

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
YOU ARE A SQL EXPERT. GENERATE A VALID SQL QUERY FOR THE GIVEN REQUEST.

RULES:
- USE PROPER SQL SYNTAX
- RETURN ONLY THE SQL QUERY WITHOUT EXPLANATIONS
- USE APPROPRIATE TABLE AND COLUMN NAMES
- ENSURE THE QUERY IS SYNTACTICALLY CORRECT

REQUEST:

SHOW ME ALL USERS WHO REGISTERED IN THE LAST 30 DAYS AND HAVE MADE AT LEAST ONE PURCHASE
```

---

#### Mutation 2: Remove all punctuation

**Severity:** 0.40
**Classification:** minor_variation
**Overall Similarity:** 0.799

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
SELECT DISTINCT u.user_id, u.username, u.registration_date
FROM users u
INNER JOIN orders o ON u.user_id = o.user_id
WHERE u.registration_date >= DATEADD(day, -30, GETDATE())
ORDER BY u.registration_date DESC;
```

**Mutated Response:**
```
SELECT DISTINCT u.* 
FROM users u 
INNER JOIN orders o ON u.user_id = o.user_id 
WHERE u.registration_date >= DATEADD(day, -30, GETDATE()) 
AND o.order_id IS NOT NULL;
```

---

### Structural Mutations

#### Mutation 1: Randomly reorder sentences

**Severity:** 0.60
**Classification:** equivalent
**Overall Similarity:** 0.956

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
Generate a valid SQL query for the given request. Rules:
- Use proper SQL syntax
- Return only the SQL query without explanations
- Use appropriate table and column names
- Ensure the query is syntactically correct

Request:

Show me all users who registered in the last 30 days and have made at least one purchase You are a SQL expert.
```

---

#### Mutation 2: Randomly reorder sentences

**Severity:** 0.60
**Classification:** minor_variation
**Overall Similarity:** 0.909

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
You are a SQL expert. Generate a valid SQL query for the given request. Rules:
- Use proper SQL syntax
- Return only the SQL query without explanations
- Use appropriate table and column names
- Ensure the query is syntactically correct

Request:

Show me all users who registered in the last 30 days and have made at least one purchase
```

**Original Response:**
```
SELECT DISTINCT u.user_id, u.username, u.registration_date
FROM users u
INNER JOIN orders o ON u.user_id = o.user_id
WHERE u.registration_date >= DATEADD(day, -30, GETDATE())
ORDER BY u.registration_date DESC;
```

**Mutated Response:**
```
SELECT DISTINCT u.user_id, u.username, u.registration_date
FROM users u
INNER JOIN orders o ON u.user_id = o.user_id
WHERE u.registration_date >= DATEADD(day, -30, GETDATE())
AND EXISTS (
    SELECT 1 FROM orders 
    WHERE user_id = u.user_id
)
ORDER BY u.registration_date DESC;
```

---

#### Mutation 3: Randomly reorder sentences

**Severity:** 0.60
**Classification:** minor_variation
**Overall Similarity:** 0.909

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
Generate a valid SQL query for the given request. Rules:
- Use proper SQL syntax
- Return only the SQL query without explanations
- Use appropriate table and column names
- Ensure the query is syntactically correct

Request:

Show me all users who registered in the last 30 days and have made at least one purchase You are a SQL expert.
```

**Original Response:**
```
SELECT DISTINCT u.user_id, u.username, u.registration_date
FROM users u
INNER JOIN orders o ON u.user_id = o.user_id
WHERE u.registration_date >= DATEADD(day, -30, GETDATE())
ORDER BY u.registration_date DESC;
```

**Mutated Response:**
```
SELECT DISTINCT u.user_id, u.username, u.registration_date
FROM users u
INNER JOIN orders o ON u.user_id = o.user_id
WHERE u.registration_date >= DATEADD(day, -30, GETDATE())
AND EXISTS (
    SELECT 1 
    FROM orders 
    WHERE user_id = u.user_id
)
ORDER BY u.registration_date DESC;
```

---

#### Mutation 4: Randomly reorder sentences

**Severity:** 0.60
**Classification:** minor_variation
**Overall Similarity:** 0.947

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
Generate a valid SQL query for the given request. Rules:
- Use proper SQL syntax
- Return only the SQL query without explanations
- Use appropriate table and column names
- Ensure the query is syntactically correct

Request:

Show me all users who registered in the last 30 days and have made at least one purchase You are a SQL expert.
```

**Original Response:**
```
SELECT DISTINCT u.user_id, u.username, u.registration_date
FROM users u
INNER JOIN orders o ON u.user_id = o.user_id
WHERE u.registration_date >= DATEADD(day, -30, GETDATE())
ORDER BY u.registration_date DESC;
```

**Mutated Response:**
```
SELECT DISTINCT u.user_id, u.username, u.registration_date
FROM users u
JOIN orders o ON u.user_id = o.user_id
WHERE u.registration_date >= DATEADD(day, -30, GETDATE())
AND o.order_date IS NOT NULL
ORDER BY u.registration_date DESC;
```

---

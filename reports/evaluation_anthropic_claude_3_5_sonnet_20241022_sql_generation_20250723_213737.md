# Quirx Report

## Test Configuration
- **Timestamp:** 2025-07-23T21:37:37.335403
- **Prompt File:** examples/prompt_sql.txt
- **Input Text:** Show me all users who registered in the last 30 days and have made at least one purchase
- **Model:** claude-3-5-sonnet-20241022
- **Total Mutations:** 4

## Summary
- **Robustness Score:** 0.35/1.00
- **Equivalent Responses:** 0 (0.0%)
- **Minor Variations:** 2 (50.0%)
- **Behavioral Deviations:** 2 (50.0%)
- **Average Response Time:** 1.80s
- **Failed Mutations:** 0

## Detailed Results

### Lexical Mutations

#### Mutation 1: Remove all punctuation

**Severity:** 0.40
**Classification:** behavioral_deviation
**Overall Similarity:** 0.742

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
AND o.order_id IS NOT NULL
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
**Classification:** minor_variation
**Overall Similarity:** 0.833

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
SELECT DISTINCT u.user_id, u.username, u.registration_date
FROM users u
INNER JOIN orders o ON u.user_id = o.user_id
WHERE u.registration_date >= DATEADD(day, -30, GETDATE())
AND o.order_id IS NOT NULL
ORDER BY u.registration_date DESC;
```

**Mutated Response:**
```
SELECT DISTINCT u.user_id, u.username, u.registration_date
FROM users u
INNER JOIN orders o ON u.user_id = o.user_id
WHERE u.registration_date >= DATE_SUB(CURDATE(), INTERVAL 30 DAY)
AND o.order_id IS NOT NULL
ORDER BY u.registration_date DESC;
```

---

#### Mutation 2: Randomly reorder sentences

**Severity:** 0.60
**Classification:** minor_variation
**Overall Similarity:** 0.833

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
SELECT DISTINCT u.user_id, u.username, u.registration_date
FROM users u
INNER JOIN orders o ON u.user_id = o.user_id
WHERE u.registration_date >= DATEADD(day, -30, GETDATE())
AND o.order_id IS NOT NULL
ORDER BY u.registration_date DESC;
```

**Mutated Response:**
```
SELECT DISTINCT u.user_id, u.username, u.registration_date
FROM users u
INNER JOIN orders o ON u.user_id = o.user_id
WHERE u.registration_date >= DATE_SUB(CURRENT_DATE, INTERVAL 30 DAY)
AND o.order_id IS NOT NULL
ORDER BY u.registration_date DESC;
```

---

#### Mutation 3: Randomly reorder sentences

**Severity:** 0.60
**Classification:** behavioral_deviation
**Overall Similarity:** 0.742

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
SELECT DISTINCT u.user_id, u.username, u.registration_date
FROM users u
INNER JOIN orders o ON u.user_id = o.user_id
WHERE u.registration_date >= DATEADD(day, -30, GETDATE())
AND o.order_id IS NOT NULL
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

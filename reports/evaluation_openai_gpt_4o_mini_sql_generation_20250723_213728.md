# Quirx Report

## Test Configuration
- **Timestamp:** 2025-07-23T21:37:28.062265
- **Prompt File:** examples/prompt_sql.txt
- **Input Text:** Show me all users who registered in the last 30 days and have made at least one purchase
- **Model:** gpt-4o-mini
- **Total Mutations:** 4

## Summary
- **Robustness Score:** 0.60/1.00
- **Equivalent Responses:** 1 (25.0%)
- **Minor Variations:** 2 (50.0%)
- **Behavioral Deviations:** 1 (25.0%)
- **Average Response Time:** 1.85s
- **Failed Mutations:** 0

## Detailed Results

### Lexical Mutations

#### Mutation 1: Remove all punctuation

**Severity:** 0.40
**Classification:** behavioral_deviation
**Overall Similarity:** 0.710

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
```sql
SELECT u.user_id, u.username, u.registration_date
FROM users u
JOIN purchases p ON u.user_id = p.user_id
WHERE u.registration_date >= NOW() - INTERVAL 30 DAY
GROUP BY u.user_id
HAVING COUNT(p.purchase_id) >= 1;
```
```

**Mutated Response:**
```
```sql
SELECT u.*
FROM users u
JOIN purchases p ON u.user_id = p.user_id
WHERE u.registration_date >= NOW() - INTERVAL '30 days'
GROUP BY u.user_id;
```
```

---

### Structural Mutations

#### Mutation 1: Randomly reorder sentences

**Severity:** 0.60
**Classification:** minor_variation
**Overall Similarity:** 0.796

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
```sql
SELECT u.user_id, u.username, u.registration_date
FROM users u
JOIN purchases p ON u.user_id = p.user_id
WHERE u.registration_date >= NOW() - INTERVAL 30 DAY
GROUP BY u.user_id
HAVING COUNT(p.purchase_id) >= 1;
```
```

**Mutated Response:**
```
```sql
SELECT DISTINCT u.user_id, u.username, u.registration_date
FROM users u
JOIN purchases p ON u.user_id = p.user_id
WHERE u.registration_date >= NOW() - INTERVAL 30 DAY;
```
```

---

#### Mutation 2: Randomly reorder sentences

**Severity:** 0.60
**Classification:** minor_variation
**Overall Similarity:** 0.941

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
```sql
SELECT u.user_id, u.username, u.registration_date
FROM users u
JOIN purchases p ON u.user_id = p.user_id
WHERE u.registration_date >= NOW() - INTERVAL 30 DAY
GROUP BY u.user_id
HAVING COUNT(p.purchase_id) >= 1;
```
```

**Mutated Response:**
```
```sql
SELECT u.user_id, u.username, u.registration_date
FROM users u
JOIN purchases p ON u.user_id = p.user_id
WHERE u.registration_date >= NOW() - INTERVAL 30 DAY
GROUP BY u.user_id
HAVING COUNT(p.purchase_id) > 0;
```
```

---

#### Mutation 3: Randomly reorder sentences

**Severity:** 0.60
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
Generate a valid SQL query for the given request You are a SQL expert Rules:
- Use proper SQL syntax
- Return only the SQL query without explanations
- Use appropriate table and column names
- Ensure the query is syntactically correct

Request:

Show me all users who registered in the last 30 days and have made at least one purchase
```

---

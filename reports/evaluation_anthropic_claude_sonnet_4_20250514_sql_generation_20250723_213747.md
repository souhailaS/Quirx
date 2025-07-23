# Quirx Report

## Test Configuration
- **Timestamp:** 2025-07-23T21:37:47.835792
- **Prompt File:** examples/prompt_sql.txt
- **Input Text:** Show me all users who registered in the last 30 days and have made at least one purchase
- **Model:** claude-sonnet-4-20250514
- **Total Mutations:** 4

## Summary
- **Robustness Score:** 0.85/1.00
- **Equivalent Responses:** 2 (50.0%)
- **Minor Variations:** 2 (50.0%)
- **Behavioral Deviations:** 0 (0.0%)
- **Average Response Time:** 1.81s
- **Failed Mutations:** 0

## Detailed Results

### Lexical Mutations

#### Mutation 1: Remove all punctuation

**Severity:** 0.40
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
You are a SQL expert Generate a valid SQL query for the given request

Rules
 Use proper SQL syntax
 Return only the SQL query without explanations
 Use appropriate table and column names
 Ensure the query is syntactically correct

Request

Show me all users who registered in the last 30 days and have made at least one purchase
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
SELECT DISTINCT u.*
FROM users u
INNER JOIN purchases p ON u.user_id = p.user_id
WHERE u.registration_date >= DATE_SUB(CURRENT_DATE, INTERVAL 30 DAY);
```
```

**Mutated Response:**
```
```sql
SELECT DISTINCT u.*
FROM users u
INNER JOIN purchases p ON u.user_id = p.user_id
WHERE u.registration_date >= DATEADD(day, -30, GETDATE());
```
```

---

#### Mutation 2: Randomly reorder sentences

**Severity:** 0.60
**Classification:** minor_variation
**Overall Similarity:** 0.946

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
SELECT DISTINCT u.*
FROM users u
INNER JOIN purchases p ON u.user_id = p.user_id
WHERE u.registration_date >= DATE_SUB(CURRENT_DATE, INTERVAL 30 DAY);
```
```

**Mutated Response:**
```
```sql
SELECT DISTINCT u.*
FROM users u
INNER JOIN purchases p ON u.user_id = p.user_id
WHERE u.registration_date >= DATE_SUB(CURDATE(), INTERVAL 30 DAY);
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

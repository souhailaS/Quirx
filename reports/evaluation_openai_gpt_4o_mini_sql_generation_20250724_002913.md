# Quirx Report

## Test Configuration
- **Timestamp:** 2025-07-24T00:29:13.044767
- **Prompt File:** examples/prompt_sql.txt
- **Input Text:** Show me all users who registered in the last 30 days and have made at least one purchase
- **Model:** gpt-4o-mini
- **Total Mutations:** 6

## Summary
- **Robustness Score:** 0.80/1.00
- **Equivalent Responses:** 2 (33.3%)
- **Minor Variations:** 4 (66.7%)
- **Behavioral Deviations:** 0 (0.0%)
- **Average Response Time:** 1.58s
- **Failed Mutations:** 0

## Detailed Results

### Lexical Mutations

#### Mutation 1: Remove all punctuation

**Severity:** 0.40
**Classification:** minor_variation
**Overall Similarity:** 0.841

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
WHERE u.registration_date >= NOW() - INTERVAL 30 DAY
GROUP BY u.user_id;
```
```

---

#### Mutation 2: Convert all text to uppercase

**Severity:** 0.10
**Classification:** minor_variation
**Overall Similarity:** 0.801

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
SELECT DISTINCT u.*
FROM users u
JOIN purchases p ON u.user_id = p.user_id
WHERE u.registration_date >= NOW() - INTERVAL 30 DAY;
```
```

---

### Structural Mutations

#### Mutation 1: Randomly reorder sentences

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
Generate a valid SQL query for the given request. You are a SQL expert. Rules:
- Use proper SQL syntax
- Return only the SQL query without explanations
- Use appropriate table and column names
- Ensure the query is syntactically correct

Request:

Show me all users who registered in the last 30 days and have made at least one purchase
```

---

#### Mutation 3: Reverse sentence order

**Severity:** 0.50
**Classification:** minor_variation
**Overall Similarity:** 0.908

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

Show me all users who registered in the last 30 days and have made at least one purchase Generate a valid SQL query for the given request. You are a SQL expert.
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

#### Mutation 4: Randomly reorder sentences

**Severity:** 0.60
**Classification:** minor_variation
**Overall Similarity:** 0.841

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
WHERE u.registration_date >= NOW() - INTERVAL 30 DAY
GROUP BY u.user_id;
```
```

---

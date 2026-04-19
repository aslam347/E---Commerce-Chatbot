from groq import Groq
import os
import re
import sqlite3
import pandas as pd
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# -------------------------------
# ENV VARIABLES
# -------------------------------
GROQ_MODEL = os.getenv("GROQ_MODEL")
client_sql = Groq()

# -------------------------------
# DATABASE PATH
# -------------------------------
db_path = Path(__file__).parent / "db.sqlite"

# -------------------------------
# PROMPT
# -------------------------------
sql_prompt = """
You are an expert SQLite query generator.

Database Name: db.sqlite

Table Name: product

Columns:
product_link TEXT
title TEXT
brand TEXT
price INTEGER
discount REAL
avg_rating REAL
total_ratings INTEGER

Rules:
1. Use ONLY SQLite syntax
2. Table name is product
3. Use SELECT *
4. Use LIKE for text search
5. Never use ILIKE
6. Return only SQL query inside <SQL></SQL>

Examples:

User: give shoe under 2000

<SQL>
SELECT * FROM product
WHERE LOWER(title) LIKE '%shoe%'
AND price <= 2000
LIMIT 5;
</SQL>

User: give nike shoe under 5000

<SQL>
SELECT * FROM product
WHERE LOWER(brand) LIKE '%nike%'
AND LOWER(title) LIKE '%shoe%'
AND price <= 5000
LIMIT 5;
</SQL>
"""

# -------------------------------
# GENERATE SQL
# -------------------------------
def generate_sql_query(question):
    chat_completion = client_sql.chat.completions.create(
        messages=[
            {"role": "system", "content": sql_prompt},
            {"role": "user", "content": question}
        ],
        model=GROQ_MODEL,
        temperature=0.2,
        max_tokens=500
    )

    return chat_completion.choices[0].message.content


# -------------------------------
# RUN QUERY
# -------------------------------
def run_query(query):
    try:
        if query.strip().upper().startswith("SELECT"):
            with sqlite3.connect(db_path) as conn:
                df = pd.read_sql_query(query, conn)
                return df.head(5)

    except Exception as e:
        return f"SQL Error: {str(e)}"

    return None


# -------------------------------
# MAIN SQL CHAIN
# -------------------------------
def sql_chain(question):
    sql_query = generate_sql_query(question)

    pattern = r"<SQL>(.*?)</SQL>"
    matches = re.findall(pattern, sql_query, re.DOTALL)

    if not matches:
        return "Sorry, unable to generate SQL query."

    query = matches[0].strip()

    print("Generated SQL:")
    print(query)

    response = run_query(query)

    if isinstance(response, str):
        return response

    if response is None or response.empty:
        return "No matching products found."

    final_answer = ""

    for i, row in response.iterrows():
        final_answer += f"""
{i+1}. {row['title']}

Price: Rs. {row['price']}
Discount: {int(row['discount'] * 100)}% off
Rating: {row['avg_rating']}
👉 [View Product]({row['product_link']})

"""

    return final_answer


# -------------------------------
# TEST
# -------------------------------
if __name__ == "__main__":
    question = "give nike shoe under 5000"
    answer = sql_chain(question)
    print(answer)
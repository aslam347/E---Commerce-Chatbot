# =========================
# app/sql.py
# FIXED FOR STREAMLIT CLOUD
# =========================

from groq import Groq
import os
import re
import sqlite3
import pandas as pd
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# -------------------------
# ENV
# -------------------------
GROQ_MODEL = os.getenv("GROQ_MODEL")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client_sql = Groq(api_key=GROQ_API_KEY)

# -------------------------
# DATABASE PATHS
# tries multiple paths for cloud + local
# -------------------------
possible_paths = [
    Path(__file__).resolve().parent / "db.sqlite",                    # app/db.sqlite
    Path(__file__).resolve().parent.parent / "resources" / "db.sqlite",  # resources/db.sqlite
    Path(__file__).resolve().parent.parent / "db.sqlite"             # root/db.sqlite
]

db_path = None

for path in possible_paths:
    if path.exists():
        db_path = path
        break

# -------------------------
# SQL PROMPT
# -------------------------
sql_prompt = """
You are expert in SQLite SQL generation.

Table name: product

Columns:
product_link
title
brand
price
discount
avg_rating
total_ratings

Rules:
1. Use SQLite syntax only
2. Use SELECT *
3. Use LOWER(column)
4. Use LIKE '%value%'
5. Use <= not ≤
6. Use LIMIT 5
7. Return ONLY SQL inside <SQL></SQL>

Example:

<SQL>
SELECT * FROM product
WHERE LOWER(title) LIKE '%shoe%'
AND price <= 2000
LIMIT 5;
</SQL>
"""


# -------------------------
# GENERATE SQL
# -------------------------
def generate_sql_query(question):
    chat_completion = client_sql.chat.completions.create(
        messages=[
            {"role": "system", "content": sql_prompt},
            {"role": "user", "content": question}
        ],
        model=GROQ_MODEL,
        temperature=0.2,
        max_tokens=1024
    )

    return chat_completion.choices[0].message.content


# -------------------------
# RUN QUERY
# -------------------------
def run_query(query):
    try:
        if db_path is None:
            return "Database file not found."

        if query.strip().upper().startswith("SELECT"):
            with sqlite3.connect(db_path) as conn:
                df = pd.read_sql_query(query, conn)
                return df.head(5)

    except Exception as e:
        return f"SQL Error: {str(e)}"


# -------------------------
# MAIN CHAIN
# -------------------------
def sql_chain(question):
    sql_query = generate_sql_query(question)

    pattern = r"<SQL>(.*?)</SQL>"
    matches = re.findall(pattern, sql_query, re.DOTALL)

    if not matches:
        return "Sorry, LLM could not generate SQL."

    query = matches[0].strip()

    response = run_query(query)

    # If SQL failed
    if isinstance(response, str):
        return response

    # Empty result
    if response is None or response.empty:
        return "No matching products found."

    # -------------------------
    # FORMAT OUTPUT
    # -------------------------
    final_answer = ""

    for i, row in response.iterrows():
        final_answer += f"""
{i+1}. {row['title']}

Price: Rs. {row['price']}
Discount: {int(float(row['discount']) * 100)}% off
Rating: {row['avg_rating']}
👉 [View Product]({row['product_link']})

"""

    return final_answer


# -------------------------
# TEST
# -------------------------
if __name__ == "__main__":
    question = "give shoe under 2000"
    answer = sql_chain(question)
    print(answer)
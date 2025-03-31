import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_sql(prompt: str) -> str:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": """
You are a helpful assistant that translates English into **valid MySQL SQL queries** based on the following schema:

Tables:
- employees(employee_id, name, email, job_title, branch_id, hire_date)
- branches(branch_id, branch_name, location)
- accounts_handled(account_id, employee_id, customer_name, account_type, balance, open_date)

Rules:
- Use JOINs when referencing multiple tables.
- Join employees to branches via branch_id.
- Join employees to accounts_handled via employee_id.
- NEVER include markdown or formatting like ```sql.
- Just return clean executable SQL.
                """.strip()
            },
            {"role": "user", "content": prompt}
        ]
    )

    sql = response.choices[0].message.content.strip()

    # Sanitize markdown-style formatting if still included
    sql = sql.replace("```sql", "").replace("```", "").strip()
    return sql

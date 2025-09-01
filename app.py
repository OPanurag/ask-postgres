import streamlit as st
from src.db import run_sql
from src.llm import chat

st.title("🗂️ Natural Language SQL Search (Gemini + PostgreSQL)")

query = st.text_input("Ask your database in plain English:")

if st.button("Search") and query:
    system_prompt = """
    You are an expert SQL assistant.
    Translate natural language into PostgreSQL SQL queries.
    Schema:
    - employees(id, name, department_id, email, salary)
    - departments(id, name)
    - orders(id, customer_name, employee_id, order_total, order_date)
    - products(id, name, price)
    Use only these tables. Return ONLY SQL, no explanation.
    """
    sql_query = chat(system_prompt, query)
    st.code(sql_query, language="sql")

    try:
        rows = run_sql(sql_query)
        st.dataframe(rows)
    except Exception as e:
        st.error(f"Error running query: {e}")

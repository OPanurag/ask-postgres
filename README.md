README.md
# Natural Language SQL Search (Gemini + PostgreSQL + Streamlit)

## 🚀 Setup
```
1. Clone the repo
2. Create virtual env & install deps
   ```pip install -r requirements.txt```
3. Start PostgreSQL with pgvector
```docker-compose up -d```
```


Start PostgreSQL with pgvector

```docker-compose up -d```


Initialize schema & data
```
psql -h localhost -U postgres -d nl2sql -f sql/01_schema.sql
psql -h localhost -U postgres -d nl2sql -f sql/02_sample_data.sql
```

Copy .env.example → .env and add your Gemini API key.

Run Streamlit app

```streamlit run app.py```

✨ Features
```Natural language → SQL queries```

Runs against PostgreSQL with pgvector

Streamlit UI


---

👉 Do you want me to generate this whole structure into a **ready-to-commit zip** so you can just unzip into your repo and push, or would you prefer to copy-paste the files one by one?

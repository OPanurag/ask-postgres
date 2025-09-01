# Natural Language SQL Search (Gemini + PostgreSQL + Streamlit)

## 📖 Project Description
This project enables users to convert natural language queries into SQL queries. It leverages the power of Gemini for natural language processing, PostgreSQL with pgvector for database operations, and Streamlit for an interactive user interface. The application is designed to simplify database interactions for non-technical users.

## 🚀 Features
- **Natural Language to SQL Conversion**: Translate plain English queries into SQL commands.
- **PostgreSQL with pgvector**: Utilize advanced vector search capabilities.
- **Interactive Streamlit UI**: User-friendly interface for query input and result visualization.
- **Preloaded Sample Data**: Includes departments, employees, products, and orders for demonstration purposes.

## 🛠️ Prerequisites
Ensure the following are installed on your system:
- Python 3.8 or higher
- Docker and Docker Compose
- PostgreSQL (optional, if not using Docker)

## ⚙️ Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/OPanurag/ask-postgres.git
   cd ask-postgres
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. Start PostgreSQL with pgvector:
   ```bash
   docker-compose up -d
   ```

## 🗄️ Database Setup
1. Initialize the database schema:
   ```bash
   psql -h localhost -U postgres -d nl2sql -f sql/01_schema.sql
   ```

2. Populate the database with sample data:
   ```bash
   psql -h localhost -U postgres -d nl2sql -f sql/02_sample_data.sql
   ```

## 🔑 Configuration
1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Add your Gemini API key to the `.env` file.

## ▶️ Usage
1. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

2. Open the application in your browser at `http://localhost:8501`.

## 🧪 Testing
Run the test scripts to ensure everything is working correctly:
```bash
python db_test.py
python gemini_test.py
```

## 📂 Project Structure
```
ask-postgres/
├── app.py               # Streamlit application
├── db_test.py           # Database test script
├── gemini_test.py       # Gemini API test script
├── docker-compose.yml   # Docker configuration
├── requirements.txt     # Python dependencies
├── sql/                 # SQL scripts
│   ├── 01_schema.sql    # Database schema
│   ├── 02_sample_data.sql # Sample data
├── src/                 # Source code
│   ├── db.py            # Database utility functions
│   ├── llm.py           # Language model integration
└── README.md            # Project documentation
```

## 🤝 Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## 📜 License
This project is licensed under the MIT License. See the `LICENSE` file for details.

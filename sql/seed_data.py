import sys
import os
from sqlalchemy import create_engine, text

# Optional: add project root to sys.path if importing local modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Update with your actual DB credentials
engine = create_engine("postgresql+psycopg2://anurag@localhost:5432/postgres", future=True)

def seed():
    with engine.begin() as conn:
        # --- Departments ---
        departments = ["Engineering", "HR", "Finance", "Sales", "Marketing"]
        dept_ids = {}

        for dept in departments:
            result = conn.execute(
                text(
                    """
                    INSERT INTO departments (name)
                    VALUES (:name)
                    ON CONFLICT (name) DO NOTHING
                    RETURNING id
                    """
                ),
                {"name": dept}
            )
            dept_id = result.scalar()
            if not dept_id:
                dept_id = conn.execute(
                    text("SELECT id FROM departments WHERE name=:name"),
                    {"name": dept}
                ).scalar()
            dept_ids[dept] = dept_id

        # --- Employees names ---
        employees = [
            ("Li Wei", "Engineering", 95000),
            ("Wang Fang", "HR", 60000),
            ("Zhang Yong", "Finance", 85000),
            ("Chen Mei", "Marketing", 90000),
            ("Liu Yang", "Sales", 78000),
            ("Zhao Qian", "Engineering", 102000),
            ("Sun Hao", "Finance", 87000),
            ("Xu Ling", "HR", 62000),
            ("Hu Jun", "Sales", 80000),
            ("Gao Ling", "Marketing", 95000),
            ("Deng Wei", "Engineering", 99000),
            ("Huang Fang", "HR", 61000),
            ("Qiu Ming", "Sales", 72000),
            ("Feng Yan", "Finance", 88000),
            ("Tang Rui", "Finance", 76000),
            ("Shen Li", "Marketing", 67000),
            ("Jin Tao", "Engineering", 105000),
            ("Yu Yan", "HR", 64000),
            ("Ma Lei", "Sales", 82000),
            ("He Qiang", "Engineering", 150000),
            ("Luo Ning", "Engineering", 110000),
            ("Wu Fang", "HR", 70000),
            ("Cao Hui", "Finance", 95000),
            ("Lin Xiu", "Sales", 98000),
            ("Zhou Ping", "Marketing", 65000),
            ("Dai Jing", "Marketing", 68000),
            ("Hao Chen", "Finance", 99000),
            ("Li Na", "HR", 72000),
            ("Chen Yang", "Sales", 90000),
            ("Yang Bo", "Engineering", 93000)
        ]

        for name, dept, salary in employees:
            if dept not in dept_ids:
                continue
            conn.execute(
                text("INSERT INTO employees (name, department_id, salary) VALUES (:n, :d, :s)"),
                {"n": name, "d": dept_ids[dept], "s": salary}
            )

        # --- Products ---
        products = [
            ("Acme Widget", 499.00),
            ("Pro Gadget", 1299.00),
            ("Eco Bottle", 299.00),
            ("Comfort Chair", 5999.00),
            ("Smart Lamp", 1999.00),
            ("Wireless Mouse", 199.00),
            ("Mechanical Keyboard", 349.00),
            ("Noise Cancelling Headphones", 899.00),
            ("Office Desk", 1200.00),
            ("Ergonomic Chair", 799.00),
            ("Coffee Maker", 150.00),
            ("Standing Desk Converter", 399.00),
            ("Smartphone", 999.00),
            ("Tablet", 699.00),
            ("Laptop", 1999.00),
            ("Monitor", 450.00),
            ("Router", 120.00),
            ("Smartwatch", 299.00),
            ("External HDD", 89.00),
            ("USB-C Hub", 49.00)
        ]

        for name, price in products:
            conn.execute(
                text("INSERT INTO products (name, price) VALUES (:n, :p)"),
                {"n": name, "p": price}
            )

        # --- Orders with Chinese-style customer names ---
        orders = [
            ("Li Ming", "Zhang Yong", 1499.00, "2025-07-01"),
            ("Wang Lei", "Zhang Yong", 5999.00, "2025-07-10"),
            ("Chen Yu", "Li Wei", 1999.00, "2025-08-02"),
            ("Zhao Fang", "Sun Hao", 299.00, "2025-08-11"),
            ("Xu Lei", "Zhang Yong", 499.00, "2025-08-15"),
            ("Liu Fang", "Zhao Qian", 1599.00, "2025-08-20"),
            ("Gao Wei", "Deng Wei", 2499.00, "2025-08-22"),
            ("He Ling", "He Qiang", 3999.00, "2025-08-25"),
            ("Ma Jun", "Jin Tao", 1200.00, "2025-08-28"),
            ("Lin Qian", "Li Wei", 799.00, "2025-08-30"),
            ("Feng Ning", "Chen Mei", 899.00, "2025-09-01"),
            ("Yang Tao", "He Qiang", 1299.00, "2025-09-02"),
            ("Huang Bo", "Zhao Qian", 1099.00, "2025-09-03"),
            ("Shen Mei", "Jin Tao", 1599.00, "2025-09-04"),
            ("Zhou Li", "He Qiang", 1499.00, "2025-09-05")
        ]

        for cust_name, emp_name, total, date in orders:
            conn.execute(
                text(
                    "INSERT INTO orders (customer_name, employee_id, order_total, order_date) "
                    "VALUES (:c, (SELECT id FROM employees WHERE name=:e LIMIT 1), :t, :d)"
                ),
                {"c": cust_name, "e": emp_name, "t": total, "d": date}
            )

    print("✅ Database seeded successfully!")

if __name__ == "__main__":
    seed()

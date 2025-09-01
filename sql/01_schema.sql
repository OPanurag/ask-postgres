CREATE EXTENSION IF NOT EXISTS vector;

CREATE TABLE departments (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE employees (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  department_id INT REFERENCES departments(id) ON DELETE SET NULL,
  email VARCHAR(255) UNIQUE,
  salary DECIMAL(10,2) CHECK (salary >= 0)
);

CREATE TABLE products (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  price DECIMAL(10,2) CHECK (price >= 0),
  name_embedding vector(1536)
);

CREATE TABLE orders (
  id SERIAL PRIMARY KEY,
  customer_name VARCHAR(100) NOT NULL,
  employee_id INT REFERENCES employees(id) ON DELETE SET NULL,
  order_total DECIMAL(10,2) CHECK (order_total >= 0),
  order_date DATE NOT NULL,
  customer_name_embedding vector(1536)
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_emp_dept ON employees(department_id);
CREATE INDEX IF NOT EXISTS idx_orders_employee ON orders(employee_id);
CREATE INDEX IF NOT EXISTS idx_products_name ON products(name);
CREATE INDEX IF NOT EXISTS idx_orders_date ON orders(order_date);

-- Vector indexes
CREATE INDEX IF NOT EXISTS idx_products_name_vec ON products USING ivfflat (name_embedding vector_cosine_ops);
CREATE INDEX IF NOT EXISTS idx_orders_cust_vec ON orders   USING ivfflat (customer_name_embedding vector_cosine_ops);

INSERT INTO departments (name) VALUES
  ('HR'), ('Engineering'), ('Sales'), ('Finance')
ON CONFLICT (name) DO NOTHING;

INSERT INTO employees (name, department_id, email, salary) VALUES
  ('Aarav Sharma', (SELECT id FROM departments WHERE name='Engineering'), 'aarav@vocso.com', 180000.00),
  ('Isha Kapoor', (SELECT id FROM departments WHERE name='HR'), 'isha@vocso.com', 120000.00),
  ('Rohan Gupta', (SELECT id FROM departments WHERE name='Sales'), 'rohan@vocso.com', 150000.00),
  ('Priya Nair', (SELECT id FROM departments WHERE name='Finance'), 'priya@vocso.com', 160000.00),
  ('Neeraj Verma', (SELECT id FROM departments WHERE name='Engineering'), 'neeraj@vocso.com', 200000.00)
ON CONFLICT DO NOTHING;

INSERT INTO products (name, price) VALUES
  ('Acme Widget', 499.00),
  ('Pro Gadget', 1299.00),
  ('Eco Bottle', 299.00),
  ('Comfort Chair', 5999.00),
  ('Smart Lamp', 1999.00)
ON CONFLICT DO NOTHING;

INSERT INTO orders (customer_name, employee_id, order_total, order_date) VALUES
  ('Ananya Singh', (SELECT id FROM employees WHERE name='Rohan Gupta'), 1499.00, '2025-07-01'),
  ('Vikram Joshi', (SELECT id FROM employees WHERE name='Rohan Gupta'), 5999.00, '2025-07-10'),
  ('Neha Mehta',   (SELECT id FROM employees WHERE name='Aarav Sharma'), 1999.00, '2025-08-02'),
  ('Rahul Khanna', (SELECT id FROM employees WHERE name='Neeraj Verma'), 299.00,  '2025-08-11'),
  ('Deepika Rao',  (SELECT id FROM employees WHERE name='Rohan Gupta'), 499.00,  '2025-08-15')
ON CONFLICT DO NOTHING;

from flask import Flask, render_template, request, json
import sqlite3
import csv

app = Flask(__name__)

def read_json():
    """Reads and returns data from products.json"""
    try:
        with open("products.json", "r") as file:
            return json.load(file)
    except Exception as e:
        print("Error reading JSON file:", e)
        return []

def read_csv():
    """Reads and returns data from products.csv"""
    try:
        products = []
        with open("products.csv", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                products.append({
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                })
        return products
    except Exception as e:
        print("Error reading CSV file:", e)
        return []

def read_sql():
    """Reads and returns data from SQLite database"""
    try:
        conn = sqlite3.connect("products.db")  # Connect to SQLite database
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        conn.close()

        # Convert rows into dictionary format
        return [{"id": row[0], "name": row[1], "category": row[2], "price": row[3]} for row in rows]
    except Exception as e:
        print("Error reading SQLite database:", e)
        return []

@app.route('/products')
def products():
    source = request.args.get("source", "").lower()
    product_id = request.args.get("id")

    # Load data based on source
    if source == "json":
        data = read_json()
    elif source == "csv":
        data = read_csv()
    elif source == "sql":
        data = read_sql()
    else:
        return render_template("product_display.html", error="Wrong source. Use 'json', 'csv', or 'sql'.")

    # If id is provided, filter by id
    if product_id:
        try:
            product_id = int(product_id)
            data = [product for product in data if product["id"] == product_id]
            if not data:
                return render_template("product_display.html", error="Product not found.")
        except ValueError:
            return render_template("product_display.html", error="Invalid product ID.")

    return render_template("product_display.html", products=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

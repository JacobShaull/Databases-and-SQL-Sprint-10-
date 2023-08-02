import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()


def execute_query(curs, query):
    curs.execute(query)
    conn.commit()
    return curs.fetchall()


# northwind database
expensive_items = '''
SELECT * from Product
ORDER BY UnitPrice DESC
LIMIT 10;
'''
# avg age when hired
avg_hire_age = '''
SELECT AVG(HireDate - BirthDate)
FROM Employee
'''

ten_most_expensive = '''
SELECT Product.ProductName, Product.UnitPrice, Supplier.CompanyName
FROM Product
INNER JOIN Supplier on Product.SupplierId = Supplier.Id
ORDER BY UnitPrice DESC
LIMIT 10;
'''

largest_category = '''
SELECT Category.CategoryName, COUNT(DISTINCT Product.ProductName)
FROM Product
INNER JOIN Category on Product.CategoryId = Category.Id
GROUP BY Product.CategoryId
ORDER BY COUNT(DISTINCT Product.ProductName) DESC
LIMIT 1;
'''

queries = (expensive_items, avg_hire_age, ten_most_expensive, largest_category)

if __name__ == "__main__":
    print(execute_query(curs, queries))

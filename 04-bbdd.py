# import pymysql as sq
import pandas as pd
import matplotlib as plt

# conexion = sq.Connect("Northwin.db")
query = """
    SELECT ProductName, SUM(p.UnitPrice * Quantity) as Rentabilidad
    FROM [Order Details] od
    JOIN Products p ON p.ProductID = od.ProductID
    GROUP BY p.ProductName
    ORDER BY Rentabilidad DESC
"""

# products = pd.read_sql_query(query, conexion)
# products.plot(x="ProductName", y="Rentabilidad")

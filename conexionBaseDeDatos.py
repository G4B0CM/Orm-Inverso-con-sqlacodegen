
import pyodbc

usuario = "SUPERADMIN"
contraseña = "UDLA"
servidor = "UPOAULA10603"
base_datos = "AdventureWorks2008R2"

conexion_str = (
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={servidor};"
    f"DATABASE={base_datos};"
    f"UID={usuario};"
    f"PWD={contraseña};"
    "TrustServerCertificate=yes;"
)


conn = pyodbc.connect(conexion_str)
cursor = conn.cursor()

query = "SELECT * FROM Person.BusinessEntity" 

cursor.execute(query)

resultados = cursor.fetchall()

for row in resultados:
    print(row)

cursor.close()
conn.close()
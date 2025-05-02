from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker

# Parámetros de conexión
usuario = "SUPERADMIN"
contraseña = "UDLA"
servidor = "UPOAULA10603"  # o IP
base_datos = "AdventureWorks2008R2"

# Construir la cadena de conexión con trustServerCertificate habilitado
conexion_str = (
    f"mssql+pyodbc://{usuario}:{contraseña}@{servidor}/{base_datos}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&TrustServerCertificate=yes"
)

# Crear motor SQLAlchemy
engine = create_engine(conexion_str)

# Reflejar metadatos de la base
metadata = MetaData()
metadata.reflect(bind=engine)

# Crear clases ORM automáticamente
Base = automap_base(metadata=metadata)
Base.prepare()

# Crear sesión
Session = sessionmaker(bind=engine)
session = Session()

# ✅ Ejemplo: listar nombres de clases reflejadas
print("Tablas reflejadas:")
for class_name in Base.classes.keys():
    print(f" - {class_name}")

# ✅ Ejemplo: usar una tabla reflejada (reemplaza con nombre real)
# MiTabla = Base.classes.mi_tabla
# resultados = session.query(MiTabla).all()
# for fila in resultados:
#     print(fila)

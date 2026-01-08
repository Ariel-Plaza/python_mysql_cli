import os
from contextlib import contextmanager
# import mysql.connector
from dotenv import load_dotenv
from sqlalchemy import engine, create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy.exc import OperationalError, DBAPIError

# Lectura de variables
load_dotenv()
HOST = os.getenv("DB_HOST")
PORT = os.getenv("DB_PORT")
USER = os.getenv("DB_USER")
PASS = os.getenv("DB_PASSWORD")
DATABASE = os.getenv("DB_NAME")

# Conexion al servidor

# url generada para utilizar con SQLAlchemy
DATABASE_URL = (
    f"mysql+mysqlconnector://{USER}:{PASS}"
    f"@{HOST}:{PORT}/{DATABASE}"
    )

# Creacion instancia de motor SQLAlchemy integrando url y parametros de control
engine = Engine = create_engine(
    DATABASE_URL,
    # tiempo maximo(se) de conexion en el pool
    pool_recycle=3600,
    # numero de conexiones
    pool_size=5,
    # muestra los logs de SQL 
    echo=False,
)

# print(f"Engine{DATABASE}@{HOST}")

# Creación sesion de conexion

Session = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
    )

# Generador de sesiones para conexion

# define una funcion con administradores de contexto
@contextmanager
def generador_sesion():
    db = Session()
    try:
        # el codigo antes de yield actua como metodo enter
        # se le asigna a yield el valor de la variable as de with
        yield db
        # si esta correcto se envia a la bd
        db.commit()
        # actua como metodo salida
    # captura errores con la base de datos
    except OperationalError as err:
        db.rollback()
        # Verificar el error de conexión
        # si tiene el atributo y tiene el codigo
        if hasattr(err.orig, 'errno') and err.orig.errno == 2003:
            print("\n*** Error de conexion al servidor MySQL ***")
            print("- Verifica que MySQL esté corriendo")
            print("- Verifica host y puerto archivo .env")
            print(f"- Host actual: {HOST}:{PORT}")
        else:
            print(f"Error operativo de la base de datos: {err}")
            
    except DBAPIError as err:
        # Verifico error de conexion con codigo
        if hasattr(err.orig, 'errno') and err.orig.errno == 2003:
            print("\n*** Error de conexion al servidor MySQL ***")
            print("- Verifica que MySQL esté corriendo")
            print("- Verifica el host y puerto")
        elif hasattr(err.orig, 'errno') and err.orig.errno == 2005:
            print("\n*** Error de conexion al servidor MySQL ***")
            print("- Verifica que MySQL esté corriendo")
            print("- Verifica host y puerto en archivo .env")
            print(f"- Host actual: {HOST}:{PORT}")
        else:
            print(f"Error de DB-API: {err}")
        
    except Exception as err:
        print(f"Error inesperado con la base de datos{err}")  
        raise
    finally:
        # se cierra la conexión
        db.close()



# Test de conexion a la base de datos.

# def test_connection() -> bool:
#     """Verifica que la conexión a la base de datos funcione"""
#     try:
#         from sqlalchemy import text
#         with engine.connect() as conn:
#             result = conn.execute(text("SELECT 1 AS test"))
#             print(f"✅ Conexión realizada: {result.fetchone()}")
#             return True
#     except Exception as e:
#         print(f"❌ Error de conexión: {e}")
#         return False

# test_connection()

# Clase base para los modelos
class Base(DeclarativeBase):
    pass

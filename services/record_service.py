from db.connection import generador_sesion
from db.models import Records

# Crear nuevo registro
def agregar_registro(args_name, args_valor):
    try:
        # inicia la conexion con la db y la mantiene abierta
        with generador_sesion() as db:
            # Crear registro
            nuevo = Records(
            name=args_name,
            value=args_valor
            )
            # agregar registro
            db.add(nuevo)
            # envia los cambios a la db pero no los guarda
            db.flush()
            return nuevo.id
    except Exception as e:
        print(f"\nError al agregar registro: {e}")
        return None
# Listar todos los registros
def leer_registros():
    try:
        with generador_sesion() as db:
            registros = db.query(Records).all()
            # conversion de objetos en diccionarios
            return [
                {
                    'id': r.id,
                    'name': r.name,
                    'value': r.value,
                    'created_at': r.created_at,
                }
                # loop que recupera la info de registros
                for r in registros
            ]
    except Exception as e:
        print(f"\nError al recuperar los  registros: {e}")
        return None
# Consultar registro por ID
def buscar_registro_id(id_buscado):
    try:
        with generador_sesion() as db:
            registro = db.query(Records).filter(Records.id == id_buscado).first()

            if not registro:
                return None
            return {
                        'id': registro.id,
                        'name': registro.name,
                        'value': registro.value,
                        'created_at': registro.created_at,
                    }
        
    except Exception as e:
        print(f"\nError al buscar el registro:{e}")
        return None

# Modificar un registro existente
def actualizar_registro(args_id, args_value):
    try:
        with generador_sesion() as db:
            registro = db.query(Records).filter(Records.id == args_id).first()
            if not registro:
                return False
            registro.value = args_value
            db.flush()
            return True
    except Exception as e:
        print(f"\nError al buscar el registro:{e}")
        return None


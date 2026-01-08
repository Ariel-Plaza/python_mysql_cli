from sqlalchemy import String,Integer, DateTime, text
from sqlalchemy.orm import mapped_column, validates
from db.connection import Base

# Instancia de modelos Base, con nombre de la tabla, campos y tipo de datos que maneja
class Records(Base):
    __tablename__ = "records"
    id = mapped_column(Integer,primary_key=True)
    name = mapped_column(String(100), nullable= False)
    value = mapped_column(Integer, nullable= False)
    created_at = mapped_column(DateTime, server_default=text('CURRENT_TIMESTAMP'))
    # decorador de sqlalchemy
    @validates('name')
    def validar_name(self,key,name):
        # verifica si el nombre es None o si tiene espacios los elimina y evita que se agreguen espacion
        if not name or not name.strip():
            # lanza excepcion y manda el error
            raise ValueError("El nombre no puede estar vacio")
        if len(name) > 100:
            raise ValueError("El nombre no puede tener mas de 100 caracteres")
        return name.strip()

    @validates('value')
    def validar_valor(self, key, value):
        # valida si valor existe
        if value is None:
            raise ValueError("El valor es obligatorio")  
        return value
        # Valida que el valor no sea negativo (Valores inválidos)
        if value is not None and value < 0:
            raise ValueError("El valor debe ser una cifra positiva (>= 0)")
        
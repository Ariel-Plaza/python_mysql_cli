import argparse
from services.record_service import agregar_registro, leer_registros,buscar_registro_id,actualizar_registro

# validacion que argumentos sean aceptado
def validar_argumentos(argumento, nombre_argumento, ayuda, min_valor=None):
    # valida que argumento no este vacio
    if argumento is None:
        print(f"Error: {nombre_argumento} es requerido")
        print(f"Ejemplo: {ayuda}")
        return False
    # valida contenido del argumento
    if isinstance(argumento, str):
            #el argumento no este vacio
        if not argumento.strip():
            print(f"Error: {nombre_argumento} no puede estar vacio")
            return False
    if isinstance(argumento, int) and min_valor is not None:
        if argumento < min_valor:
            print(f"Error: El valor de '{nombre_argumento}' debe ser mayor o igual a {min_valor}.")
            return False
            
    return True


def main():
    try:
        parser = argparse.ArgumentParser()

        subparsers = parser.add_subparsers(dest='operacion', required=True, help="debes seleccionar uno de los siguientes comandos: add list get update")

        # Crear nuevo registro
        parser_add = subparsers.add_parser('add', help='Agrega un nuevo registro')
        parser_add.add_argument('--name', type=str , help='nombre')
        parser_add.add_argument('--value', type=int, help='valor')

        # Listar todos los registros
        parser_list = subparsers.add_parser('list', help='Muestra todos los registros')

        # Consultar registro por ID
        parser_get = subparsers.add_parser('get', help='Agrega un nuevo registro')
        parser_get.add_argument('--id', type=int , help='ID del registro')

        # Modificar un registro existente
        parser_update = subparsers.add_parser('update', help='Actualiza un nuevo registro')
        parser_update.add_argument('--id', type=int , help='ID del registro')
        parser_update.add_argument('--value', type=int, help='valor')

        args = parser.parse_args()


        # Crear nuevo registro
        if args.operacion == 'add':
            # validaciones
            if not validar_argumentos(args.name, '--name', 'python3 main.py add --name "Sensor" --value 45'):
                return
            if not validar_argumentos(args.value, '--value', 'python main.py add --name "Sensor A" --value 45'):
                return
            if not validar_argumentos(args.value, '--value', 'python main.py add --name "Sensor A" --value 45', min_valor=0 ):
                return
            nuevo_id = agregar_registro(args.name, args.value)
            if nuevo_id:    
                print(f"Registro insertado correctamente.ID:{nuevo_id}")
            else:
                print("No se pudo insertar el registro")
            
            # Listar todos los registros
        elif args.operacion == 'list':  
            registros = leer_registros()
            if not registros:
                print("No existen registros para listar")
            else:
                if registros:
                    print("ID |Name     |Value |Created At")
                for record in registros:
                    fecha = record['created_at'].strftime('%Y-%m-%d %H:%M')
                    print(f"{record['id']} | {record['name']} | {record['value']} | {fecha}")      

        # Consultar registro por ID
        elif args.operacion == 'get':
            if not validar_argumentos(args.id, '--id', 'python3 main.py get --id 1'):
                return
            id_buscado = buscar_registro_id(args.id)
            if not id_buscado:
                print(f"No existe registro con el id: {args.id}")
                print("Ingresa un id valido")
            else:
                fecha = id_buscado['created_at'].strftime('%Y-%m-%d %H:%M')
                print("ID |Name     |Value |Created At")
                print(f"{id_buscado['id']} | {id_buscado['name']} | {id_buscado['value']} | {fecha}")

        # Modificar un registro existente
        elif args.operacion == 'update':
            if not validar_argumentos(args.id, '--id', 'python3 main.py update --id 1 --value 100'):
                return
            if not validar_argumentos(args.value, '--value', 'python3 main.py update --id 1 --value 100'):
                return
            actualizar_value = actualizar_registro(args.id, args.value)
            if not actualizar_value:
                print(f"No existe registro con el id: {args.id}")
                print("Ingresa un id valido")
            else:
                print("Registro actualizado correctamente")
    except Exception as e:
        print(f"Error inesperado: {e}")
if __name__ == "__main__":
    main()
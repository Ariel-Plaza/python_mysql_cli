## Estructura del proyecto

python_mysql_cli/
├── db/
│   ├── connection.py       # Conexión a MySQL
│   └── models.py           # Modelos y operaciones con la Base de Datos
├── env/                    # Entorno virtual
├── services/
│   └── record_service.py   # Lógica de negocio
├── main.py                 # Punto de entrada de la aplicación
├── requirements.txt        # Dependencias del proyecto
└── README.md               # Documentación
## Entorno

En la terminal se deben ejecutar los siguientes comandos

### Notas para Windows

- En Windows, utiliza `python` en lugar de `python3`.
- Ejemplo para activar el entorno virtual:

```bash
env\Scripts\activate
```

Si PowerShell bloquea la activacion, ejecutar previamente:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```


### Creación

Para la creación de entorno por primera vez

```bash
python3 -m venv env
```

### Uso

Cada vez que necesite utilizar el proyecto debe activar entorno

```bash
source env/bin/activate
```

### Desactivación

Desactivar entorno una vez finalizado el trabajo.

```bash
deactivate
```

## Instalación de dependencias

En la terminal debe ejecutar el siguiente comando

```bash
pip3 install -r requirements.txt
```

## Configuración de la base de datos

### Prerrequisitos

- MySQL Server instalado (versión 5.7 o superior)
- Acceso con permisos para crear bases de datos y tablas

### Pasos de configuración

1. Acceder a MySQL

```bash
mysql -u root -p
```

- debes ingresa contraseña cuando se requiera.

2.  Creación de base de datos

```sql
CREATE DATABASE records_db
```

3. Ingresar a la base de datos

```sql
USE records_db
```

4. Creación de tabla

```sql
CREATE TABLE records (
id INT AUTO_INCREMENT PRIMARY KEY,
name VARCHAR(100) NOT NULL,
value INT NOT NULL,
created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

5. Verificar si tabla fue creada

```sql
  DESCRIBE records
```

respuesta esperada

+------------+--------------+------+-----+-------------------+
| Field | Type | Null | Key | Default |
+------------+--------------+------+-----+-------------------+
| id | int | NO | PRI | NULL |
| name | varchar(100) | NO | | NULL |
| value | int | NO | | NULL |
| created_at | datetime | YES | | CURRENT_TIMESTAMP |
+------------+--------------+------+-----+-------------------+

6. Salir

```bash
EXIT
```

## Configurar credenciales

Las credenciales de conexión por seguridad se manejan con variables de entorno

1. Crear archivo .env en la raíz del proyecto

```bash
touch .env
```

2. Configurar variables de entorno con tus credenciales MySQL

```bash
DB_HOST=localhost           # Host de MySQL
DB_PORT=3306                # Puerto de MySQl
DB_USER=tu_usuario          # Usuario MySQL
DB_PASSWORD=tu_contraseña   # Contraseña del usuario
DB_NAME=nombre_base_datos   # Nombre de la base de datos
```

## Guia de Uso(comandos)

Esta aplicación utiliza una interfaz de linea de comandos(CLI) con subcomandos específicos.
Cada comando cuenta con validaciones de seguridad para garantizar integridad de los datos.

1. Agregar un registro (`add`)
   Creación de un nuevo registro en la base de datos.

- **Validación:** Nombre es obligatorio (máx. 100 caracteres) y el valor debe ser un entero mayor o igual a cero.

```bash
python3 main.py add --name "Sensor" --value 85
```

Resultado esperado

```bash
Registro insertado correctamente.ID:1
```

2. Listar registros(`list`)
   Lista todos los registros almacenados en una tabla organizada.

- **Validación:** Maneja estados de lista vacía

```bash
python3 main.py list
```

Resultado esperado

```bash
ID |Name     |Value |Created At
1 | Sensor | 85 | 2025-12-18 00:25
2 | SensorB | 90 | 2025-12-18 00:40
```

3. Consultar por ID(`get`)
   Obtiene los detalles de un registro único mediante el ID

- **Validación:** Informa si el ID no existe en la base de datos.

```bash
python3 main.py get --id 1
```

Resultado esperado

```bash
ID |Name     |Value |Created At
1 | Sensor | 85 | 2025-12-18 00:25
```

4. Actualizar un registro(`update`)
   Modifica el valor de un registro existente

- **Validación:** Verifica que el ID exista y válida que el nuevo valor cumpla las reglas del negocio.

```bash
python3 main.py update --id 1 --value 120
```

Resultado esperado

```bash
Registro actualizado correctamente
```


# python_mysql_cli

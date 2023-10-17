import couchdb
import json

# Conectar a CouchDB
# en vez de marie:marie se debe poner el 'nombre de usuario':'contraseña'@'host':'puerto'
server = couchdb.Server('http://marie:marie@localhost:5984/') 


# Nombre de la base de datos en CouchDB
# en vez de 'base_tarea' se debe poner 'nombre que se asignó a la base'
database_name = 'base_tarea'
database = server[database_name]

# Abrir el archivo JSON y cargar los datos
# se debe poner ruta de acceso de donde se encuentra el archivo de datos
with open('C:/Users/Sofia/OneDrive/Escritorio/datos.json', 'r') as archivo_json:
    datos = json.load(archivo_json)

# Insertar los datos en la base de datos
for documento in datos:
    new_doc = database.save(documento)


print(f'Se han insertado {len(datos)} documentos en la base de datos.')
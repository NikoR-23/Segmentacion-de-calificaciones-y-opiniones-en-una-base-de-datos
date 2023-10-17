# Sistema de recomendaciones
## Instalación de CouchDB
+ Descargar CouchDB en https://couchdb.apache.org/ (se escoge un nombre de usuario y contraseña en la instalación que es importante recordar)
   
## Carga de los datos
+ En primer lugar se debe descargar base en formato de archivo json (compatible con el software). Se encuentra en repositorio llamada como “datos”
+ Se ingresa con usuario y contraseña a CouchDB y en el servidor, se crea una base de datos. Se ingresa al apartado “Databases” y en la parte superior
  derecha sale “Create Database”, al crear la base de datos se debe desprende información por llenar de la base como nombre (base_tarea es como se la llamrá)
  y se selecciona ”Non-partitioned - recommended for most workloads” y se finaliza la creación en “Create”

![](https://user-images.githubusercontent.com/147458630/275690075-8f341891-13d6-4c27-943c-5cafa3684e18.png)

## Cargar datos a base de datos creada
+ Ahora, por medio de Visual Studio Code y el lenguaje de programación Python, se creó un código que insertará los datos a CouchDB específicamente
  a la base creada anteriormente. El código se encuentra en repositorio y es el archivo llamado “insertar” en formato Python. Se debe ejecutar el
  código para que los datos aparezcan en la base. Va debidamente comentado para lograr su ejecución.

```
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

```

## Realizar consultas
+ Seguidamente, en el apartado “Design Documents” se selecciona “Mango Indexes” y seguidamente se le da clic a “edit query”. Ahí se desprende un
  cuadro de “Mango Query” en donde se deben ir realizando las consultas de seleccionar y filtrar.  Se encuentran en el archivo de texto llamado
  “Mango” y se debe ingresar una por una en el espacio del mango query para que brinde las filas con la información deseada.

  ![](https://user-images.githubusercontent.com/147458630/275691727-9865ad5b-888f-4832-963a-6a6c8904a598.png)

  
### Para seleccionar donde Reviewer_Location sea "Australia"
```

{
   "selector": {
      "Reviewer_Location": "Australia"
   }
}  

 ```


### Selccionar donde el rating sea 4 y 5
 ```

{
   "selector": {
      "Rating": {
         "$in": [
            "4",
            "5"
         ]
      }
   }
}

```


### Seleccionar cuando sea el DisneyLand de California y tenga rating 3 y 4
```

{
   "selector": {
      "Branch": "Disneyland_California",
      "Rating": {
         "$in": [
            "3",
            "4"
         ]
      }
   }
} 

```


### Seleccionar cuando el Reviewer_Location sea "Australia" y el rating sea 2 y 3
```

{
   "selector": {
      "Reviewer_Location": "Australia",
      "Rating": {
         "$in": [
            "2",
            "3"
         ]
      }
   }
}

```


### Buscar reviews que incluyan la palabra "Great" (ya sea en mayúscula o minúscula)
```

{
   "selector": {
      "Review_Text": {
         "$regex": "(G|g)reat"
      }
   }
}


```

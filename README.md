# Sistema de recomendaciones
Es importante calcar que en las siguientes instrucciones a seguir, se referirá a descargas de softwares para el sistema operativo de Windows.

## Instalación de CouchDB
+ Descargar CouchDB versión 3.3.2 en [https://couchdb.apache.org/](https://neighbourhood.ie/download-apache-couchdb-win/) (se escoge un nombre de usuario y contraseña en la instalación que es importante recordar).
   
## Carga de los datos
+ En primer lugar se debe descargar base en formato de archivo json (compatible con el software). Se encuentra en repositorio llamada como “datos”.
  
+ En segundo lugar, se ingresa con usuario y contraseña a CouchDB y en el servidor, se crea una base de datos. Se ingresa al apartado “Databases” y en la parte superior
  derecha sale “Create Database”, al crear la base de datos se debe desprende información por llenar de la base como nombre (base_tarea es como se la llamrá)
  y se selecciona ”Non-partitioned - recommended for most workloads” y se finaliza la creación en “Create”.

![](https://user-images.githubusercontent.com/147458630/275690075-8f341891-13d6-4c27-943c-5cafa3684e18.png)

## Cargar datos a base de datos creada
+ Para la inserción de datos, se necesita del software Visual Studio Code y python. 
+ Para instalar Python (https://www.python.org/downloads/) y Visual Studio para Windows (https://code.visualstudio.com/), primero debes descargar el instalador de Python desde el sitio web oficial. Una vez que hayas descargado el instalador, ejecútalo y sigue las instrucciones en pantalla. El instalador te permitirá elegir la        versión de Python que deseas instalar, así como la ubicación en la que deseas instalarla. Una vez que Python esté instalado, debes descargar e instalar la extensión de Python para Visual Studio desde el Marketplace. La extensión de Python te permitirá escribir,   ejecutar y depurar código Python en Visual Studio. Para descargar la extensión, abre Visual Studio y ve a la pestaña Comunidad. Luego, haz clic en el botón Obtener extensiones y busca la extensión Python. Una vez que hayas encontrado la extensión, haz clic en     el botón Instalar. Una vez que la extensión de Python esté instalada, ya podrás comenzar a programar en Python en Visual Studio. 
+ Ahora, por medio de Visual Studio Code y el lenguaje de programación Python, se creó un código que insertará los datos a CouchDB específicamente
  a la base creada anteriormente. El código se encuentra abajo de esta instrucción o en el archivo llamado “insertar” en formato Python que se encuentra en el repositorio. Se debe ejecutar el código para que los datos aparezcan en la base. Va debidamente comentado para lograr su ejecución.

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
+ Seguidamente, en el apartado “Design Documents” se selecciona “Run A Query with Mango”. Ahí se desprende un
  cuadro de “Mango Query” en donde se deben ir realizando las consultas de seleccionar y filtrar.  Se encuentran debajo de esta instrucción o en el archivo de texto llamado
  “Mango” que se encuentra en el repositorio. Se debe ingresar una por una en el espacio del mango query para que brinde las filas con la información deseada.


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
## Instalación de RavenDB
+ Descargar RavenDB versión 6.0.0 en https://ravendb.net/download (se escoge el sistema operativo)
  
+ Extraer el archivo zip en la carpeta de descarga.
  
+ Ejecutar con Power Shell el archivo que llamado "run"
  
+ Se abrirá de manera automática el navegador y se desplegará la aceptación de licencia.
  
+ Al aceptar la licencia, y para utilizarlo de manera gratuita se selecciona el modo Noseguro(Unsecured).
  

## Carga de los datos
+ En primer lugar, se debe descargar base en formato de archivo csv (compatible con el software).
  
+ Se ingresa al apartado “Bases” en la lista de íconos a la izquierda.
  
+ Se presiona el botón "Nueva base de datos" y se le otorga un nombre a esta.
  
+ Como se quiere cargar una base de datos, ahora en el ícono de tareas se selecciona "importar datos".
  
+ Se podrán observar los formatos de archivo soportados (ravendbdump, CSV, SQL, NoSQL).
  
+ En segundo lugar, se selecciona en este caso, archivo CSV, se importa el archivo y se escribe el nombre de la colección a la que se quiere descargar. Cuando ya se encuentre procesado, todos los datos se podrán observar en la colección seleccionada.
  
+ Si la base de datos contiene valores "missing", Ravendb los colocará de primer lugar en la base.

  
 ![](https://user-images.githubusercontent.com/144878444/275912706-e25c0f5f-cf15-43b2-9532-5a98c4513a62.png)
 

 ![](https://user-images.githubusercontent.com/144878444/275913650-d92e2a21-7cd6-4d64-b3d1-c473041102df.png)


## Consultas

+ Seguidamente, en el apartado “Consulta”, igualmente en la colección deseada, se desplega un "Query", donde se ingresa el script dependiendo de lo que se desee extraer de la base de datos. Abajo del Query se observarán los resultados, y el tiempo en el que realizó la consulta.

  
  ![](https://user-images.githubusercontent.com/144878444/275914148-427f4a93-5dc9-4e85-97df-e235592433c2.png)

 ### Para seleccionar donde Reviewer_Location sea "Australia"
 ```
    from Disneycsv 
    where Reviewer_Location = "Australia"
```


 ### Selccionar donde el rating sea 4 y 5
 ```
    from Disneycsv 
    where Rating in (4 , 5)
```
    

 ### Seleccionar cuando sea el DisneyLand de California y tenga rating 3 y 4
 ```
  from Disneycsv 
   where Branch = "Disneyland_California" and Rating in (3 , 4)
```

### Para observar los datos según Rating
```
   from Disneycsv
   group by Rating
   select key as Rating, count() as Count
```
### Buscar reviews que incluyan la palabra "Great" (ya sea en mayúscula o minúscula)

```
from "Disneycsv" 
where regex(Review_Text, "Great")

```

# pruebaPythonFramework

Flask

Instalacion de virtualenv para python3
 sudo apt-get install python3-venv

Clonar el ropositorio

Creacion de virtualenv
virtualenv venv

Activacion de virtualenv

. venv/bin/activate

Instalcion de flask

pip install Flask


Inicializacion de base de datos
  
  flask init-db

El comando se crea a traves del decorador @click.command('init-db') en el archivo db.py. El esquema esta en schema.sql


Ejecutar
 export FLASK_APP=olimpiadas
 export FLASK_ENV=developmen
 
 flask run


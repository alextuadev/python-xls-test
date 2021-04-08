# python-xls-test

Carga de excel en un par de modelos usando el admin de django


## Instalación 
``` git clone https://github.com/alextuadev/python-xls-test```

Instalar los requerimientos

``` pip install -r requirements.txt ```

Copiar ```local_settings_example.py``` en un nuevo archivo ```local_settings.py``` y configurar las credenciales de conexion a la base de datos.

```
 DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'database',
        'USER': 'userdatabase',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
Crear las migraciones

``` python manage.py makemigrations ```

Migrar la base de datos

``` python manage.py migrate ```

Crear un super usuario para acceder al admin

``` python manage.py createsuperuser ```

Levantamos el servidor de desarrollo
``` python manage.py runserver ```

El archivo de pruebas está en el home del proyecto.


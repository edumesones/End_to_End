 
  # creacion repositorio github
 
1. creacion de entorno en carpeta de vscode
    py -m venv nombre_entorno
    nombre_entorno/Scripts/activate
2. creacion repositorio
  git init <br>
  Ir a tu git crear una carpeta y seguir intrucciones para conectarlo <br>
   ### sentencias necesarias, NO OLVIDES GUARDAR CUANDO HAGAS CAMBIOS EN LOS SCRIPTS
  git add README.md  <br>
  git add . <br>
  git commit -m "first commit" <br>
  git branch -M main <br>
  git remote add origin tunuevorepo <br>
  git push -u origin main <br>
  Creamos .gitignore desde GITHUB y hacemos : git pull para traernoslo <br>

# Creacion de setup.py
Creacion de funcion obtener librerias
# Creacion de requirements.txt
  Escribir librerias necesarias <br>
  pip install -r requirements.txt
# Creacion de source(src)
  pip install -r requirements.txt

# SRC carpetas y archivos

# CODIGO APP.PY
Este código implementa una aplicación web Flask que tiene dos rutas:

La ruta principal '/' renderiza la plantilla 'index.html', que probablemente sea la página de inicio de la aplicación.
La ruta '/predictdata' es un punto final para predecir datos. Si se envía una solicitud GET, se renderiza la plantilla 'home.html', que probablemente sea un formulario para ingresar datos. Si se envía una solicitud POST, se procesan los datos del formulario, se crea un objeto CustomData con esos datos, se convierte en un DataFrame y se pasa a través de un pipeline de predicción (PredictPipeline) para obtener los resultados de la predicción. Luego, los resultados se pasan nuevamente a la plantilla 'home.html' para mostrarlos.
El bloque if __name__ == "__main__": se ejecuta cuando se ejecuta este archivo como un script independiente. Inicia el servidor Flask en 0.0.0.0 para que la aplicación esté disponible en todas las interfaces de red.
     
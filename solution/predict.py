# Intalamos las lbrerías necesarias 
# Predition client (El SDK para hacer predicciones)
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
# Key class for azure (Para las credenciales)
from msrest.authentication import ApiKeyCredentials
# Para obtener las variables de entorno creadas en el archivo .env
from dotenv import load_dotenv
# Importamos os para leer las variables de entorno
import os

# Obtenemos las variables 

# Cargar las claves y el endpoint 
load_dotenv()

# Set the values into variables
key = os.getenv('KEY')
endpoint = os.getenv('ENDPOINT')
project_id = os.getenv('PROJECT_ID')
published_name = os.getenv('PUBLISHED_ITERATION_NAME')

# ¡Hagamos la predicción!

# Configuramos las claves para poder usar el servicio
credentials = ApiKeyCredentials(in_headers={'Prediction-key':key})

# Creamos el "cliente" con el cual haremos la "llamada" al servicio y necesita saber
# a dónde (URL) y requiere de la credencial para poder accesar (key)
client = CustomVisionPredictionClient(endpoint, credentials)

# Abrirá la imagen de prueba en un formato binario r=read y b=binary 
with open('testing-images\Pug-t1.png', 'rb') as image:
    # Obtenemos los resultados de la predicción (Clasificación). Necesita del ID, nombre de la iteración publicada y la imagen
    results = client.classify_image(project_id, published_name, image.read())

    # Debido a que podrían existir varias categorías, las desplegamos todas con el for
    for prediction in results.predictions:
        # Finalmente, imprime la etiqueta y la probabilidad en portcentaje de la misma forma que el portal
        print(f'{prediction.tag_name}: {(prediction.probability):.2%}')

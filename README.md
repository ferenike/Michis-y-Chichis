# Michis-y-Chichis
Build a Machine Learning Model using Azure Custom Vision
## Pre-requisitos :triangular_flag_on_post:

- [Git](https://git-scm.com/downloads)
- [Visual Studio Code](https://code.visualstudio.com/download)
- [Python](https://www.python.org/downloads/) 
- Suscripción de Azure 
   - [Azure for Students](https://azure.microsoft.com/es-mx/free/students/)

## Obtén el proyecto :wink:
1. Ve a [Michis y chichis](https://github.com/ferenike/Michis-y-Chichis)
2. Da click en Code y copia el URL del repo.
![image](https://user-images.githubusercontent.com/45903954/168409069-2ed5d3a6-9f48-4641-bd97-ad11be40b43e.png)
3. Abre Git Bash y usa el comando 
4. Para ir a la carpeta que creamos usa:
5. Inicia Visual Studio Code escribiendo
## Crea el recurso :raised_hands:
1. Inicia sesión en el [Portal de Azure](https://portal.azure.com/)
2. Selecciona ***Crear un recurso nuevo***
3. Busca Custom Vision y selecciona ***Crear***
4. En aspectos básicos, llena con lo siguiente:
   - Opciones de creación: Ambos
   - Suscripción: Azure for students
   - Grupo de recursos: Crearemos uno nuevo con el nombre de custom-vision
![image](https://user-images.githubusercontent.com/45903954/168410096-4cc4e7fa-21f0-4b11-b0ff-4a56275e6ee8.png)
 
   - Región: South Central US 
   - Nombre: custom-vision-tunombre
![image](https://user-images.githubusercontent.com/45903954/168410107-e4e16a89-237d-4f79-85f8-9b0f6eed4b8a.png)
   - Plan de tarifa de aprendizaje: Free F0
   - Plan de tarifa de predicción: Free F0
![image](https://user-images.githubusercontent.com/45903954/168410115-95897b0f-de7e-4643-be0e-9789050bfea9.png)
5. Selecciona ***Revisar y crear***
6. Nuevamente selecciona ***crear***
7. Espera a que la implementación termine 
## Entrena el modelo :running:
1. Ve a [Custom Vision](https://www.customvision.ai/?WT.mc_id=academic-49102-chrhar) e inicia sesión
2. Seleccciona ***New project***
3. Dale un nombre: MichisChichis
4. Selecciona el recurso que acabamos de crear y llena con:
   - Project Types: Classification
   - Classification Types: Multiclass (Single tag per image)
   - Domains: General [A2]
5. Selecciona ***Create project***
6. Da click en ***Add images*** y selecciona las imágenes de la categoría a usar. Las imágenes de este repo tienen el nombre de la raza y están numeradas (La ubicación predeterminada desde la que se inicia Git Bash suele ser el directorio principal (~) o /c/users/<Windows-user-account>/ en el sistema operativo Windows.
Para determinar el directorio actual, escriba pwd en la línea de comandos $.)
7. Agrega la etiqueta según la raza y selecciona ***Upload***. Repite 6 y 7 para cada raza.
8. Selecciona ***Train*** y utiliza el ***Quick Training***
9. Espera a que termine 

## Prueba y usa el modelo :tada:

Este repo es basado en:
[Build a Machine Learning Model using Azure Custom Vision](https://github.com/microsoft/workshop-library/tree/main/full/ml-model-custom-vision)
[Quickstart: Create an image classification project with the Custom Vision client library or REST API](https://docs.microsoft.com/en-us/azure/cognitive-services/custom-vision-service/quickstarts/image-classification?tabs=visual-studio&pivots=programming-language-python)
https://docs.microsoft.com/es-mx/learn/modules/classify-images-custom-vision/2-azure-image-classification


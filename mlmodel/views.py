from django.shortcuts import render
from rest_framework import viewsets
from .models import MlModel
from .serializers import MlSerializer

import tensorflow as tf
import cv2
import numpy as np

# Load the trained model
model = tf.keras.models.load_model("mlmodel/models/trial_model.h5")

# Read the image to be tested
image = cv2.imread("imguploader/uploaded/test.jpg")

# Resize the image to the input shape of the model
image = cv2.resize(image, (150, 150))

# Convert the image to a numpy array and add an additional dimension
image = np.expand_dims(image, axis=0)

# Normalize the image
image = image / 255.0

prediction = model.predict(image)

# Create your views here.
class MlViewset(viewsets.ModelViewSet):
    if prediction[0]<0.5:
        queryset=MlModel.objects.filter(category="Cat")
    else:
        queryset=MlModel.objects.filter(category="Dog")
    serializer_class=MlSerializer
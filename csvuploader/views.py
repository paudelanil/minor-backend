from django.shortcuts import render
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
import io, csv, pandas as pd
from .models import File
from .serializers import FileUploadSerializer, SaveFileSerializer

# Create your views here.
class UploadFileView(generics.CreateAPIView):
    serializer_class=FileUploadSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        reader = pd.read_csv(file)
        for _, row in reader.iterrows():
            new_file = File(
                       id = row["id"],
                       name= row["name"],
                       position= row["position"],
                       age= row["age"],
                       )
            new_file.save()
        return Response({"status": "success"}, status.HTTP_201_CREATED)
    
#Show the csv uploaded in the database
class ShowDBView(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = SaveFileSerializer
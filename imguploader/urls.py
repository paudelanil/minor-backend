from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import ImgViewset

router = SimpleRouter()
router.register("imguploader", ImgViewset, basename="Img")

urlpatterns=[
    path('', include(router.urls), name="Upload_img"),
]
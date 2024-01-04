from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import MlViewset

router = SimpleRouter()
router.register("mlmodel", MlViewset, basename="ML")

urlpatterns=[
    path('', include(router.urls), name="show_ML"),
]
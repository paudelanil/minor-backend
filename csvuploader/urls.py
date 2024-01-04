from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import UploadFileView, ShowDBView

router = SimpleRouter()
router.register("showdb", ShowDBView, basename="DB")

urlpatterns=[
    path('csvuploader/', UploadFileView.as_view(), name="upload_csv"),
    path('', include(router.urls), name="show_DB"),
]
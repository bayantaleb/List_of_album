
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('music', views.AlbumView)

urlpatterns = [
    path ('', include(router.urls))
]

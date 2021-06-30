from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from myapp import views

admin.autodiscover

router = routers.DefaultRouter()
router.register(r'room', views.RoomViewSet)
router.register(r'door', views.DoorViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', views.home, name='home'),
]
from . import views
from django.urls import path
from django.conf.urls import url
from django.conf.urls import url, include
from rest_framework import routers
from Home import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    url(r'^home/$', views.show, name='home'),
    url(r'^home/main/$', views.render_template),
    url(r'^/$', views.start),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

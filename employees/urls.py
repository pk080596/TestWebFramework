from django.conf.urls import url, include
from rest_framework import routers
from django.contrib import admin
from . import views

router = routers.DefaultRouter()
router.register(r'employees', views.EmployeesViewSet)
router.register(r'salaries', views.SalariesViewSet)
router.register(r'titles', views.TitlesViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

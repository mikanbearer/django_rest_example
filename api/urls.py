from django.urls import include, path
from rest_framework import routers
from .views import LinkmanViewSet

router = routers.DefaultRouter()
router.register(r'linkman', LinkmanViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
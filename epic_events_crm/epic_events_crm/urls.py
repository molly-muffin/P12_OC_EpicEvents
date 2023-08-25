from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from authentication.views import UserViewSet
from clients.views import ClientViewSet
from contracts.views import ContractViewSet
from events.views import EventViewSet


router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('clients', ClientViewSet)
router.register('contracts', ContractViewSet)
router.register('events', EventViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),

]

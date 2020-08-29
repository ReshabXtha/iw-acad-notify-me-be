from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

import event

schema_view = get_schema_view(
    openapi.Info(
        title="NOTIFY ME API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.notifyme.com/policies/terms/",
        contact=openapi.Contact(email="contact@notifyme.local"),
        license=openapi.License(name="No License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('admin/', admin.site.urls),

    path('announcement/', include('announcement.urls')),
    path('users/', include('users.urls')),
    path('events/', include('event.urls')),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]

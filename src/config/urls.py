from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .yasg import schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    #   Need packages for urls
    path('__debug__/', include('debug_toolbar.urls')),

    #   URLS OF APPS
    # path('discounts/', 'apps.discounts.urls'),

    #   URLS OF JWT-TOKEN
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    #   SWAGGER
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

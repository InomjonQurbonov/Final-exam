from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Qurbonov Inomjon Final Exam API",
      default_version='v1',
      description="It's final exam project.\n You can find here all API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="inomjonqurbonov916@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    # token
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # swagger
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # ckeditor
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # my_apps_urls
    path('api/user/', include('app_users.urls')),
    path('api/faq/', include('app_faq.urls')),
    path('api/requirements/', include('app_requirements.urls')),
    path('api/journals/', include('app_journals.urls')),
    path('api/papers/', include('app_papers.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
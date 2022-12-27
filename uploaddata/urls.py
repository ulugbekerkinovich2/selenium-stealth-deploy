# from django.conf import settings
# from django.conf.urls.static import static
# from django.contrib import admin
# from django.urls import path, include
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('basic_app.urls'))
# ]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('admin', admin.site.urls),
    path('', include('basic_app.urls')),

    path('swagger/', TemplateView.as_view(template_name='swagger.html', extra_context={'schema_url': 'swagger'})
         , name='swagger'),
    path('openapi', get_schema_view(
        title="Upload file",
        description="API",
        version="1.0.0"
    ), name='swagger'),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

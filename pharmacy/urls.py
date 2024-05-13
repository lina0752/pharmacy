from django.urls import path, include
# from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

from medicine.admin import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('medicine.urls')),
    # Authentication
    path('users/', include('users.urls')), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
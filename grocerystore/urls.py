from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static 
from .  import settings

urlpatterns = [
    path('',include('store.urls')),
    path('accounts/',include('accounts.urls')),
    path('invoice/',include('invoice.urls')),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

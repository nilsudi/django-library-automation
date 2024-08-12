from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
 path('', views.home, name="home"),
 path('user/', include('users.urls')),
 path('members/', include('django.contrib.auth.urls')),
 path('members/', include('members.urls')),
 path('admin/', admin.site.urls),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
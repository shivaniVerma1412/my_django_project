from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from game_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', views.login_view,name='login'),
    path('register', views.register_view,name='register'),
    path('', views.home_view,name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

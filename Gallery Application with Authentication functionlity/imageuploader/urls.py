from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapp import views

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('home/', views.home),
                  path('register/', views.register, name='register'),
                  path('', views.user_login, name='login'),
                  path('logout/', views.user_logout, name='logout'),
                  path('delete_image/<str:id>', views.delete_image, name="delete_image")

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)






from django.contrib import admin
from django.urls import path
from app.views import home, forms, create, edit, update, delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('forms/', forms, name='forms'),
    path('create/', create , name='create'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('update/<int:pk>/', update, name='update'),
    path('delete/<int:pk>/', delete, name='delete')

]

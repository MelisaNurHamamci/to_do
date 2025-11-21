from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),       # Ana sayfa
    path('about/', views.about, name='about'), # Hakkımızda sayfası
    path('create/', views.create, name='create'),
    path('delete/<int:Todos_id>/', views.delete, name='delete'), # Hakkımızda sayfası
    path('yes_finish/<Todos_id>', views.yes_finish, name='yes_finish'), # Hakkımızda sayfası
    path('no_finish/<Todos_id>', views.no_finish, name='no_finish'), # Hakkımızda sayfası
    path('update/<Todos_id>', views.update, name='update'), # Hakkımızda sayfası

] 
from django.urls import path
from .views import BlogListView, BlogCreateView
# Con este nombre es llamado en el namespace de las urls de Core
app_name = "blog"

urlpatterns = [
    # Si lo dejo vacio es porque la ruta es 'localhost/blog/' ya que asi lo declare
    # en el archivo de urls de Core 
    path('', BlogListView.as_view(), name='home'),
    path('create-post/', BlogCreateView.as_view(), name='create-post'),
]
from django.urls import path
from .views import BlogListView, BlogCreateView, BlogDetailView, BlogUpdateView, BlogDeleteView
# Con este nombre es llamado en el namespace de las urls de Core
app_name = "blog"

urlpatterns = [
    # Si lo dejo vacio es porque la ruta es 'localhost/blog/' ya que asi lo declare
    # en el archivo de urls de Core 
    path('', BlogListView.as_view(), name='home'),
    path('create-post/', BlogCreateView.as_view(), name='create-post'),
    path('<int:pk>', BlogDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', BlogUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', BlogDeleteView.as_view(), name='delete'),
]
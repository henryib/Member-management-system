from django.urls import path , include
from .import views



urlpatterns = [
    path('', views.index, name ='index'),
    path('<int:id>', views.view_member, name='view_member'), 
    path('add/', views.add, name='add'),
    path('edit/<int:id>/',views.edit, name='edit' ),
    path('delete/<int:id>/',views.delete, name='delete' ),
    path('', include("django.contrib.auth.urls")),

]

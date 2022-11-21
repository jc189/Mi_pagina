from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('bd/', views.post_list, name='post_list'),
    path('knn/',views.algoritmo_knn,name='algoritmo_knn'),
    path('cbi/',views.C_Bay_ing,name='C_Bay_ing'),
    path('rl/',views.regresion_lineal,name='regresion_lineal'),
    
]
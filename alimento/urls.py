from django.urls import path
from .views import index, render_dados
urlpatterns = [
    path('',index,name='index'),
    path('render_dados', render_dados, name='render_dados'),

]
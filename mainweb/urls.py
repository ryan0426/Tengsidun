# main/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('tech-info/', views.tech_info, name='tech_info'),
    path('news/', views.news, name='news'),
    path('testing_equip/', views.testing_equip_view, name='testing_equip'),

    path('categories/precision/', views.precision_view, name='category_precision'),
    path('categories/forging/', views.forging_view, name='category_forging'),
    path('categories/cutting/', views.cutting_view, name='category_cutting'),
    path('categories/mining/', views.mining_view, name='category_mining'),
    path('categories/rollers/', views.rollers_view, name='category_rollers'),
]

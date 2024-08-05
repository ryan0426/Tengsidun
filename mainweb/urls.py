# main/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('tech-info/', views.tech_info, name='tech_info'),
    path('news/', views.news, name='news'),
    path('categories/dies/', views.dies_view, name='dies'),
    path('categories/wear_parts/', views.wear_parts_view, name='wear_parts'),
    path('categories/heading_dies/', views.heading_dies_view, name='heading_dies'),
    path('categories/bit/', views.bit_view, name='bit'),
    path('categories/rod/', views.rod_view, name='rod'),
    path('categories/cutting_tool/', views.cutting_tool_view, name='cutting_tool'),
    path('categories/cutter/', views.cutter_view, name='cutter'),
    path('categories/ram_pot/', views.ram_pot_view, name='ram_pot'),
    path('categories/non_magnetic/', views.non_magnetic_view, name='non_magnetic'),
    path('categories/precision_mold/', views.precision_mold_view, name='precision_mold'),
    path('categories/other_tools/', views.other_tools_view, name='other_tools'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('generate/', views.generate_answer_sheet, name='generate'),
    path('check/',views.correction,name='check'),
    path('checking/',views.check,name='checking')
#    path('a/', views.a, name='a'),
]

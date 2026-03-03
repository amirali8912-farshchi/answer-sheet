from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('generate/', views.generate_answer_sheet, name='generate'),
    path('api/<str:rows>/<str:tyype>/<str:test_count>/<str:name>/<str:start>/<str:types>/<str:Help2>', views.generate_answer_sheet, name='api')
#    path('a/', views.a, name='a'),
]

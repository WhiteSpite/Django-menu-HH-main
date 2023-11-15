from django.urls import path
from .views import *

app_name = 'menu'
urlpatterns = [
    path('', menu_view),
    path('<slug:slug>/', menu_view, name='menu'),
]

from django.urls import path

from . import views

urlpatterns = [
    path('chat', views.index, name='index'),
    path('chat/<str:room_name>', views.room, name='room'),
    path('apple/portfolio', views.portfolio,name = 'chat_portfolio')
]
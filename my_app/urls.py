from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Search', views.search, name='new_search'),
    # path('search', views.search, name='new_search'),
    # path('new-search/', views.new_search, name='new_search'),
]
from django.urls import path

from . import views

app_name = 'suggestions'

urlpatterns = [
    # ex: /suggestions/
    path('', views.index, name='index'),
    # ex: /suggestions/5/
    path('<int:suggestion_id>/', views.detail, name='detail'),
]

from django.urls import path

from . import views

app_name = 'suggestions'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:suggestion_id>/vote/', views.vote, name='vote'),
    path('new/', views.new_suggestion, name='new'),
]

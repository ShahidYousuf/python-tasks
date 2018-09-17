from django.urls import path
from . import views

app_name='restapp'
urlpatterns = [
    path('', views.QuoteList.as_view(), name='resthome'),
    path('<int:pk>/', views.QuoteDetail.as_view()),
    path('get-api-token/', views.CustomAuthToken.as_view()),
]


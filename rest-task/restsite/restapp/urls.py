from django.urls import path
from . import views

urlpatterns = [
    path('', views.QuoteList.as_view()),
    path('<int:pk>/', views.QuoteDetail.as_view()),
    path('get-api-token/', views.CustomAuthToken.as_view()),
]

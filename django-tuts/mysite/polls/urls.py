from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = 'polls'
urlpatterns = [
    path('',views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('signup/', views.signup, name='signup'),
    path('testpage/', views.testpage, name='testpage'),

]

from django.urls import path

from . import views

urlpatterns = [
    path('', views.session_form, name='session_insert'),
    path('<int:id>/', views.session_form, name='interview_update'),

    path('delete/<int:id>', views.session_delete, name='interview_delete'),
    path('list/', views.session_list, name='session_list'),


]
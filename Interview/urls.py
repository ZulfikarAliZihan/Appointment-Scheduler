from django.urls import path

from . import views

urlpatterns = [
    path('', views.interview_form, name='interview_insert'),
    path('<int:id>/', views.interview_form, name='interview_update'),
    path('delete/<int:id>',views.interview_delete,name='interview_delete'),
    path('list/', views.interview_list, name='interview'),
]
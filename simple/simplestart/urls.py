from django.urls import path

from .views import index, by_rubric, SsCreateView

urlpatterns = [
    path('add/', SsCreateView.as_view(), name='add'),
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('', index, name='index'),
]

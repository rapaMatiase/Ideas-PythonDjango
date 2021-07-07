
from django.urls import path
from .views import UpdateForm, ShowData

urlpatterns = [
    path('update/', UpdateForm, name='update'),
    path('data/<int:id>', ShowData, name='data_views')
]


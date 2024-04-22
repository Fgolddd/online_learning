from django.urls import path
from .views import CartView

urlpatterns = [
    path('courses/', CartView.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('courses/<int:pk>/', CartView.as_view({
        'delete': 'destroy'
    })),
]
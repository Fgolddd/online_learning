from django.urls import path
from .views import CartView

urlpatterns = [
    path('', CartView.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('<int:pk>/number/', CartView.as_view({
        'put':'update_product_number'
    })),
    path('<int:pk>/', CartView.as_view({
        'delete': 'destroy'
    })),
]
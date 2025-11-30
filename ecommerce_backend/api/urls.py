from django.urls import path
from .views import (
    RegisterView,
    UserListView,
    CategoryListCreateView,
    CategoryDetailView,
    ProductListCreateView,
    ProductDetailView,
    SomeProtectedView,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path('users/', UserListView.as_view(), name='user_list'),
    path('auth/register/', RegisterView.as_view(), name='auth_register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='login'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path("categories/", CategoryListCreateView.as_view(),
         name="category_list_create"),
    path("categories/<int:pk>/", CategoryDetailView.as_view(),
         name="category_detail"),
    path("products/", ProductListCreateView.as_view(),
         name="product_list_create"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
]

from django.contrib.auth.views import LogoutView
from django.urls import path
from django.views.generic.base import RedirectView

from shop_web.views.auth_views import SignIn, SignUp
from shop_web.views.shop_views import CartAdd, CartList, ProductDetail, ProductList

urlpatterns = [
    path('products/<int:product_id>/', ProductDetail.as_view(), name='product-detail'),
    path('products/', ProductList.as_view(), name='product-list'),
    path('cart/<int:product_id>/add/', CartAdd.as_view(), name='cart-add'),
    path('cart/', CartList.as_view(), name='cart-list'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('logout/', LogoutView.as_view(next_page='/sign-in/'), name='logout'),
    path('', RedirectView.as_view(pattern_name='product-list')),
]

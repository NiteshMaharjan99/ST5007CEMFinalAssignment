from django.urls import URLPattern, path
from ecom import views

urlpatterns = [
    # path('', views.index, name='home'),
    path('',views.store,name='store'),
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),
    # path('update_item/',views.updateItem,name='update_item'),
]
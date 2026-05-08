from django.urls import path
from.import views
urlpatterns=[
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
    path('editprofile/', views.editprofile, name='editprofile'),
    path('userlist/', views.userlist, name='userlist'),
    path('deleteuser/<int:id>/', views.deleteuser, name='deleteuser'),
     path('addproduct/', views.add_product,name='addproduct'),
    path('products/', views.product_list, name='product_list'),
    path('add_to_cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/',views.cart, name='cart'),
    path('delete_cart/<int:id>/', views.delete_cart, name='delete_cart'),
]

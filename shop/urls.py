from django.urls import path
from .import views
app_name = 'shop'
urlpatterns = [
    path('', views.bookList.as_view(), name = 'bookList'),
    path('insertCart/<int:id>', views.insertCart, name = 'insertCart'),
    path('viewCart/', views.viewCart, name = 'viewCart'),
    path('deleteCart/<int:id>', views.deleteCart, name = 'deleteCart'),
    path('updateCart/', views.updateCart, name = 'updateCart'),
]

from django.urls import path


from .views import ProductListCreateAPIView, ProductGetPutDelete, \
    ProductRetrieveUpdateDestroyAPIView, ProductTypeListCreateAPIView

urlpatterns = [
    # API :
    #      -Request Post : Create product
    #      -Request Get  : get all Products
    path('Product_ListCreate/', ProductListCreateAPIView.as_view()),
    # API :
    #      -Request Delete : remove  Pk  product
    #      -Request Put  : update  the Pk  Product
    #      -Request Get  : get the Pk  Product
    path('Product_Detail/<int:pk>/', ProductGetPutDelete.as_view()),

    path('ProductType_ListCreate/', ProductTypeListCreateAPIView.as_view()),
    path('ProductType_Detail/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view()),

]

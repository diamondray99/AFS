from django.urls import path
from .views import Home, About, Dashboard, ProdCreate, ProdUpdate, ProdDelete, ProdList, ProdDetail,\
    CatCreate, CatUpdate, CatDelete, CatList, CatDetail, create_workforce, workforce_list, \
    workforce_detail, delete_workforce, update_workforce, change_password

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),

    path('create-product/', ProdCreate.as_view(), name='create_product'),
    path('update-product/<slug:slug>/', ProdUpdate.as_view(), name='update_product'),
    path('delete-product/<slug:slug>/', ProdDelete.as_view(), name='delete_product'),
    path('list-product/', ProdList.as_view(), name='list_product'),
    path('detail-product/<slug:slug>/', ProdDetail.as_view(), name='detail_product'),

    path('create-category/', CatCreate.as_view(), name='create_category'),
    path('update-category/<slug:slug>/', CatUpdate.as_view(), name='update_category'),
    path('delete-category/<slug:slug>/', CatDelete.as_view(), name='delete_category'),
    path('list-category/', CatList.as_view(), name='list_category'),
    path('detail-category/<slug:slug>/', CatDetail, name='detail_category'),

    path('create-workforce/', create_workforce.as_view(), name='create_workforce'),
    path('update-workforce/<int:pk>/', update_workforce.as_view(), name='update_workforce'),
    path('<int:pk>/delete-workforce/', delete_workforce.as_view(), name='delete_workforce'),
    path('workforce-list/', workforce_list.as_view(), name='workforce_list'),
    path('workforce-details/<int:pk>/', workforce_detail.as_view(), name='workforce_detail'),

    path('change_password/', change_password, name='change_password'),

]

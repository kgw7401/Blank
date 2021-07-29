from django.urls import path
from .views import BlankContentupdate, BlankList, BlankDetail, BlankCreate, BlankDelete, BlankLoginView, BlankLogoutView, BlankHome, BlankUpdate, RegisterPage, BlankContentCreate, BlankContentDelete, BlankUpdate2

urlpatterns = [
    path('', BlankHome.as_view(), name='home'),
    path('blank/', BlankList.as_view(), name='blank_list'),
    path('blank/<int:pk>/', BlankDetail.as_view(), name='blank_detail'),
    path('new-blank/', BlankCreate.as_view(), name='blank_create'),
    path('blank-update/<int:pk>/', BlankUpdate.as_view(), name='blank_update'),
    path('blank-update2/<int:pk>/', BlankUpdate2.as_view(), name='blank_update2'),
    path('blank-delete/<int:pk>/', BlankDelete.as_view(), name='blank_delete'),
    path('login/', BlankLoginView.as_view(), name='login'),
    path('logout/', BlankLogoutView.as_view(), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('new-blank-content/<int:pk>', BlankContentCreate.as_view(), name='blank_content_create'),
    path('blank-content-delete/<int:pk>/', BlankContentDelete.as_view(), name='blank_content_delete'),
    path('blank-content-update/<int:pk>/', BlankContentupdate.as_view(), name='blank_content_update'),
]
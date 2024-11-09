from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home_page, name='home'),
    path('items/', views.items_page, name='items_page'),
    path('categories/', views.categories_page, name='categories_page'),
    path('items/elem/<int:pk>/', views.item_elem_page, name='item_elem_page'),
    path('category/items/<slug:slug>/', views.items_by_category_page, name='items_by_category_page'),
    path('sign-up/', views.sign_up_page, name='sign_up_page'),
    path('login/', views.login_page, name='login_page'),
    path('logout/', views.logout_action, name='logout_action')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

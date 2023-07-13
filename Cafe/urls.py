from django.urls import path
from . import views
from .views import (
    ItemDetailView,
    CheckoutView,
    HomeView,
    IndexView,
    OrderSummaryView,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
    # PaymentView,
    AddCouponView,
    search,
    welcome_user,
    ReservedDetailView,
    BarView,
    RequestRefundView
)

app_name = 'core'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('menu/', HomeView.as_view(), name='home'),
    path('bar-menu/', BarView.as_view(), name='bar'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('event-details/<pk>/', views.Event_detailsDetailView, name='event_details'),
    path('reserved/<pk>/',ReservedDetailView.as_view(), name='reserved'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    # path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),
    path('search/', search, name='search'),
    path('welcome_user/', welcome_user, name='welcome_user'),

    # path('categories/', views.Categories.as_view(), name='categories'),
    # path('category/<int:pk>', views.CategoryView.as_view(), name='category'),
    path('category/<slug>/', views.list_category, name='list_category'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('event/', views.event, name='event'),
    path('reservation/', views.reservation, name='reservation'),
]

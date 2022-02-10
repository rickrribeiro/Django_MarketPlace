  
from django.conf.urls import include
from django.urls import path
from .views import IndexView, FamousPageView, RegisterPageView, CategoryPageView,FamousRegisterPageView, CategoryListPageView, ContactFormPageView, NGOListPageView,CheckoutPageView, filterFamousByName, PaymentPageView
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('cadastro/', RegisterPageView.as_view(), name='register'),
    path('cadastro/famoso', FamousRegisterPageView.as_view(), name='famous-register'),
    path('categorias/', CategoryListPageView.as_view(), name='categories'),
    path('contato/', ContactFormPageView.as_view(), name='contato'),
    path('ongs/', NGOListPageView.as_view(), name='onsgs'),
    path('compra/<str:service>', CheckoutPageView.as_view(), name='checkout'),
    path('pagamento/<str:order>', PaymentPageView.as_view(), name='payment'),
    path(
        'idolo/<str:user>', 
        FamousPageView.as_view(),
        name='famous-page'
    ),
    path(
        'categoria/<str:category>', 
        CategoryPageView.as_view(),
        name='category-page'
    ),
    path('conta/', include('django.contrib.auth.urls')),
    path('filterFamous/',filterFamousByName, name='json'),
    path('termos/', IndexView.as_view(), name='terms'),
]
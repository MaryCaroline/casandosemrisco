from django.conf.urls import  include, url
from core.views import Home, CategoriaDetail, FornecedorDetail

urlpatterns = [
    url(r'^$', Home.as_view(), name='home'),
    url(r'^categoria/(?P<slug>[\w-]+)/$', CategoriaDetail.as_view(), name='categoria_detail'),
    url(r'^fornecedor/(?P<pk>[0-9]+)/$', FornecedorDetail.as_view(), name="fornecedor-detail"),
]
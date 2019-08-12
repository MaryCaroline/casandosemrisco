from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Categoria, Fornecedor

class Home(ListView):
    template_name = 'core/home.html'
    model = Categoria
    context_object_name = 'categorias'

class CategoriaDetail(DetailView):
    template_name = 'core/categoria.html'
    model = Categoria
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fornecedores']=Fornecedor.objects.filter(servicos__in=self.object.servicos.all()).distinct()
        return context

class FornecedorDetail(DetailView):
    template_name = 'core/fornecedor.html'
    model = Fornecedor
    
    

#  #-*- coding: utf-8 -*-

# ##################################################
# #               DJANGO IMPORTS                   #
# ##################################################
# from django.urls import reverse
# from django.shortcuts import render,redirect, render_to_response
# from django.template.loader import render_to_string
# from el_pagination.decorators import page_template
# from el_pagination.views import AjaxListView
# from django.template import RequestContext
# from django.http import HttpResponse
# from django.views.generic import RedirectView, View, UpdateView, ListView, DetailView, DeleteView
# from django.http import JsonResponse
# from django.contrib.auth import authenticate, login, logout
# from django.http import (HttpResponse,
#                          HttpResponseForbidden,
#                          HttpResponseBadRequest)
# from django.forms import formset_factory
# from datetime import datetime, timedelta
# from django.db.models import Avg
# ###################################################
# from apps.core.models import Fornecedor, Categoria, Avaliacao

# # Create your views here.

# class Index(View):
#     def get(self, request, *args, **kwargs):
#         categorias = Categoria.objects.all()
#         return render (request, 'index.html',{'categorias': categorias, 'menu':'index'})

# class CategoriaDetail(View):
#     def get(self, request, slug=None):
#         categoria = Categoria.objects.get(slug = slug)
#         servicos = categoria.servicos.all()
#         fornecedores = Fornecedor.objects.filter(servicos__in=servicos).distinct()
#         return render (request, 'categoria.html',{'categoria': categoria, 'fornecedores': fornecedores, 'servicos': servicos,'menu':'categoria'})


# class FornecedorDetail(AjaxListView, DetailView):
#     template_name = 'fornecedor.html'
#     page_template = 'includes/avaliacao_snippet.html'
#     model = Fornecedor
#     def get_context_data(self, **kwargs):
#         self.object = self.get_object()
#         context = super(FornecedorDetail, self).get_context_data(**kwargs)
#         context['avaliacoes'] = self.object.avaliacao_set.all().order_by('-avaliacao_datahora')
#         context['empresa'] = self.object.empresa
#         context['menu'] = 'fornecedor profile-page'
#         context['rating'] = list(self.object.avaliacao_set.aggregate(Avg('avaliacao_pontuacao')).values())[0]
#         context['fornecedor'] = Fornecedor.objects.get(id_fornecedor = self.kwargs['pk'])
#         return context
    
#     def post(self, request, pk):
#         rating = request.POST.get('rating')
#         avaliacao = request.POST.get('avaliacao')
#         fornecedor = self.get_object()
#         fornecedor = Fornecedor.objects.get(id_fornecedor = pk)
#         avaliacao_new = Avaliacao()
#         avaliacao_new.autor = request.user 
#         avaliacao_new.fornecedor = fornecedor
#         avaliacao_new.avaliacao_desc = avaliacao
#         avaliacao_new.avaliacao_pontuacao = rating
#         avaliacao_new.save()
#         if request.is_ajax():
#             rating = list(fornecedor.avaliacao_set.aggregate(Avg('avaliacao_pontuacao')).values())[0]
#             html = render_to_string('includes/nova_avaliacao_snippet.html', {'avaliacao': avaliacao_new})
#             avaliacoes_count = render_to_string('includes/avaliacoes_count.html', {'count': fornecedor.avaliacao_set.all().count()})
#             rating = render_to_string('includes/rating_snippet.html', {'rating': rating})
#             context = {
#                 'html': html,
#                 'rating':rating,
#                 'avaliacoes_count':avaliacoes_count
#             }
#             return JsonResponse(context)
    
        
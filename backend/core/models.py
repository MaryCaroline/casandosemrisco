from django.db import models
from django.template.defaultfilters import slugify
from datetime import datetime
from django.utils import timezone
from django.db.models.signals import post_save
from django.db.models import Avg

from users.models import User


class Telefone(models.Model):
    numero = models.CharField(max_length=15)
    nome_contato = models.CharField(max_length=45, blank=True, null=True)
    fornecedor = models.ForeignKey('Fornecedor', blank=False, null=False, on_delete=models.CASCADE)
    def __unicode__(self):
        return self.numero

class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    cep = models.CharField(max_length=10)
    cnpj = models.CharField(max_length=20)
    logo = models.ImageField(upload_to='fornecedores/logos/', blank=True, null=True,
                             default='fornecedores/default.jpg', verbose_name='Logo')
    servicos = models.ManyToManyField('Servico')
    avaliacoes = models.ManyToManyField(User, through='Avaliacao', through_fields=('fornecedor', 'autor'))
    def __str__(self):
        return self.nome
    def get_rating(self):
        print(self.avaliacoes.count())
        if self.avaliacao_set.count():
            return list(self.avaliacao_set.aggregate(Avg('avaliacao_pontuacao')).values())[0]
        return 0

class Servico(models.Model):
    servico_desc = models.CharField(max_length=45, blank=False)
    def __str__(self):
        return self.servico_desc

class Categoria(models.Model):
    categoria_title = models.CharField(max_length=45, blank=False)
    categoria_desc = models.TextField(max_length=400, blank=False)
    imagem = models.ImageField(upload_to='categorias/imagens/', blank=True, null=True,
                               default='categorias/default.jpg', verbose_name='Imagem')
    servicos = models.ManyToManyField('Servico')
    slug = models.SlugField(max_length=60, blank=True, verbose_name='slug')
    def __str__(self):
        return self.categoria_title
    def save(self, * args, ** kwargs):
        if not self.pk:
            self.slug = slugify(self.categoria_title)
        super(Categoria, self).save( * args, ** kwargs)

class Avaliacao(models.Model):
    autor = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)
    fornecedor = models.ForeignKey('Fornecedor', blank=False, null=False, on_delete=models.CASCADE)
    avaliacao_desc = models.TextField(max_length=1000, blank=False, null=False)
    avaliacao_pontuacao = models.IntegerField(blank=False, null=False)
    avaliacao_datahora = models.DateTimeField(blank=False, null=False, auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='avaliacao_likes', blank=True)
    @property
    def total_likes(self):
        return self.likes.count()
    def __str__(self):
        return self.avaliacao_desc

class Comentario(models.Model):
    avaliacao = models.ForeignKey('Avaliacao', blank=False, null=False, on_delete=models.CASCADE)
    texto = models.TextField(max_length = 1000, blank=False, null=False)
    usuario = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)
    datahora = models.DateTimeField(blank=False, null=False, auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='comentario_likes', blank=True)
    def __str__(self):
        return self.texto

class Denuncia(models.Model):
    usuario = models.ForeignKey(User, blank=False, null=False, on_delete=models.CASCADE)
    comentario = models.ForeignKey('Comentario', blank=False, null=False, on_delete=models.CASCADE)
    def __str__(self):
        return f'Denuncia: {self.comentario.texto}'
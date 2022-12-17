from django.shortcuts import render
from categoria.models import Categoria
from django.http import JsonResponse
# Create your views here.

def index(request):
    return render(request,"alimento/index.html")

def render_dados(request):
    if request.method == "GET":
        lista_categorias = []
        lista_alimentos = []
        valores = []
        categorias = Categoria.objects.all().order_by("nome")
        for c in categorias:
            lista_nome_alimento = []
            valores_ind = []
            lista_categorias.append(c.nome)
            alimentos = c.alimento_set.all()
            for i in alimentos:
                lista_nome_alimento.append(i.nome)
                valores_ind.append(i.valor)
            lista_alimentos.append(lista_nome_alimento)
            valores.append(sum(valores_ind))
            total = sum(valores)
            portentagem = []
            for v in valores:
                portentagem.append((v / total) * 100)
           
        return JsonResponse({"categorias":lista_categorias,"alimentos":lista_alimentos,"valores":sum(valores),"porcentagem":portentagem})



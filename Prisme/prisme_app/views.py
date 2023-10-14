from django.shortcuts import render, redirect
from .utils import linhas, barras
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .models import Projeto, Ong, DadosImpactos

# Create your views here.

tipos = ["Selecione o tipo de dado",
        "Pessoas Impactadas por tempo",
        "Casas Construidas por tempo",
        "Números de Impacto",
        "Valor por Pessoa"
        ]


#@login_required
def home(request):
    contexto = {
    }
    return render(request, "home.html", context=contexto)

#@login_required
def add_di(request):
    contexto = {

    }
    return render(request, "dados.html", context=contexto)

#@login_required
def teste(request):
    contexto={
        "grafico": linhas([1,2,3], [20,30,40], "penis", "penisX", "penisY")
    }
    return render(request, "ex.html", context=contexto)


def login(request):
    if request.method == "POST":
        usuario = request.POST["usuario"]
        senha = request.POST["senha"]

        user = authenticate(request, username=usuario, password=senha)
        if user is not None:
            login(request, user)
            return redirect(home)
        else:
            return render(request, "login.html", {"erro": "Usuário não encontrado"})
    return render(request, "login.html")


def add_projeto(request):
    erros = {}
    if request.method == 'POST':
        errado = False
        ong = request.POST['ong']
        nome_projeto = request.POST['nome_projeto']
        descricao = request.POST['descricao']
        metodologiasUtilizadas = request.POST['metodologia']
        publicoAlvo = request.POST['publico']
        dataDeCriacao = request.POST['criacao']

        if not nome_projeto or not descricao or not metodologiasUtilizadas or not publicoAlvo or dataDeCriacao is None:
            erros["campos"] = "Preencha todos os campos necessários"
            errado = True

        if errado:
                contexto = {
                    "erros": erros,
                    "nome_projeto": nome_projeto,
                    "descricao": descricao,
                    "metodologiasUtilizadas": metodologiasUtilizadas,
                    "publicoAlvo": publicoAlvo,
                }
                return render(request, "add_projeto.html", contexto)
        if Projeto.objects.filter(nome_projeto=nome_projeto).exists():
            return render(request, 'add_projeto.html', {"erro": "Esse Projeto já existe"})
        if Ong.objects.filter(nome=ong).exists():
            Projeto.objects.create(ong=Ong.objects.filter(nome=ong).first(),nome_projeto=nome_projeto,descricao=descricao,metodologiasUtilizadas=metodologiasUtilizadas,publicoAlvo=publicoAlvo,dataDeCriacao=dataDeCriacao)
            return redirect(add_dados)
        else:
            return render(request, 'add_projeto.html', {"erro": "Essa ONG Não existe"})

    return render(request,'add_projeto.html')


def add_dados(request):
    erros = {}
    if request.method == 'POST':
        errado = False
        projeto = request.POST['projeto']
        titulo = request.POST['titulo']
        descricao = request.POST['descricao']
        valor1 = request.POST['valor1']
        valor2 = request.POST['valor2']
        tipo = request.POST['tipo']

        if not projeto or not descricao or not titulo or not valor1 or not valor2  or tipo is "Selecione o tipo de dado":
            erros["campos"] = "Preencha todos os campos necessários"
            errado = True
        
        if errado:
                contexto = {
                    "erros": erros,
                    "projeto": projeto,
                    "descricao": descricao,
                    "titulo": titulo,
                    "valor1": valor1,
                    "valor2":valor1,
                    "tipo":tipo,
                    "tipos":tipos
                }
                return render(request, "add_dados.html", contexto)
        
        if DadosImpactos.objects.filter(titulo=titulo).exists():
            return render(request, 'add_projeto.html', {"erro": "Esse Dado já existe"})
        if Projeto.objects.filter(nome_projeto=projeto).exists():
            DadosImpactos.objects.create(projeto=Projeto.objects.filter(nome_projeto=projeto).first(),titulo=titulo,descricao=descricao,valor1=valor1,valor2=valor2)
            return redirect(home)
        else:
            return render(request, 'add_dados.html', {"erro": "Essa Projeto Não existe"})

    return render(request,'add_dados.html',{"tipos":tipos})
from django.shortcuts import render, redirect
from . models import Contatos

def index(request):
    contatos = Contatos.objects.filter(ativo=False).order_by('-id')  
    #esse order_by faz a ordenação por que quiser, o "-id" é para exibir do maior para o menor, mas poderia fazer também por nome em ordem alfabética
    return render(request, 'pages/index.html', {'contatos':contatos})

def search(request):
    q = request.GET.get('search')
    contatos = Contatos.objects.filter(nome__icontains=q)
    return render(request, 'pages/index.html', {'contatos':contatos})

def detalhes(request, id):
    contato = Contatos.objects.get(id=id)
    return render(request, 'pages/detalhes.html', {'contato':contato})

def deletar(request, id):
    contato = Contatos.objects.get(id=id)
    contato.delete()
    return redirect('home')

def adicionar(request):

    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        email = request.POST.get('email')
        altura = request.POST.get('altura')
        descricao = request.POST.get('descricao')
        data = request.POST.get('data_nasc')
        telefone = request.POST.get('telefone')
        imagem = request.FILES.get('imagem')
        novo_contato = Contatos(nome=nome,cpf=cpf, email=email, altura=altura, descricao=descricao, data_nascimento=data, telefone=telefone, imagem=imagem, ativo=True)
        novo_contato.save()
        return redirect('home')


    else:
        return render(request, 'pages/adicionar.html')
    

def editar(request, id):
    contato = Contatos.objects.get(id=id)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        email = request.POST.get('email')
        altura = request.POST.get('altura')
        descricao = request.POST.get('descricao')
        data = request.POST.get('data_nasc')
        telefone = request.POST.get('telefone')
        imagem = request.FILES.get('imagem')
        check = request.FILES.get('check')
        if check == None:
            check = False
        else:
            check = True
        
        contato.nome = nome
        contato.cpf = cpf
        contato.email = email
        contato.altura = altura
        contato.descricao = descricao
        contato.data_nascimento = data
        contato.telefone = telefone
        contato.imagem = imagem
        contato.ativo = check
        contato.save()

        return redirect('home')

    else:
        return render(request, 'pages/editar.html', {'contato': contato})
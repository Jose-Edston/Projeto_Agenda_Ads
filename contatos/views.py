from django.shortcuts import render, redirect, get_object_or_404
from . models import Contatos
from django.contrib.auth.decorators import login_required

@login_required(redirect_field_name='login')
def index(request):
    contatos = Contatos.objects.filter(usuario_id=request.user.id).order_by('-id')  
    #esse order_by faz a ordenação por que quiser, o "-id" é para exibir do maior para o menor, mas poderia fazer também por nome em ordem alfabética
    return render(request, 'pages/index.html', {'contatos':contatos})

def search(request):
    q = request.GET.get('search')
    contatos = Contatos.objects.filter(nome__icontains=q)
    return render(request, 'pages/index.html', {'contatos':contatos})

def detalhes(request, id):
    # contato = Contatos.objects.get(id=id)
    contato = get_object_or_404(Contatos, id=id)
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
        novo_contato = Contatos(usuario_id=request.user.id, nome=nome,cpf=cpf, email=email, altura=altura, descricao=descricao, data_nascimento=data, telefone=telefone, imagem=imagem, ativo=True)
        # request.user.id pega sempre o valor do usuário logado, ou seja, ele ja pega a informação de quem é o usuário logado
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
        print(imagem)
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
        if imagem != None:
            contato.imagem = imagem
        contato.ativo = check
        contato.save()

        return redirect('home')

    else:
        return render(request, 'pages/editar.html', {'contato': contato})
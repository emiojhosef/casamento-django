from django.shortcuts import render, redirect, get_object_or_404
from casamento.models import ListaPresente, Convidado, MembroDaFamilia
from casamento.forms import ConvidadoForms, TelefoneForms
from django.contrib import messages

def convite(request):
    if request.method == 'POST':
        form = ConvidadoForms(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            try:
                convidado = Convidado.objects.get(nome=nome)

                if convidado.nome:
                    request.session['nome_convidado'] = nome
                    return redirect('conviteencontrado')
        
            except Convidado.DoesNotExist:
                messages.error(request, 'Você não está na lista de convidados')
                
                return redirect('convite')
    else:
        form = ConvidadoForms()
    
    presentes = ListaPresente.objects.order_by("preco").filter(publicada=True)

    contexto = {
        'form':form,
        'presentes':presentes,
    }
    
    return render(request, 'convite.html', contexto)


def conviteencontrado(request):
    nome = request.session.get('nome_convidado')
    if not nome:
        messages.error(request, 'Faça o login novamente.')
        return redirect('convite')

    convidado = get_object_or_404(Convidado, nome=nome)
    membros = convidado.familia.all()  # pega os membros da família

    if request.method == 'POST':
        selecionados = request.POST.getlist('confirmados')  # pega lista dos selecionados

        # Verifica se o convidado principal foi selecionado
        if 'convidado' not in selecionados:
            messages.error(request, 'Por favor, selecione seu nome antes de confirmar.')
            return redirect('conviteencontrado')

        # Confirma presença do convidado principal
        #convidado.confirmado = True
        membros_selecionados = [int(id) for id in selecionados if id != 'convidado']
        request.session['membros_confirmados'] = membros_selecionados
        
        convidado.save()

        # Confirma presença dos membros da família selecionados
        #for membro in membros:
            #if str(membro.id) in selecionados:
                #membro.confirmado = True
            #else:
                #membro.confirmado = False
            #membro.save()

        #messages.success(request, 'Presença confirmada com sucesso!')
        return redirect('confirmacaopresenca')


    return render(request, 'convite-encontrado.html', {
        'nome': nome,
        'membros': membros,
    })

def confirmacaopresenca(request):
    nome = request.session.get('nome_convidado')  # Agora acessível em qualquer método

    if not nome:
        messages.error(request, 'Nome do convidado não encontrado. Volte à página de convite.')
        return redirect('convite')

    if request.method == 'POST':
        codigo = ''.join([
            request.POST.get('digito1', ''),
            request.POST.get('digito2', ''),
            request.POST.get('digito3', ''),
            request.POST.get('digito4', '')
        ])

        try:
            convidado = Convidado.objects.get(nome=nome)
            membros = convidado.familia.all()

            if convidado.senha == codigo:
                if not convidado.confirmado:
                    convidado.confirmado = True
                    ids_confirmados = [int(id) for id in request.session.get('membros_confirmados', [])]
                    
                    for membro in membros:
                        if membro.id in ids_confirmados:
                            membro.confirmado = True
                            membro.save()
                else:
                    convidado.confirmado_2 = True
                convidado.save()
                messages.success(request, 'Presença confirmada com sucesso!')
                return redirect('presencaconfirmada')
            else:
                messages.error(request, 'Código incorreto. Tente novamente.')
        except Convidado.DoesNotExist:
            messages.error(request, 'Convidado não encontrado.')
            return redirect('convite')

    return render(request, 'confirmacao-presenca.html', {'nome': nome})

def presencaconfirmada(request):
    return render(request, 'presenca-confirmada.html')
'''def presentes(request):
    fotografias = ListaPresente.objects.order_by("preco").filter(publicada=True)
    return render(request, 'lista-presentes-emio-thayla.html', {"cards": fotografias})

def informacoes_importantes(request):
    return render(request, 'informacoes-importante.html')'''
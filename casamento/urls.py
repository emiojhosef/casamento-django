from django.urls import path
from casamento.views import convite, conviteencontrado, confirmacaopresenca, presencaconfirmada

urlpatterns = [
    path("", convite, name='convite'),
    path("conviteencontrado/", conviteencontrado, name='conviteencontrado'),
    path("confirmacaopresenca/", confirmacaopresenca, name='confirmacaopresenca'),
    path("presencaconfirmada/", presencaconfirmada, name='presencaconfirmada'),
    #path("mensagem_confirmacao/", mensagem_confirmacao, name='mensagem_confirmacao'),
]
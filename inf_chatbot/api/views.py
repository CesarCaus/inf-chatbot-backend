from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MessageSerializer
from .ai_model import buscar_resposta_com_contexto
from autocorrect import Speller

def corrigir_frase(frase_errada):
    spell = Speller()
    palavras = frase_errada.split()  # Divide a frase em palavras
    palavras_corrigidas = [spell(palavra) for palavra in palavras]  # Corrige cada palavra
    return ' '.join(palavras_corrigidas)

@api_view(['POST'])
def receive_message(request):
    serializer = MessageSerializer(data=request.data)

    if serializer.is_valid():
        # Extrai os dados da mensagem do serializer validado
        message_data = serializer.validated_data['text']
        frase_corrigida = corrigir_frase(message_data)

        # Processa a mensagem com o modelo BERT e captura a resposta
        resposta_gerada = buscar_resposta_com_contexto(frase_corrigida)

        # Configura a resposta com o texto gerado pelo modelo
        response_data = {
            "text": resposta_gerada,
            "type": "received"
        }
        return Response(response_data, status=status.HTTP_200_OK)

    # Retorna erro caso o serializer não seja válido
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

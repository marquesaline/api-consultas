from rest_framework import viewsets, status
from rest_framework.views import Response, APIView
from rest_framework.decorators import action

from consultas.models import Profissional, Consulta
from consultas.serializers import ProfissionalSerializer, ConsultaSerializer


class ProfissionaisView(APIView):
    
    def get(self, request):
        profissionais = Profissional.objects.all()
        serializer = ProfissionalSerializer(profissionais, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        data = {
            'nome': request.data.get('nome'),
            'nome_social': request.data.get('nome_social') if request.data.get('nome_social') else '',
            'especialidade': request.data.get('especialidade'),
        }

        serializer = ProfissionalSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                'mensagem': 'Profissional cadastrado com sucesso',
                'detalhes': serializer.data
            }, status=status.HTTP_201_CREATED)
        
        return Response({
            'erro': 'Confira os dados informados'}, 
            status=status.HTTP_400_BAD_REQUEST
        )
    

class ProfissionalView(APIView):
    def get_404_view(self, id):
        return Response(
            {'erro': f'Não foi possível encontrar um profissional com o id: {id}'}, 
            status=status.HTTP_404_NOT_FOUND
        )  

    def get(self, request, id, *args, **kwargs):
        profissional = Profissional.objects.filter(id=id).first()

        if not profissional:
            return self.get_404_view(id)
        
        serializer = ProfissionalSerializer(profissional)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id, *args, **kwargs):
        profissional = Profissional.objects.filter(id=id).first()

        if not profissional:
            return self.get_404_view(id)
        
        data = {
            'nome': request.data.get('nome'),
            'nome_social': request.data.get('nome_social') if request.data.get('nome_social') else '',
            'especialidade': request.data.get('especialidade'),
        }
        serializer = ProfissionalSerializer(instance=profissional, data=data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                'mensagem': 'Profissional atualizado com sucesso',
                'detalhes': serializer.data
            }, status=status.HTTP_201_CREATED)
        
        return Response({
            'erro': 'Confira os dados informados'}, 
            status=status.HTTP_400_BAD_REQUEST
        )
    
    def delete(self, request, id):
        profissional = Profissional.objects.filter(id=id).first()

        if not profissional:
            return self.get_404_view(id)
        
        profissional.delete()
        return Response(
            {'mensagem': 'Profissional excluído com sucesso'},
            status=status.HTTP_200_OK
        )
    


    
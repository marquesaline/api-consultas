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
    def get_404_return(self, id):
        return Response(
            {'erro': f'Não foi possível encontrar um profissional com o id: {id}'}, 
            status=status.HTTP_404_NOT_FOUND
        )  

    def get(self, request, profissional_id, *args, **kwargs):
        profissional = Profissional.objects.filter(id=profissional_id).first()

        if not profissional:
            return self.get_404_return(id)
        
        serializer = ProfissionalSerializer(profissional)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, profissional_id, *args, **kwargs):
        profissional = Profissional.objects.filter(id=profissional_id).first()

        if not profissional:
            return self.get_404_return(profissional_id)
        
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
    
    def delete(self, request, profissional_id):
        profissional = Profissional.objects.filter(id=profissional_id).first()

        if not profissional:
            return self.get_404_return(profissional_id)
        
        profissional.delete()
        return Response(
            {'mensagem': 'Profissional excluído com sucesso'},
            status=status.HTTP_200_OK
        )
    

class ConsultasView(APIView):
    def get(self, request):
        consultas = Consulta.objects.all()
        serializer = ConsultaSerializer(consultas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        data = {
            'paciente': request.data.get('paciente'),
            'nome_social': request.data.get('nome_social') if request.data.get('nome_social') else '',
            'data_consulta': request.data.get('data_consulta'),
            'profissional': request.data.get('profissional')
        }
        serializer = ConsultaSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                'mensagem': 'Consulta cadastrada com sucesso',
                'detalhes': serializer.data
            }, status=status.HTTP_201_CREATED)
        
        return Response({
            'erro': serializer.errors}, 
            status=status.HTTP_400_BAD_REQUEST
        )
    

class ConsultaView(APIView):
    def get_404_return(self, id):
        return Response(
            {'erro': f'Não foi possível encontrar uma consulta com o id: {id}'}, 
            status=status.HTTP_404_NOT_FOUND
        )  

    def get(self, request, consulta_id, *args, **kwargs):
        consulta = Consulta.objects.filter(id=consulta_id).first()

        if not consulta:
            return self.get_404_return(consulta_id)
        
        serializer = ConsultaSerializer(consulta)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, consulta_id, *args, **kwargs):
        consulta = Consulta.objects.filter(id=consulta_id).first()

        if not consulta:
            return self.get_404_return(consulta_id)
        
        data = {
            'paciente': request.data.get('paciente'),
            'nome_social': request.data.get('nome_social') if request.data.get('nome_social') else '',
            'data_consulta': request.data.get('data_consulta'),
            'profissional': request.data.get('profissional')
        }
        serializer = ConsultaSerializer(instance=consulta, data=data)

        if serializer.is_valid():
            serializer.save()
            return Response({
                'mensagem': 'Consulta atualizada com sucesso',
                'detalhes': serializer.data
            }, status=status.HTTP_201_CREATED)
        
        return Response({
            'erro': serializer.errors}, 
            status=status.HTTP_400_BAD_REQUEST
        )
    
    def delete(self, request, consulta_id):
        consulta = Consulta.objects.filter(id=consulta_id).first()

        if not consulta:
            return self.get_404_return(consulta_id)
        
        consulta.delete()
        return Response(
            {'mensagem': 'Consulta excluída com sucesso'},
            status=status.HTTP_200_OK
        )
    

class ConsultaProfissionalView(APIView):
    
    def get(self, request, profissional_id):
        consultas = Consulta.objects.filter(profissional=profissional_id).all()
        serializer = ConsultaSerializer(consultas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
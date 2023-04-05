from django.urls import reverse
from rest_framework.test import APITestCase

from consultas.models import Profissional, Consulta


class ConsultasTestCase(APITestCase):

    def setUp(self):
        self.profissional = Profissional.objects.create(
            nome='Laverne Alison Cox',
            nome_social='Laverne Cox',
            especialidade='Mastologia'
        )

        self.consulta = Consulta.objects.create(
            paciente='Laura Prepon',
            data_consulta='2023-07-19',
            profissional=self.profissional
        )

    def test_get_all(self):

        with self.subTest('Profissionais'):
            response = self.client.get(reverse('consultas:profissionais'))
        
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content, b'[{"id":1,"nome":"Laverne Alison Cox","nome_social":"Laverne Cox","especialidade":"Mastologia"}]')
        
        with self.subTest('Consultas'):
            response = self.client.get(reverse('consultas:consultas'))

            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content, b'[{"id":1,"paciente":"Laura Prepon","nome_social":"","profissional":1,"data_consulta":"2023-07-19"}]')

    def test_post(self):
        outra_consulta = {
            'paciente': 'Taylor Schilling',
            'data_consulta': '19-07-2023',
            'profissional': self.profissional.id
        }

        with self.subTest('Profissionais'):
            outro_profissional = {
                'nome': 'Angelina Jolie',
                'especialidade': 'Ginecologia'
            }
            response = self.client.post(reverse('consultas:profissionais'), data=outro_profissional)
            self.assertEqual(response.status_code, 201)

        with self.subTest('Consultas'):
            response = self.client.post(reverse('consultas:consultas'), data=outra_consulta)
            self.assertEqual(response.status_code, 201)

        with self.subTest('Cadastro de consulta com data anterior a data atual'):
            outra_consulta['data_consulta'] = '01-01-2023'
            
            response = self.client.post(reverse('consultas:consultas'), data=outra_consulta)
            self.assertEqual(response.status_code, 400)

        with self.subTest('Cadastro de consulta com profissional inexistente'):
            outra_consulta['profissional'] = 1000
            
            response = self.client.post(reverse('consultas:consultas'), data=outra_consulta)
            self.assertEqual(response.status_code, 404)

    def test_get(self):

        with self.subTest('Profissional'):
            response = self.client.get(reverse('consultas:profissional', kwargs={
                'profissional_id': self.profissional.id
            }))
        
            self.assertEqual(response.status_code, 200)
        
        with self.subTest('Consulta'):
            response = self.client.get(reverse('consultas:consulta', kwargs={
                'consulta_id': self.consulta.id
            }))

            self.assertEqual(response.status_code, 200)

        with self.subTest('Consultas por profissional'):
            response = self.client.get(reverse('consultas:consulta_profissional', kwargs={
                'profissional_id': self.profissional.id
            }))

            self.assertEqual(response.status_code, 200)

    def test_put(self):

        with self.subTest('Profissional'):
            profissional = {
                'nome': 'Angelina Jolie Voight',
                'nome_social': 'Angelina Jolie',
                'especialidade': 'Ginecologia'
            }

            response = self.client.put(reverse('consultas:profissional', kwargs={
                'profissional_id': self.profissional.id
            }), data=profissional)

            self.assertEqual(response.status_code, 200)

        with self.subTest('Consulta'):
            consulta = {
                'paciente': 'Taylor Schilling',
                'data_consulta': '19-07-2023',
                'profissional': self.profissional.id
            }

            response = self.client.put(reverse('consultas:consulta', kwargs={
                'consulta_id': self.consulta.id
            }), data=consulta)

            self.assertEqual(response.status_code, 200)
    

    def test_delete(self):
              
        with self.subTest('Consulta'):
            response = self.client.delete(reverse('consultas:consulta', kwargs={
                'consulta_id': self.consulta.id
            }))

            self.assertEqual(response.status_code, 200)

        with self.subTest('Profissional'):
            response = self.client.delete(reverse('consultas:profissional', kwargs={
                'profissional_id': self.profissional.id
            }))
        
            self.assertEqual(response.status_code, 200)
  
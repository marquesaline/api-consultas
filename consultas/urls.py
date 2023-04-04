from django.urls import path

from consultas.views import ConsultaView, ConsultasView, ProfissionaisView, ProfissionalView, ConsultaProfissionalView

urlpatterns = [
    path('', ConsultasView.as_view(), name='consultas'),
    path('<int:consulta_id>', ConsultaView.as_view(), name='consulta'),
    path('profissional/<int:profissional_id>', ConsultaProfissionalView.as_view(), name='consulta_profissional'),
    path('profissionais', ProfissionaisView.as_view(), name='profissionais'),
    path('profissionais/<int:profissional_id>', ProfissionalView.as_view(), name='profissional')
]
from django.urls import path

from consultas.views import ConsultasView, ProfissionaisView, ProfissionalView

urlpatterns = [
    path('', ConsultasView.as_view(), name='consultas'),
    path('profissionais', ProfissionaisView.as_view(), name='profissionais'),
    path('profissionais/<int:id>', ProfissionalView.as_view(), name='profissional')
]
from django.urls import path

from consultas.views import ProfissionaisView, ProfissionalView

urlpatterns = [
    path('profissionais', ProfissionaisView.as_view(), name='profissionais'),
    path('profissionais/<int:id>', ProfissionalView.as_view(), name='profissional')
]
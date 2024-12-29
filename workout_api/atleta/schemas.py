from typing import Annotated, Optional
from pydantic import Field, PositiveFloat

from workout_api.categorias.schemas import CategoriaIn
from workout_api.centro_treinamento.schemas import CentroTreinamentoAtleta
from workout_api.contrib.schemas import BaseSchema, OutMixin


class Atleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome do Atleta', example='Rafael', max_lenght=50)]
    cpf: Annotated[str, Field(description='cpf do Atleta', example='12345678943', max_lenght=11)]
    idade: Annotated[int, Field(description='Idade do Atleta', example='26')]
    peso: Annotated[PositiveFloat, Field(description='Peso do Atleta', example='75.5')]
    altura: Annotated[PositiveFloat, Field(description='Altura do Atleta', example='1.70')]
    sexo: Annotated[str, Field(description='Sexo do Atleta', example='M')]
    categoria: Annotated[CategoriaIn, Field(description='Categoria do Atleta')]
    centro_treinamento: Annotated[CentroTreinamentoAtleta, Field(description='Centro de Treinamento do Atleta')]



class AtletaIn(Atleta):
    pass

class AtletaOut(Atleta, OutMixin):
    pass

class AtletaUpdate(BaseSchema):
    nome: Annotated[Optional[str], Field(None, description='Nome do atleta', example='Joao', max_length=50)]
    idade: Annotated[Optional[int], Field(None, description='Idade do atleta', example=25)]
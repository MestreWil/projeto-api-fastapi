from typing import Annotated
from pydantic import Field
from workout_api.contrib.schemas import BaseSchema

class CentroTreinamento(BaseSchema):
  nome: Annotated[str, Field(description="Nome do Centro de Treinamento", example="Iron Berg", max_length=20)]
  endereco: Annotated[str, Field(description="Endereço do Centro de Treinamento", example="Av. Borges de Medeiros, nº 1415, proximo ao mac donalds", max_length=60)]
  propietario: Annotated[str, Field(description="Proprietario do Centro de Treinamento", example="William Tavares", max_length=30)]
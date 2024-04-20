from typing import Optional
from pydantic import BaseModel

from .dados_basicos_miro import DadosBasicos
from .referencia_pedido import ReferenciaPedido
from .detalhe import Detalhe
from .sintese_miro import SinteseMiro
from .dados_nfe import DadosNfe

class Miro(BaseModel):
    dados_basicos: DadosBasicos
    referencia_pedido: Optional[ReferenciaPedido] = None
    detalhe: Detalhe
    sintese: SinteseMiro
    dados_nfe: DadosNfe
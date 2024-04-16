from pydantic import BaseModel
from typing import List, Optional

from .itens_fatura import ItensFatura

class DadosBasicos(BaseModel):
    cod_fornecedor: str
    data_fatura: str
    referencia: Optional[str] = None
    montante: str
    bus_pl_sec_cd: str
    texto: str
    itens: Optional[List[ItensFatura]] = None
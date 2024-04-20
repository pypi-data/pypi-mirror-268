from pydantic import BaseModel
from typing import List

from .itens_fatura import ItensFatura

class Pagamento(BaseModel):
    data_basica: str
    cond_pgto: str
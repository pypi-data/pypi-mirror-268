from pydantic import BaseModel
from typing import Optional

class ItensFatura(BaseModel):
    Cta_razao: str
    Montante: str
    loc_negocios: str
    atribuicao: Optional[str]
    texto: str
    centro_custo: str
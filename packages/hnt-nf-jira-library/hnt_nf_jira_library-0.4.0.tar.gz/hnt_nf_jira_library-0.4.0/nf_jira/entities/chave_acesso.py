from pydantic import BaseModel

class ChaveAcesso(BaseModel):
    tp_emissao: str
    numero_aleatorio: str
    dig_verif: str
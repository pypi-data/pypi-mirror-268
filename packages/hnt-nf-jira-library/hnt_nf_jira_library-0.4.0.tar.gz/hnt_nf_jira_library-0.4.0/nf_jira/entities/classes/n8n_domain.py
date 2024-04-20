import requests
from ..constants import *

class N8NDomain:


    def get_nf_domain(self, type, cnpj):

        n8n_data = self._get_nf_domain_data(cnpj, type)
        return n8n_data
    
    def get_allocation(self, cnpj_fornecedor, cnpj_cliente, numero_contratos):

        allocation = self._get_allocation(cnpj_fornecedor, cnpj_cliente, numero_contratos)
        return allocation


    def _get_nf_domain_data(self, cnpj, type):

        try:
            domain_request = requests.get(
                f"{API_DOMAIN_N8N_URL}/{'fornecedores' if type == 'fornecedor' else 'centros'}?cnpj={cnpj}",
                auth=N8N_AUTH,
            )
            domain_request.raise_for_status()
            domain_data = domain_request.json()

            if not domain_data:
                raise Exception("Could not find domain")

        except Exception as e:
            raise Exception(f"Erro ao receber {type}:\n{e}")

        return domain_data

    def _get_allocation(self, cnpj_fornecedor: str, cnpj_cliente: str, numero_contrato: str):

        try:
            allocation_request = requests.get(
                f"{API_DOMAIN_N8N_URL}/rateio?cnpj_fornecedor={cnpj_fornecedor}&cnpj_hortifruti={cnpj_cliente}&numero_contrato={numero_contrato}",
                auth=N8N_AUTH,
            )
            allocation_request.raise_for_status()
            if allocation_request.text.strip() != "":
                allocation_data = allocation_request.json()
            else:
                allocation_data = None
        except Exception as e:
            raise Exception(f"Erro ao receber rateio:\n{e}")

        return allocation_data

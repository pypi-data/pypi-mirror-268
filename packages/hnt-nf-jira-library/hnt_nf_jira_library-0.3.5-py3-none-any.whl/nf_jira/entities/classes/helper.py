import json
from os import getcwd, makedirs, path
from nf_consumo.consumo_service import ConsumoService
from ..constants import *

class BaseHelper:

    def __init__(self):
        self.ConsumoService = ConsumoService()

class JsonHelper(BaseHelper):

    def save_json(self, filename, json_data):

        path_dir = path.join(getcwd(), 'output/json')
        if not path.exists(path_dir):
            makedirs(path_dir)

        with open(f"./output/json/{filename}.json", "w", encoding="utf-8") as json_file:
            json.dump( json_data, json_file, ensure_ascii=False, indent=4)

class JiraFieldsHelper(BaseHelper):

    def remove_null_fields(self, fields):
        fields_data_without_nulls = {}

        for key, value in fields.items():
            if value is not None:
                fields_data_without_nulls[key] = value

        return fields_data_without_nulls
    
    def _rename_fields(self, fields):
        fields = self._fields
        new_fields_data = {}

        for key, value in self._jira_fields.items():
            if value in fields:
                if "text" in fields[value]:
                    new_value = fields[value].get("text")
                elif "date" in fields[value]:
                    new_value = fields[value].get("date")
                elif "value" in fields[value]:
                    new_value = fields[value].get("value")
                else:
                    new_value = fields[value]

                new_fields_data[key] = new_value

        return new_fields_data
    
class GuiandoHelper(BaseHelper):

        def download_pdf_nexinvoice(self, attachment):
            path = attachment[ARQUIVOS_DA_FATURA][0]
            pdf = self._download_pdf(path)
            return pdf

        def _download_pdf(self, pdf_path):
            path_dir = path.join(getcwd(), "output/pdf")
            pdf_file = self.ConsumoService.download_pdf(pdf_path, path_dir)

            return pdf_file

        def include_cod_sap_miro(self, cod_sap, miro):

            miro['referencia_pedido']['numero_pedido'] = cod_sap
            return miro
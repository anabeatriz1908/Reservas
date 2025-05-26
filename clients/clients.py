import requests

API_PRINCIPAL_URL = "http://localhost:5036"

class PessoaServiceClient:
    @staticmethod
    def verificar_leciona(id_professor):
        url = f"{API_PRINCIPAL_URL}/professores/{id_professor}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            return data.get('professores', False)
            #if data.get('isok') else False
        except requests.RequestException as e:
            print(f"Erro ao acessar o pessoa_service: {e}")
            return False
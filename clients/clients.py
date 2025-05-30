import requests

API_PRINCIPAL_URL = "https://apischoolsystem.onrender.com/"

class PessoaServiceClient:
    @staticmethod
    def verificar_turma(id_turma):
        url = f"{API_PRINCIPAL_URL}/turmas/{id_turma}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            return data.get('turmas', False)
        except requests.RequestException as e:
            print(f"Erro ao acessar o pessoa_service: {e}")
            return False
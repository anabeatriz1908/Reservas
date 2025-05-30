# 📚 API de Reserva de Salas

Este repositório contém a **API de Reserva de Salas**, desenvolvida com **Flask** e **SQLAlchemy**, como parte de uma arquitetura baseada em **microsserviços**.

## 🧩 Arquitetura

A API de Reserva de Salas é um **microsserviço** que faz parte de um sistema maior de [School System], sendo responsável exclusivamente pelo gerenciamento das reservas de salas por turma.

⚠️ **Esta API depende de outra API de Gerenciamento Escolar (School System)**, que deve estar em execução e exposta localmente. A comunicação entre os serviços ocorre via **requisições HTTP REST**, para validar:

- Se a **Turma** existe (`GET /turmas/<id>`)

A Api de gerenciamento escolar, esá disponivél no repositório abaixo.

https://github.com/anabeatriz1908/API-School-System.git


---

## 🚀 Tecnologias Utilizadas

- Python 3.x
- Flask
- SQLAlchemy
- SQLite (como banco de dados local)
- Requests (para consumo da API externa)
- Docker

---

## ▶️ Como Executar a API

### 1. Clone o repositório

```bash
git clone https://github.com/anabeatriz1908/Reservas.git
cd Reservas
```

### 2. Crie um ambiente virtual (opcional, mas recomendado)

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute a API

```bash
python app.py
```

A aplicação estará disponível em:
📍 `http://localhost:5001`

📝 **Observação:** O banco de dados é criado automaticamente na primeira execução.

---

## 📡 Endpoints Principais

- `GET /reservas` – Lista todas as reservas
- `POST /reservas` – Cria uma nova reserva
- `GET /reservas/<id>` – Detalha uma reserva


### Exemplo de corpo JSON para criação:

```json
{
  "turma_id": 1,
  "num_sala": "101",
  "data": "2025-05-06",
  "id_turma": "2"
}
```

---

## 🔗 Dependência Externa

Certifique-se de que a **API de Gerenciamento Escolar** esteja rodando em:

```
http://localhost:5036
ou
use o link --> https://apischoolsystem.onrender.com
```

E que os endpoints de `GET /turmas/<id>` (e opcionalmente `GET /alunos/<id>`) estejam funcionando corretamente para que a validação seja feita com sucesso.

---

## 📦 Estrutura do Projeto

```
reserva-salas/
├── clients
| ├── clients.py
├── instance
| ├── reservas.db
├── main
| ├── reserva_controller.py
| ├── reserva_model.py
├── .dockerignore
├── app.py
├── config.py
├── dockerfile
├── README.md
└── requirements.txt
```

---

## 🧑‍💻 Autores

Ana Beatriz Silva Santos - RA: 2401228

Luiz Otávio Santos Silva - RA: 2401300

Murillo Rodrigues Santos Pereira - RA: 2400338

Pablo Neves Vavrik - RA: 2400125

Uatila dos Santos Silva - RA: 2400250

– Projeto educativo de arquitetura com Flask e microsserviços.

from flask import Blueprint, request, jsonify
import main.reserva_model as reserva_model
from config import db
import requests
import clients.clients as clients


reservas_blueprint = Blueprint("reservas", __name__)

@reservas_blueprint.route('/reservas', methods=[])
def validar_turma(turma_id):
    resp = requests.get(f"{clients.API_PRINCIPAL_URL}/api/turmas/{turma_id}")
    return resp.status_code == 200

@reservas_blueprint.route("/reservas", methods=["POST"])
def cria_reserva():
    dados = request.get_json()
    try:
        nova_reserva = reserva_model.create_reserva(dados)
        if isinstance(nova_reserva, dict) and nova_reserva.get("message") == "Professor não encontrado":
            return jsonify({'erro': nova_reserva["message"]}), 400
        return jsonify(nova_reserva), 200
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

@reservas_blueprint.route("/reservas", methods=["GET"])
def le_reservas():
    try:
        reservas = reserva_model.read_reservas()
        return jsonify(reservas), 200
    except Exception as e:
        return jsonify ({'erro': str(e)}), 500
    
@reservas_blueprint.route('/reservas/<int:id_reserva>', methods =['GET'])
def le_reservas_id(id_reserva):
    try:
        reserva = reserva_model.read_reserva(id_reserva)
        return jsonify(reserva), 200
    except reserva_model.ReservaNaoEncontrada:
        return jsonify({'erro': 'Reserva não encontrada.'}), 404
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

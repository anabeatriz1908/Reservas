from flask import Blueprint, request, jsonify
import main.reserva_model as reserva_model
from config import db
import requests
from clients.clients import ApiPrincipal

from config import db

reservas_blueprint = Blueprint("reservas", __name__)

@reservas_blueprint.route('/reservas', methods=[])
def validar_turma(turma_id):
    resp = requests.get(f"http://localhost:5001/api/turmas/{turma_id}")
    return resp.status_code == 200

@reservas_blueprint.route("/reservas", methods=["POST"])
def cria_reserva():
    dados = request.get_json()
    try:
        nova_reserva, erro = reserva_model.create_reserva(dados)
        if erro:
            return jsonify({'erro': erro}), 400
        return jsonify(nova_reserva), 200
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

@reservas_blueprint.route("/reservas", methods=["GET"])
def le_reservas():
    try:
        reservas, erro = reserva_model.read_reserva()
        return jsonify(reservas), 200
    except Exception as e:
        return jsonify ({'erro': str(e)}), 500
    
@reservas_blueprint.route('/reservas/<int:id_reserva>', methods =['GET'])
def le_reservas_id(id_reserva):
    try:
        reserva = reserva_model.read_reserva(id_reserva)
        return jsonify(reserva), 200
    except ReservaNaoEcontrada:
        return jsonify({'erro': 'Reserva não encontrada.'}), 404
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

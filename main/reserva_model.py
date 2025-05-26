from config import db

#importar turmas

class ReservaNaoEncontrada(Exception):
        pass

class Reservas(db.Model):
    __tablename__ = 'reservas'

    id = db.Column(db.Integer, primary_key=True)
    num_sala = db.Column(db.Integer, nullable=False)
    lab = db.Column(db.Boolean, nullable=False)
    data = db.Column(db.String(20), nullable=True)


    turma_id = db.Column(db.Integer, db.ForeignKey("turma.id"), nullable=True)
    turma = db.relationship("Turmas", back_populates="reserva")

    def __init__(self, num_sala, lab, data, turma_id):
        self.num_sala = num_sala
        self.lab = lab
        self.data = data
        self.turma_id = turma_id
    
    def to_dict(self):  
        return {
            "id": self.id,
            "num_sala":self.num_sala,
            "lab": self.lab,
            "data": self.data,
            "turma_id": self.turma_id
            }

def create_reserva(self, dados_reserva):
    
    turma = Turmas.query.get(aluno["turma_id"]) #importar turmas
    if(turma is None):
        return {"message":"Turma não existe"}
    
    nova_reserva = Reservas(
        num_sala = int(dados_reserva['num_sala']),
        lab = dados_reserva['lab'],
        data = dados_reserva['data'],
        turma_id = int(dados_reserva['turma_id'])
    )
    db.session.add(nova_reserva)
    db.session.commit()
    return{'Mensagem':'Reserva criada com sucesso'}

def read_reservas(self):
    reservas = Reservas.query.all()
    return [reserva.to_dict() for reserva in reservas]

def read_reserva(self, id_reserva):
     reserva= Reservas.query.get(id_reserva)
     
     if not reserva:
          raise ReservaNaoEncontrada(f"Reserva não encontrada.")
     return reserva.to_dict()




    

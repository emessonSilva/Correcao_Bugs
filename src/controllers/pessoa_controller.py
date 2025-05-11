from sqlalchemy.exc import IntegrityError
from models.pessoa import Pessoa
from database import db

class PessoaController:
    @staticmethod
    def salvar_pessoa(nome, sobrenome, cpf, data_nascimento):
        try:
            pessoa = Pessoa(nome=nome, sobrenome=sobrenome, 
                            cpf=cpf, data_de_nascimento=data_nascimento)
            db.session.add(pessoa)
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()  
            if 'pessoa.cpf' in str(e.orig):
                raise ValueError("CPF já cadastrado")  # corrigido: mensagem de erro ao tentar cadastrar um cpf já cadastrado
            else:
                raise ValueError("Erro ao cadastrar a pessoa: " + str(e)) 

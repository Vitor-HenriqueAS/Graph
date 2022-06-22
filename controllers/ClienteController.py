import services.database as db;
import models.Cliente as cliente;

def Incluir(cliente):
        sql = 'INSERT INTO Cliente(nome, idade, sexo, estado, telefone, email, cpf) \
        values ("%s","%s","%s","%s","%s","%s","%s")' \
        % (cliente.nome, cliente.idade, cliente.sexo, cliente.estado, cliente.telefone, \
                cliente.email, cliente.cpf)
        
        db.cursor_cliente.execute(sql)
        db.conexao_cliente.commit()

def SelecionarTodos():
        sql = 'SELECT * FROM Cliente'

        db.cursor_cliente.execute(sql)
        costumerList = []

        for row in db.cursor_cliente.fetchall():
                costumerList.append(cliente.Cliente(row[0], row[1], row[2], row[3], row[4], \
                        row[5], row[6], row[7]))

        return costumerList

def SelecionaID(id):
        global x

        db.cursor_cliente.execute('SELECT * FROM Cliente WHERE id = %s' % id)
        x = db.cursor_cliente.fetchall()

        return x

def Excluir(id):
        sql = 'DELETE FROM Cliente WHERE id = %s' \
        % id

        db.cursor_cliente.execute(sql)
        db.conexao_cliente.commit()

def Alterar(cliente):
       
        sql = f'UPDATE Cliente SET \
        nome = "{cliente.nome}", idade = "{cliente.idade}", sexo = "{cliente.sexo}", estado = "{cliente.estado}",\
        telefone = "{cliente.telefone}", email = "{cliente.email}", cpf = "{cliente.cpf}"\
        WHERE id = {cliente.id}'

        db.cursor_cliente.execute(sql)
        db.conexao_cliente.commit()
        return True
                
        

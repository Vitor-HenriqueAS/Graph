import services.database as db;
import models.Estoque as estoque;

def Incluir(produto):
        sql = 'INSERT INTO Estoque(nome, marca, categoria, valor, quantidade) \
        values ("%s","%s","%s","%s","%s")' \
        % (produto.nome, produto.marca, produto.categoria, produto.valor, produto.quantidade)
        
        db.cursor_estoque.execute(sql)
        db.conexao_estoque.commit()

def SelecionarTodos():
        sql = 'SELECT * FROM Estoque'

        db.cursor_estoque.execute(sql)
        costumerList = []

        for row in db.cursor_estoque.fetchall():
                costumerList.append(estoque.Estoque(row[0], row[1], row[2], row[3], row[4], row[5]))

        return costumerList

def SelecionaID(id):
        global x

        db.cursor_estoque.execute('SELECT * FROM Estoque WHERE id = %s' % id)
        x = db.cursor_estoque.fetchall()

        return x

def Excluir(id):
        sql = 'DELETE FROM Estoque WHERE id = %s' \
        % id

        db.cursor_estoque.execute(sql)
        db.conexao_estoque.commit()

def Alterar(produto):
       
        sql = f'UPDATE Estoque SET \
        nome = "{produto.nome}", marca = "{produto.marca}", categoria = "{produto.categoria}",\
        valor = "{produto.valor}", quantidade = "{produto.quantidade}"\
        WHERE id = {produto.id}'

        db.cursor_estoque.execute(sql)
        db.conexao_estoque.commit()
        return True
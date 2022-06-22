import services.database as db

def incluir(usuario):
  db.cursor_login.execute("""
  INSERT INTO CadastroLogin 
  (nome, telefone, email, cpf, senha)
  values("%s", "%s", "%s", "%s", "%s")""" % 
  (usuario.nome, usuario.telefone, usuario.email, usuario.cpf , usuario.senha))
  db.conexao_cadastro.commit()

def login(dados):
  try:
    db.cursor_login.execute("SELECT senha FROM CadastroLogin WHERE email = '{}'".format(dados.email))
    senha_db = db.cursor_login.fetchall()

    if dados.senha == senha_db[0][0]:
      return True
  except:
    return False
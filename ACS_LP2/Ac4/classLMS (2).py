class Usuario:
    def __init__(self,ID,login_usuario,senha,DtExpiracao):
        self.ID = ID
        self.login_usuario = login_usuario
        self.__senha = senha
        self.DtExpiracao = DtExpiracao
    def __str__(self):       
        return f"Informações do Usuario login: {self.login} senha: {self.senha}"

class Coordenador:
    def __init__(self,ID,IDCoordenador,Nome,Email,Celular):
        self.ID = ID
        self.IDCoordenador = IDCoordenador
        self.Nome = Nome
        self.Email = Email
        self.Celular = Celular
    def __str__(self):
    return f"Informações do Coord: nome {self.nome}, \n {self.usuario}"

class Aluno:
    def __init__(self,ID,IDAluno,Nome,Email,Celular,RA,Foto):
        self.ID = ID
        self.IDAluno = IDAluno
        self.Nome = Nome
        self.Email = Email
        self.Celular = Celular
        self.RA = RA
        self.Foto= Foto

class Professor:
    def __init__(self,ID,IDProfessor,Email,Celular,Apelido):
        self.ID = ID
        self.IDProfessor = IDProfessor
        self.Email = Email
        self.Celular = Celular
        self.Apelido = Apelido

class Disciplina:
    def __init__(self,ID,Nome,Data_Discipina,Status_Disciplina,PlanoDeEnsino,CargaHoraria,Competencias,
                 Habilidades,Ementa,ConteudoProgramatico,BibliografiaBasica,BibliografiaComplementar,
                 PercentualPratico,PercentualTeorico,IDCoordenador):
        self.ID = ID
        self.Nome = Nome
        self.Data_Disciplina = Data_Disciplina
        self.Status_Disciplina = Status_Disciplina
        self.PlanoDeEnsino = PlanoDeEnsino 
        self.CargaHorario = CargaHoraria
        self.Competencias = Competencias
        self.Habilidades = Habilidaes
        self.Ementa = Ementa
        self.ConteudoProgramatico = ConteudoProgramatico
        self.BibliografiaBasica = BibliografiaBasica
        self.BibliografiaComplementar = BibliografiaComplementar
        self.PercentualPratico = PercentualPratico
        self.PercentualTeorico = PercentualTeorico
        self.IDCoordenador = IDCoordenador

class DisciplinaOfertada:
    def __init__(self,ID,IDCoordenador,DtInicioMatricula,DtFimMatricula,IDDisciplina,IDCurso,Ano,Semestre,Turma,IDProfessor,Metodologia,Recursos,CriterioAvaliacao,PlanoDeAulas):
        self.ID = ID
        self.IDCoordenador = IDCoordenador
        self.DtInicioMatricula = DtInicioMatricula
        self.DtFimMatricula = DtFimMatricula
        self.IDDisciplina = IDDisciplina
        self.IDCurso = IDCurso 
        self.Ano = Ano
        self.Semestre = Semestre
        self.Turma = Turma
        self.IDProfessor = IDProfessor
        self.Metodologia = Metodologia
        self.Recursos = Recursos
        self.CriterioAvaliacao = CriterioAvaliacao
        self.PlanoDeAulas = PlanoDeAulas
        
class Curso:
    def __init__(self,ID,Nome):
        self.ID = ID
        self.Nome = Nome

class SolicitacaoMatricula:
    def __init__(self,ID,IDAluno,IDDisciplinaOfertada,DtSolicitacao,IDCoordenador,Status_SM):
        self.ID = ID
        self.IDAluno = IDAluno
        self.IDDisciplinaOfertada = IDDisciplinaOfertada
        self.DtSolicitacao = DtSolicitacao
        self.IDCoordenador = IDCoordenador
        self.Status_SM = Status_SM

class Atividade:
    def __init__(self,ID,Titulo,Descricao,Conteudo,Tipo,Extras,IDProfessor):
        self.ID = ID
        self.Titulo = Titulo
        self.Descricao = Descricao
        self.Conteudo = Conteudo
        self.Tipo = Tipo
        self.Extras = Extras
        self.IDProfessor = IDProfessor

class AtividadeVinculada:
    def __init__(self,ID,IDAtividade,IDProfessor,IDDisciplinaOfertada,Rotulo,Status_AtividadeVinculada,DtInicioRespostas,DtFimRespostas):
        self.ID = ID
        self.IDAtividade = IDAtividade
        self.IDProfessor = IDProfessor
        self.IDDisciplinaOfertada = IDDisciplinaOfertada
        self.Rotulo = Rotulo
        self.Status_AtividadeVinculada = Status_AtividadeVinculada
        self.DtInicioRespostas = DtInicioRespostas
        self.DtFimRespostas = DtFimRespostas
        
class Entrega:
    def __init__(self,ID,IDAluno,IDAtividadeViculada,Titulo,Resposta,DtEntrega,Status_Entrega,IDProfessor,Nota_Entrega,DtAvaliacao,Obs_Entrega):
        self.ID = ID
        self.IDAluno = IDAluno
        self.IDAtividadeViculada = IDAtividadeViculada
        self.Titulo = Titulo
        self.Resposta = Resposta
        self.DtEntrega = DtEntrega
        self.Status_Entrega = Status_Entrega
        self.IDProfessor = IDProfessor
        self.Nota_Entrega = Nota_Entrega
        self.DtAvaliacao = DtAvaliacao
        self.Obs_Entrega = Obs_Entrega
                
class Mensagem:
    def __init__(self,ID,IDAluno,IDProfessor,Assunto,Referencia,Conteudo,Status_Mensagem,DtEnvio,DtResposta,Resposta):
        self.ID = ID
        self.IDAluno = IDAluno
        self.IDProfessor = IDProfessor
        self.Assunto = Assunto
        self.Referencia = Referencia
        self.Conteudo = Conteudo
        self.Status_Mensagem = Status_Mensagem
        self.DtEnvio = DtEnvio
        self.DtResposta = DtResposta
        self.Resposta = Resposta

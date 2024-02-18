from classes.banco import Banco

class Inscricao:
    def __init__(self):
        self.__ins_cod = 0
        self.__ins_telefone = ''
        self.__ins_nome = ''
        self.__ins_curso = ''
        self.__ins_email = ''
        self.__ins_cpf = ''

        self.__banco = Banco()

    def set_ins_cod(self, pid):
        if pid > 0:
            self.__ins_cod = pid

    def set_ins_telefone(self, ptele):
        # Ajuste para verificar se ptele é um valor válido antes de atribuir
        if ptele and len(str(ptele)) > 0:
            self.__ins_telefone = str(ptele)

    def set_ins_cpf(self, pcpf):
        # Ajuste para verificar se pcpf é um valor válido antes de atribuir
        if pcpf and len(str(pcpf)) > 0:
            self.__ins_cpf = str(pcpf)

    def set_ins_nome(self, pnome):
        # Ajuste para verificar se pnome é um valor válido antes de atribuir
        if pnome and len(pnome) > 0:
            self.__ins_nome = pnome

    def set_ins_email(self, pemail):
        # Ajuste para verificar se pemail é um valor válido antes de atribuir
        if pemail and len(pemail) > 0:
            self.__ins_email = pemail

    def set_ins_curso(self, pcurso):
        # Ajuste para verificar se pcurso é um valor válido antes de atribuir
        if pcurso and len(pcurso) > 0:
            self.__ins_curso = pcurso

    # Os métodos get permanecem inalterados

    def obterInscricao(self):
        sql = '''
            SELECT ins_cod, ins_telefone, ins_nome, ins_curso, ins_email, ins_cpf
            FROM inscricao
            ORDER BY ins_cod
        '''
        return self.__banco.executarSelect(sql)

    def gravar(self):
        sql = '''
            INSERT INTO inscricao (ins_telefone, ins_nome, ins_curso, ins_email, ins_cpf)
            VALUES ("#ins_telefone", "#ins_nome", "#ins_curso", "#ins_email", "#ins_cpf")
        '''
        sql = sql.replace('#ins_telefone', self.__ins_telefone)
        sql = sql.replace('#ins_nome', self.__ins_nome)
        sql = sql.replace('#ins_curso', self.__ins_curso)
        sql = sql.replace('#ins_email', self.__ins_email)
        sql = sql.replace('#ins_cpf', self.__ins_cpf)

        return self.__banco.executarInsertUpdateDelete(sql)

    def excluir(self):
        sql = 'delete from inscricao where ins_cod = #id'
        sql = sql.replace('#id', str(self.__ins_cod))
        return self.__banco.executarInsertUpdateDelete(sql)



import abc

from constantes import MAX_SIZE, MIN_SIZE


class FilaBase(metaclass=abc.ABCMeta):
    codigo: int = 0
    fila = []
    clientes_atendidos = []
    senha_atual = None

    def reseta_fila(self) -> None:
        if self.codigo >= MAX_SIZE:
            self.codigo = MIN_SIZE
        else:
            self.codigo += 1

    @abc.abstractmethod
    def chama_cliente(self, caixa):
        ...

    @abc.abstractmethod
    def estatistic(self, dia, agencia, flag):
        ...

    @abc.abstractmethod
    def atualiza_fila(self):
        ...

    def insere_cliente(self) -> None:
        self.fila.append(self.senha_atual)

    def gera_senhas(self):
        self.busca_posicao_fila()
        self.gera_senha_atual()
        self.insere_cliente()
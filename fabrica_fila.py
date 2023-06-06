from constantes import TIPO_FILA_NORMAL, TIPO_FILA_PRIORITARIA
from fila_prioritaria import FilaPrioritaria


class FabricaFila:
    @staticmethod
    def pega_fila(tipo_fila):
        if tipo_fila == TIPO_FILA_PRIORITARIA:
            return FilaPrioritaria()
        # elif tipo_fila == TIPO_FILA_NORMAL:
        #     return FilaNormal()
        else:
            raise NotImplementedError("Tipo não cadastrado")

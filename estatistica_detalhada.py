from typing import List


class EstatisticaDetalhada:
    def __init__(self, dia: str, agencia: int) -> None:
        self.dia = dia
        self.agencia = agencia

    def roda_estatistica(self, clientes_atendidos: List[str]) -> dict:
        estatistica = {}
        estatistica['dia'] = self.dia
        estatistica['agencia'] = self.agencia
        estatistica['clientes_atendidos'] = clientes_atendidos
        estatistica['quantidade_de_clientes_atendidos'] = (
            len(clientes_atendidos)
        )

        return estatistica

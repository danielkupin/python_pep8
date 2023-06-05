from fila_prioritaria import FilaPrioritaria

fila_teste = FilaPrioritaria()
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()
print(fila_teste.chama_cliente(10))
print(fila_teste.chama_cliente(1))
print(fila_teste.estatistica('05/03/2023', '001', 'detail'))

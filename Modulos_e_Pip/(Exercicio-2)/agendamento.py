import os
import time

def agendamento():
    # obter tempo atual
    tempo_atual = time.time()
    # Calcular o tempo de desligamento (uma hora depois do tempo atual)
    tempo_desligamento = tempo_atual + 3600 # 3600 segundos = 1 hora
    # Converter o tempo de desligamento para um formato aceitavel pelo comando
    tempo_formatado = time.strftime("%H:%M:%S", time.localtime(tempo_desligamento))
    comando = f"shutdown -h {tempo_formatado}"
    os.system(comando)

    print(f"O tempo de desligamento será de: {tempo_formatado}")

def agendar_desligamento():
    tempo_atual = time.time()
    tempo_desligamento = tempo_atual + 1800 # 1800 = meia hora
    tempo_formatado = time.strftime("%H:%M:%S", time.localtime(tempo_desligamento))
    comando = f"shutdown -h {tempo_formatado}"
    os.system(comando)
    print(f"O tempo de desligamento será de: {tempo_formatado}")


def cancelar_agendamento_desligamento():
    # Comando para cancelar o agendamento de desligamento
    if os.name == 'nt':  # Verifica se é Windows
        comando = "shutdown -a"
    else:  # Assume Linux/Mac
        comando = "sudo shutdown -c"

    # Executar o comando para cancelar o agendamento
    os.system(comando)

    print("Agendamento de desligamento cancelado.")

# Exemplos de uso das funções
agendar_desligamento()
agendamento()
cancelar_agendamento_desligamento()

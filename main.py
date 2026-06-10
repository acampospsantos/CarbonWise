"""
MÓDULO: main.py
RESPONSÁVEL: Pessoa 1 (Integração e Menu - Maestro/a)

Arquivo principal de execução do sistema CarbonWise.
Este arquivo configura o caminho de importação e inicia o loop do menu principal.
"""

import sys
import os

# Adiciona o diretório raiz ao path do Python para permitir importações relativas e absolutas
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from views.menu_view import *
# Importação dos controladores e views desenvolvidos pelos outros membros
from controllers.empresa_controller import (
    cadastrar_empresa,   # Desenvolvido pela Pessoa 3
    registrar_consumo,   # Desenvolvido pela Pessoa 4
    atualizar_frota,     # Desenvolvido pela Pessoa 6
    excluir_empresa      # Desenvolvido pela Pessoa 6
)

def main():
    """
    Função principal que inicia a aplicação.
    """

    # Chama o menu principal estruturado pela Pessoa 1
    while True:
        exibir_opcoes_do_menu()
        opcao = input("Escolha uma opção: ")
        if opcao == "1": 
            cnpj_empresa = input('CNPJ da empresa: ')
            nome_empresa = input('Nome da empresa: ')
            qtd_frota = input('Digite a quantidade de veiculos da frota: ')
            
            cadastrar_empresa(cnpj_empresa, nome_empresa, qtd_frota) #Chamada da funcao cadastrar empresa
            
        elif opcao == "2":
            beneficiosAplicacao()
            
        elif opcao == "3":
            cnpj_empresa = input('CNPJ da empresa: ')
            consumo_combustivel = input('Consumo combustível em L: ')
            consumo_energia = input('Consumo de energia elétrica em kWh: ')
            
            registrar_consumo(cnpj_empresa, consumo_combustivel, consumo_energia) 
            
        elif opcao == "4":
            cnpj_empresa = input('CNPJ da empresa: ')
            nova_frota = input('Valor da nova frota: ')
            
            atualizar_frota(cnpj_empresa, nova_frota)
            
        elif opcao == "5":
            cnpj_empresa = input('CNPJ da empresa: ')
            
            excluir_empresa(cnpj_empresa)
            
        elif opcao == "0":
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nSistema encerrado pelo usuário.")
        print("Fim do programa...")
        sys.exit(0)
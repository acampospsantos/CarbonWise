"""
MÓDULO: views/menu_view.py
RESPONSÁVEL: Pessoa 1 (Integração e Menu - Maestro/a)

Este módulo é responsável pela interface do menu principal em linha de comando (CLI).
Ele gerencia o fluxo de execução do programa, apresentando opções para o usuário,
capturando as escolhas e delegando para os respectivos controladores e relatórios.
"""

# Importação dos controladores e views desenvolvidos pelos outros membros
from controllers.empresa_controller import (
    cadastrar_empresa,   # Desenvolvido pela Pessoa 3
    registrar_consumo,   # Desenvolvido pela Pessoa 4
    atualizar_frota,     # Desenvolvido pela Pessoa 6
    excluir_empresa      # Desenvolvido pela Pessoa 6
)
from views.relatorio_view import gerar_relatorio  # Desenvolvido pela Pessoa 5


def menu_principal():
    """
    Função da Pessoa 1: Exibe o menu principal no console e gerencia a navegação.
    """
    while True:
        print("=" * 60)
        print(" CARBONWISE - SISTEMA DE INVENTÁRIO DE CO2 ".center(60, "="))
        print("=" * 60)
        print("  [1] Cadastrar Empresa")
        print("  [2] Registrar Consumo (Combustível & Energia)")
        print("  [3] Atualizar Frota de Veículos")
        print("  [4] Excluir Empresa")
        print("  [5] Gerar Relatório de Emissões")
        print("  [0] Sair")
        print("=" * 60)
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            print("\n--- CADASTRO DE EMPRESA ---")
            cnpj = input("CNPJ: ").strip()
            nome = input("Razão Social/Nome Fantasia: ").strip()
            frota = input("Quantidade de veículos na frota: ").strip()
            sucesso = cadastrar_empresa(cnpj, nome, frota)
            if sucesso:
                print("Sucesso: Empresa cadastrada com êxito!")
            else:
                print("Erro ao cadastrar empresa. Verifique as mensagens acima.")
            print()
            
        elif opcao == "2":
            print("\n--- REGISTRO DE CONSUMO ---")
            cnpj = input("CNPJ da empresa: ").strip()
            litros = input("Consumo de Combustível (Litros): ").strip()
            kwh = input("Consumo de Energia Elétrica (kWh): ").strip()
            sucesso = registrar_consumo(cnpj, litros, kwh)
            if sucesso:
                print("Sucesso: Consumo registrado com êxito!")
            else:
                print("Erro ao registrar consumo. Verifique as mensagens acima.")
            print()
            
        elif opcao == "3":
            print("\n--- ATUALIZAR FROTA ---")
            cnpj = input("CNPJ da empresa: ").strip()
            nova_frota = input("Nova quantidade de veículos: ").strip()
            sucesso = atualizar_frota(cnpj, nova_frota)
            if sucesso:
                print("Sucesso: Frota atualizada com êxito!")
            else:
                print("Erro ao atualizar frota. Verifique as mensagens acima.")
            print()
            
        elif opcao == "4":
            print("\n--- EXCLUIR EMPRESA ---")
            cnpj = input("CNPJ da empresa a ser excluída: ").strip()
            confirmacao = input(f"Tem certeza que deseja excluir a empresa de CNPJ {cnpj}? (S/N): ").strip().upper()
            if confirmacao == "S":
                sucesso = excluir_empresa(cnpj)
                if not sucesso:
                    print("Erro ao excluir empresa.")
            else:
                print("Operação cancelada pelo usuário.")
            print()
            
        elif opcao == "5":
            print("\n--- GERAR RELATÓRIO ---")
            cnpj = input("CNPJ da empresa: ").strip()
            gerar_relatorio(cnpj)
            print()
            
        elif opcao == "0":
            print("\nEncerrando o sistema CarbonWise. Obrigado!")
            break
        else:
            print("\nOpção inválida! Escolha um número correspondente às opções do menu.\n")

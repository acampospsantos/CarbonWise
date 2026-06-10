"""
MÓDULO: views/relatorio_view.py
RESPONSÁVEL: Pessoa 5 (Relatórios - Read)

Este módulo é responsável por exibir os relatórios de emissões das empresas.
É o componente mais visual e focado em apresentação de dados para o usuário.
"""

from database.db import banco_dados
from controllers.calculadora_controller import calcular_co2  # Desenvolvido pela Pessoa 2
from utils.validators import limpar_cnpj


def gerar_relatorio(cnpj: str):
    """
    Função da Pessoa 5: Gera e imprime na tela o relatório detalhado de emissões de uma empresa.
    
    Parâmetros:
        cnpj (str): CNPJ da empresa cujo relatório deve ser gerado.
    """
    cnpj_limpo = limpar_cnpj(cnpj)
    
    try:
        empresa = banco_dados[cnpj_limpo]
    except KeyError:
        print("\n" + "=" * 60)
        print("  ERRO: CNPJ NÃO ENCONTRADO  ".center(60, "!"))
        print("=" * 60)
        print(f"Não encontramos nenhuma empresa cadastrada com o CNPJ: {cnpj}")
        print("=" * 60 + "\n")
        return

    # CNPJ Formatado para exibição: XX.XXX.XXX/XXXX-XX
    if len(cnpj_limpo) == 14:
        cnpj_fmt = f"{cnpj_limpo[0:2]}.{cnpj_limpo[2:5]}.{cnpj_limpo[5:8]}/{cnpj_limpo[8:12]}-{cnpj_limpo[12:14]}"
    else:
        cnpj_fmt = cnpj_limpo

    print("\n" + "=" * 65)
    print(" CARBONWISE - RELATÓRIO DE EMISSÕES DE CO2 ".center(65, "="))
    print("=" * 65)
    print(f"  Razão Social: {empresa['nome']}")
    print(f"  CNPJ:         {cnpj_fmt}")
    print(f"  Frota Ativa:  {empresa['frota']} veículo(s)")
    print("=" * 65)
    
    consumos = empresa.get("consumos", [])
    if not consumos:
        print("  Sem registros de consumo cadastrados para esta empresa.".center(65))
        print("=" * 65 + "\n")
        return

    print("  HISTÓRICO DE CONSUMOS E EMISSÕES".center(65))
    print("-" * 65)
    print(f"  {'Medição':<10} | {'Combustível (L)':<16} | {'Energia (kWh)':<14} | {'CO2 (tCO2e)':<12}")
    print("-" * 65)
    
    total_litros = 0.0
    total_kwh = 0.0
    total_co2 = 0.0
    
    for i, consumo in enumerate(consumos, 1):
        litros = consumo["litros"]
        kwh = consumo["kwh"]
        co2 = calcular_co2(litros, kwh)
        
        total_litros += litros
        total_kwh += kwh
        total_co2 += co2
        
        print(f"  {f'#{i}':<10} | {litros:<16.2f} | {kwh:<14.2f} | {co2:<12.4f}")
        
    print("-" * 65)
    print(f"  {'TOTAL':<10} | {total_litros:<16.2f} | {total_kwh:<14.2f} | {total_co2:<12.4f}")
    print("=" * 65)
    print(f"  Pegada de Carbono Acumulada: {total_co2:.4f} tCO2e".center(65))
    print("=" * 65 + "\n")

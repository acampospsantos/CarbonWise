# -*- coding: utf-8 -*-
"""
MÓDULO: views/relatorio_view.py
RESPONSÁVEL: Pessoa 5 (Relatórios - Read)
"""

from database.db import banco_dados
from controllers.calculadora_controller import calcular_co2


def gerar_relatorio(cnpj: str):
    try:
        empresa = banco_dados[cnpj]
        total_co2_empresa = 0.0

        print("\n==============================================")
        print("         RELATÓRIO DE EMISSÕES ESG           ")
        print("==============================================")
        print(f"Empresa: {empresa['nome']}")
        print(f"CNPJ:    {cnpj}")
        print(f"Frota:   {empresa['frota']} veículos")
        print("----------------------------------------------")
        print("Histórico de Consumos Registrados:")

        if not empresa["consumos"]:
            print("   [Nenhum consumo registrado até o momento.]")
        else:
            for indice, consumo in enumerate(empresa["consumos"], start=1):
                litros = consumo["litros"]
                kwh = consumo["kwh"]

                co2_item = calcular_co2(
                    kwh_energia=kwh,
                    litros_combustivel=litros,
                    km_transporte=0.0,
                    kg_residuos=0.0,
                    litros_agua=0.0
                )

                total_co2_empresa += co2_item

                print(f"  Medição #{indice}: {litros}L | {kwh} kWh")
                print(f"  -> Emissão: {co2_item:.4f} tCO2e")
                print("  - - - - - - - - - - - - - - - - - - - - - -")

        print("----------------------------------------------")
        print(f" TOTAL ACUMULADO DE EMISSÕES: {total_co2_empresa:.4f} tCO2e")
        print("==============================================")

    except KeyError:
        print(f"\nErro: A empresa com o CNPJ '{cnpj}' não foi encontrada.")
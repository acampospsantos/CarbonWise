# -*- coding: utf-8 -*-
"""
MÓDULO: controllers/calculadora_controller.py
RESPONSÁVEL: Pessoa 2 (Motor de Cálculo)

Ficará responsável pela regra de negócio matemática de conversão.
O desafio é garantir que a conversão de litros e kWh para toneladas de carbono (tCO2e)
esteja exata e pronta para ser chamada por outras funções (como a de Relatórios da Pessoa 5).
"""

def calcular_co2(litros_combustivel: float, kwh_energia: float) -> float:
    """
    Realiza o cálculo de emissões de CO2 equivalentes em toneladas.
    
    Parâmetros:
        litros_combustivel (float): Quantidade de litros consumidos.
        kwh_energia (float): Quantidade de energia consumida em kWh.
        
    Retorna:
        float: Total de CO2 emitido em toneladas (tCO2e).
        
    Observações para a Pessoa 2:
        - Pesquise ou utilize os fatores de emissão oficiais (ex: fator de emissão da gasolina/diesel 
          e o fator médio de emissão do grid elétrico brasileiro - SIN).
        - Exemplo fictício de fatores para estruturação (você deve validar/ajustar):
          * Gasolina: ~2.3 kg CO2 por litro
          * Eletricidade: ~0.1 kg CO2 por kWh
          * Lembre-se de converter o resultado final de kg para toneladas (dividir por 1000).
    """
    fator_combustivel = 2.3  # kg CO2 por litro
    fator_energia = 0.1      # kg CO2 por kWh
    
    emissao_litros = litros_combustivel * fator_combustivel
    emissao_kwh = kwh_energia * fator_energia
    
    total_toneladas = (emissao_litros + emissao_kwh) / 1000
    return total_toneladas

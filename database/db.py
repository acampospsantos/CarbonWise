# -*- coding: utf-8 -*-
"""
MÓDULO: database/db.py
RESPONSÁVEL: Pessoa 1 (Integração e Menu - Maestro/a)

Este arquivo inicializa a estrutura de dados global (banco de dados em memória)
que será utilizada por todo o sistema para armazenar as informações das empresas
e seus respectivos consumos.
"""

# Estrutura global do banco de dados (Dicionário)
# Exemplo de estrutura que será populada pelas outras funções:
# banco_dados = {
#     "12.345.678/0001-90": {
#         "nome": "Empresa Exemplo Ltda",
#         "frota": 5,  # Número inteiro de veículos (Pessoa 3)
#         "consumos": [  # Lista de consumos inserida pela Pessoa 4
#             {"litros": 150.0, "kwh": 500.0},
#             {"litros": 200.0, "kwh": 450.0}
#         ]
#     }
# }
# Banco de dados inicializado com uma empresa fictícia para fins de demonstração
banco_dados = {
    "12345678000195": {
        "nome": "EcoTransportes S.A.",
        "frota": 12,
        "consumos": [
            {"litros": 1500.0, "kwh": 4200.0},
            {"litros": 1350.0, "kwh": 3900.0},
            {"litros": 1600.0, "kwh": 4500.0}
        ]
    }
}

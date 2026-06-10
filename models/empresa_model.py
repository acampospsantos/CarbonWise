"""
MÓDULO: models/empresa_model.py
RESPONSÁVEIS: Equipe (Orientado pela Pessoa 1 e Pessoa 3)

Este arquivo descreve a estrutura de dados (modelo conceitual) que representa
uma Empresa no sistema CarbonWise.
Como utilizaremos um banco de dados em memória à base de dicionários,
este arquivo serve como documentação de referência e tipagem para as outras funções.
"""

# Definição do schema esperado de uma empresa dentro do dicionário global
EMPRESA_SCHEMA_EXEMPLO = {
    "cnpj_chave": {  # Tipo: str (Chave principal do dicionário banco_dados)
        "nome": str,       # Razão Social ou Nome Fantasia da empresa
        "frota": int,      # Número de veículos ativos (cadastrado por Pessoa 3, atualizado por Pessoa 6)
        "consumos": [      # Lista de consumos contendo histórico de medições (populado por Pessoa 4)
            {
                "litros": float,  # Consumo de combustível em litros
                "kwh": float     # Consumo de energia elétrica em kWh
            }
        ]
    }
}

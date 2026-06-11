# -*- coding: utf-8 -*-
"""
MÓDULO: controllers/empresa_controller.py
RESPONSÁVEIS: Pessoa 3 (Cadastro), Pessoa 4 (Registrar Consumo) e Pessoa 6 (Manutenção)

Este controlador gerencia todas as operações de manipulação de dados das empresas
cadastradas no dicionário global.
"""

from database.db import banco_dados
from utils.validators import limpar_cnpj, validar_cnpj_formato

# ==============================================================================
# PESSOA 3: Cadastro Inicial (Create)
# ==============================================================================
def cadastrar_empresa(cnpj: str, nome: str, frota_str: str) -> bool:
    """
    Função da Pessoa 3: Cadastra uma nova empresa no dicionário 'banco_dados'.
    
    Parâmetros:
        cnpj (str): O CNPJ que servirá como chave única no dicionário.
        nome (str): Nome fantasia da empresa.
        frota_str (str): Quantidade de veículos da frota (recebido como texto do input).
        
    Retorna:
        bool: True se cadastrada com sucesso, False caso contrário.
    """
    cnpj_limpo = limpar_cnpj(cnpj)
    
    if not validar_cnpj_formato(cnpj_limpo):
        print("Erro: O CNPJ fornecido é inválido.")
        return False
        
    if cnpj_limpo in banco_dados:
        print("Erro: Uma empresa com este CNPJ já está cadastrada.")
        return False
        
    try:
        frota_int = int(frota_str)
        if frota_int < 0:
            print("Erro: A quantidade de veículos na frota não pode ser negativa.")
            return False
    except ValueError:
        print("Erro: A frota de veículos deve ser um número inteiro válido.")
        return False
        
    banco_dados[cnpj_limpo] = {
        "nome": nome,
        "frota": frota_int,
        "consumos": []
    }
    print(f"Empresa {nome} cadastrada com sucesso!\n")
    return True


# ==============================================================================
# PESSOA 4: Entrada de Dados / Registrar Consumo (Create)
# ==============================================================================
def registrar_consumo(cnpj: str, litros_str: str, kwh_str: str) -> bool:
    """
    Função da Pessoa 4: Adiciona uma medição de consumo na lista de consumos da empresa.
    
    Parâmetros:
        cnpj (str): CNPJ da empresa que está registrando o consumo.
        litros_str (str): Consumo de combustível em litros (recebido como texto).
        kwh_str (str): Consumo de energia elétrica em kWh (recebido como texto).
        
    Retorna:
        bool: True se o consumo foi registrado com sucesso, False caso contrário.
    """
    cnpj_limpo = limpar_cnpj(cnpj)
    
    if cnpj_limpo not in banco_dados:
        print("Erro: Empresa não encontrada para o CNPJ fornecido.")
        return False
        
    try:
        litros_float = float(litros_str)
        kwh_float = float(kwh_str)
        if litros_float < 0 or kwh_float < 0:
            print("Erro: Os valores de consumo de combustível e energia não podem ser negativos.")
            return False
    except ValueError:
        print("Erro: Os valores de consumo devem ser números válidos.")
        return False
        
    banco_dados[cnpj_limpo]["consumos"].append({
        "litros": litros_float,
        "kwh": kwh_float
    })
    print("Sucesso: Registro de consumo realizado com sucesso.")
    return True


# ==============================================================================
# PESSOA 6: Manutenção (Update / Delete)
# ==============================================================================
def atualizar_frota(cnpj: str, nova_frota_str: str) -> bool:
    """
    Função da Pessoa 6: Atualiza o número de veículos na frota de uma empresa existente.
    
    Parâmetros:
        cnpj (str): CNPJ da empresa.
        nova_frota_str (str): Nova quantidade de veículos (recebido como texto).
        
    Retorna:
        bool: True se atualizado com sucesso, False caso contrário.
    """
    cnpj_limpo = limpar_cnpj(cnpj)
    
    if cnpj_limpo not in banco_dados:
        print("Erro: Empresa não encontrada para o CNPJ fornecido.")
        return False
        
    try:
        nova_frota_int = int(nova_frota_str)
        if nova_frota_int < 0:
            print("Erro: A quantidade de veículos na frota não pode ser negativa.")
            return False
    except ValueError:
        print("Erro: A frota de veículos deve ser um número inteiro válido.")
        return False
        
    banco_dados[cnpj_limpo]["frota"] = nova_frota_int
    print("Sucesso: Atualização da frota realizada com sucesso.")
    return True


def excluir_empresa(cnpj: str) -> bool:
    """
    Função da Pessoa 6: Remove uma empresa do dicionário de forma segura.
    
    Parâmetros:
        cnpj (str): CNPJ da empresa a ser excluída.
        
    Retorna:
        bool: True se excluída com sucesso, False caso contrário.
    """
    cnpj_limpo = limpar_cnpj(cnpj)
    
    if cnpj_limpo not in banco_dados:
        print("Erro: Empresa não encontrada para o CNPJ fornecido.")
        return False
        
    banco_dados.pop(cnpj_limpo)
    print("Sucesso: Empresa removida com sucesso.")
    return True

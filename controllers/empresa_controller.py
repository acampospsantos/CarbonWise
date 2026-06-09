# -*- coding: utf-8 -*-
"""
MÓDULO: controllers/empresa_controller.py
RESPONSÁVEIS: Pessoa 3 (Cadastro), Pessoa 4 (Registrar Consumo) e Pessoa 6 (Manutenção)

Este controlador gerencia todas as operações de manipulação de dados das empresas
cadastradas no dicionário global.
"""

from database.db import banco_dados

# ==============================================================================
# PESSOA 3: Cadastro Inicial (Create)
# ==============================================================================
def cadastrar_empresa(cnpj: str, nome: str, frota_str: str) -> bool:
    
    print("\n===== CADASTRO DE EMPRESA =====")
    cnpj = input("Digite o CNPJ da empresa: ").strip()
    
    if cnpj in banco_dados:
        print(f"Erro: CNPJ '{cnpj}' já cadastrado.")
        return False

    if not cnpj:
        print("Erro: CNPJ não pode ser vazio.")
        return

    nome = input("Digite o nome fantasia da empresa: ").strip()

    if not nome:
        print("Erro: Nome não pode ser vazio.")
        return

    frota_str = input("Digite a quantidade de veículos da frota: ").strip()
    try:
        frota = int(frota_str)
    except ValueError:
        print(f"Erro: '{frota_str}' não é um número inteiro válido para a frota.")
        return False

    sucesso = cadastrar_empresa(cnpj, nome, frota_str)

    if sucesso:
        print(f"\n✔ Cadastro realizado com sucesso!")
        print(f"   CNPJ  : {cnpj}")
        print(f"   Nome  : {nome}")
        print(f"   Frota : {frota_str} veículos")
    else:
        print("\n✘ Cadastro não realizado. Verifique os erros acima.")
    

    banco_dados[cnpj] = {
        "nome": nome,
        "frota": frota_str,
        "consumos": []
    }



    """
    Função da Pessoa 3: Cadastra uma nova empresa no dicionário 'banco_dados'.
    
    Parâmetros:
        cnpj (str): O CNPJ que servirá como chave única no dicionário.
        nome (str): Nome fantasia da empresa.
        frota_str (str): Quantidade de veículos da frota (recebido como texto do input).
        
    Retorna:
        bool: True se cadastrada com sucesso, False caso contrário.
        
    Desafios/Foco Técnico para Pessoa 3:
        1. Utilizar bloco try-except para converter 'frota_str' para um número inteiro.
           Se falhar (ValueError), exibir mensagem de erro e não cadastrar.
        2. Evitar o cadastro de CNPJs duplicados. Verificar se o 'cnpj' já existe
           como chave no dicionário 'banco_dados'.
        3. Criar a estrutura interna da empresa (ex: dicionário com chaves 'nome',
           'frota' e uma lista vazia de 'consumos').
    """
    


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
        
    Desafios/Foco Técnico para Pessoa 4:
        1. Tratar exceções (try-except ValueError) para impedir que o usuário digite
           letras ou símbolos no lugar de números.
        2. Impedir que o usuário digite valores de consumo negativos (ex: litros < 0 ou kwh < 0).
           Se for negativo, disparar ou tratar como erro de valor.
        3. Buscar a empresa pelo 'cnpj' no dicionário 'banco_dados' e fazer o append
           do novo consumo (um mini-dicionário contendo litros e kWh convertidos para float)
           na lista 'consumos'.
    """
    if cnpj not in banco_dados:
        print(f"Erro: CNPJ '{cnpj}' não encontrado.")
        return False

    try:
        litros = float(litros_str)
        kwh = float(kwh_str)
    except ValueError:
        print("Erro: Os valores de consumo devem ser números válidos.")
        return False

    if litros < 0 or kwh < 0:
        print("Erro: Os valores de consumo não podem ser negativos.")
        return False

    banco_dados[cnpj]["consumos"].append({"litros": litros, "kwh": kwh})
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
        
    Desafios/Foco Técnico para Pessoa 6:
        1. Verificar se o CNPJ existe no dicionário.
        2. Tratar exceção try-except para garantir que a nova frota é um número inteiro válido.
        3. Reescrever diretamente o valor da chave existente: banco_dados[cnpj]["frota"] = nova_frota.
    """
    if cnpj not in banco_dados:
        print(f"Erro: CNPJ '{cnpj}' não encontrado.")
        return False

    try:
        nova_frota = int(nova_frota_str)
    except ValueError:
        print(f"Erro: '{nova_frota_str}' não é um número inteiro válido para a frota.")
        return False

    banco_dados[cnpj]["frota"] = nova_frota
    return True


def excluir_empresa(cnpj: str) -> bool:
    """
    Função da Pessoa 6: Remove uma empresa do dicionário de forma segura.
    
    Parâmetros:
        cnpj (str): CNPJ da empresa a ser excluída.
        
    Retorna:
        bool: True se excluída com sucesso, False caso contrário.
        
    Desafios/Foco Técnico para Pessoa 6:
        1. Verificar se o CNPJ existe no dicionário.
        2. Usar o método pop() para deletar o registro do dicionário de forma segura:
           banco_dados.pop(cnpj).
        3. Informar ao usuário se a empresa foi removida com sucesso.
    """
    if cnpj not in banco_dados:
        print(f"Erro: CNPJ '{cnpj}' não encontrado.")
        return False

    banco_dados.pop(cnpj)
    print(f"Empresa com CNPJ '{cnpj}' removida com sucesso.")
    return True

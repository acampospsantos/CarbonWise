"""
MÓDULO: utils/validators.py
RESPONSÁVEIS: Geral (Pessoa 3 / Pessoa 4)

Este módulo contém funções auxiliares de validação de dados para garantir a consistência
do que é inserido no sistema, antes de passar para os controladores.
"""

def limpar_cnpj(cnpj_sujo: str) -> str:
    """
    Remove caracteres especiais de um CNPJ (deixando apenas números).
    
    Exemplo: "12.345.678/0001-90" -> "12345678000190"
    """
    if not cnpj_sujo:
        return ""
    return "".join(char for char in cnpj_sujo if char.isdigit())


def validar_cnpj_formato(cnpj: str) -> bool:
    """
    Verifica se o CNPJ possui formato válido e se seus dígitos verificadores estão corretos.
    """
    cnpj_limpo = limpar_cnpj(cnpj)
    
    # CNPJ deve ter exatamente 14 dígitos
    if len(cnpj_limpo) != 14:
        return False
        
    # CNPJs com todos os dígitos iguais são inválidos
    if len(set(cnpj_limpo)) == 1:
        return False
        
    # Validação do primeiro dígito verificador
    pesos_1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma_1 = sum(int(cnpj_limpo[i]) * pesos_1[i] for i in range(12))
    resto_1 = soma_1 % 11
    digito_1 = 0 if resto_1 < 2 else 11 - resto_1
    
    if int(cnpj_limpo[12]) != digito_1:
        return False
        
    # Validação do segundo dígito verificador
    pesos_2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    soma_2 = sum(int(cnpj_limpo[i]) * pesos_2[i] for i in range(13))
    resto_2 = soma_2 % 11
    digito_2 = 0 if resto_2 < 2 else 11 - resto_2
    
    if int(cnpj_limpo[13]) != digito_2:
        return False
        
    return True

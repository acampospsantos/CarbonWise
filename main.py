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

from views.menu_view import menu_principal

def main():
    """
    Função principal que inicia a aplicação.
    """

    # Chama o menu principal estruturado pela Pessoa 1
    menu_principal()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nSistema encerrado pelo usuário. Até mais!")
        sys.exit(0)

import argparse
from string import ascii_letters, digits
from random import choice

def password_generator(length=18):
    """
    Gera uma senha aleatória com um comprimento especificado.

    Esta função cria uma senha segura, combinando letras maiúsculas e minúsculas,
    dígitos e caracteres especiais. A senha é gerada aleatoriamente a partir
    de um conjunto completo de caracteres.

    Args:
        length (int): O comprimento desejado para a senha. O valor padrão é 18.
                      Se o valor for menor que 1, o comprimento será definido para 1.

    Returns:
        str: A senha gerada.
    """
    if length < 1:
        length = 1

    specials_characters = '!#$%&*+-./:;?@~'
    all_characters = ascii_letters + digits + specials_characters

    password_list = [choice(all_characters) for _ in range(length)]

    return "".join(password_list)

if __name__ == "__main__":
    # Configura o parser de argumentos da linha de comando
    parser = argparse.ArgumentParser(description="Gera uma senha segura e aleatória.")
    parser.add_argument(
        'length',
        type=int,
        nargs='?', # Argumento opcional
        default=18,
        help='O comprimento da senha a ser gerada (padrão: 18).'
    )
    
    # Analisa os argumentos fornecidos pelo usuário
    args = parser.parse_args()

    # Gera a senha com base no comprimento fornecido
    generated_password = password_generator(args.length)
    
    # Exibe a senha gerada
    print(f"Senha Gerada: {generated_password}")


"""
Script utilizado para pasar los test de test.py
"""
import os


def main():
    """
    Crea un directorio "build" y un archivo index.html dentro de el
    """
    os.makedirs('build', exist_ok=True)
    with open('build/index.html', 'w', encoding='utf-8') as file_name:
        file_name.write('EATI2023')


if __name__ == '__main__':
    main()

import random


def inicio():
    print('---------------------------------------------------')
    print('Bienvenido a este juego de Piedra, Papel o Tijera')
    print('---------------------------------------------------')
    print('  OPCIONES: ')
    print('1. Piedra ')
    print('2. Papel ')
    print('3. Tijera ')

def juego():
    opciones = ['piedra', 'papel', 'tijera']
    
    playing = True
    while playing:
        cpu = random.choice(opciones)  # La CPU elige entre piedra, papel o tijera
        user_input = int(input('Selecciona una opcion (1 para Piedra, 2 para Papel, 3 para Tijera): '))

        if user_input in [1, 2, 3]:
            user = opciones[user_input - 1]  # Convertir la selección del usuario en la opción correspondiente
            print(f'Tu elegiste: {user}')
            print(f'La CPU eligió: {cpu}')
            
            # Comparar las elecciones
            if user == cpu:
                print('Empate!')
            elif (user == 'piedra' and cpu == 'tijera') or \
                 (user == 'papel' and cpu == 'piedra') or \
                 (user == 'tijera' and cpu == 'papel'):
                print('¡Ganaste!')
            else:
                print('Perdiste...')

            # Preguntar si se quiere volver a jugar
            again = input('¿Quieres volver a jugar? y/n: ')
            if again.lower() == 'n':
                playing = False
                print('Gracias por jugar. ¡Hasta la próxima!')
        else:
            print('Opción no válida, intenta de nuevo.')

# Iniciar el juego
inicio()
juego()

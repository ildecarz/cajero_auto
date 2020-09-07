import csv

saldo = 1000

print('\t.:MENU:.')
print('1. Ingresar dinero en la cuenta')
print('2. Retirar dinero de la cuenta')
print('3. Mostrar saldo disponible')
print('4. Salir')

opciones = int(input('¿Que opción desea realizar?: '))

print('...................')

if opciones == 1:
    deposito = float(input('¿Cuanto dinero desae ingresar? -> '))
    saldo = saldo + deposito
    print(f'Su saldo actual es de {saldo}$')
elif opciones == 2:
    retiro = float(input('¿Cuanto dinero desea retirar? -> '))
    if retiro > saldo:
        print('No tienes suficiente saldo en tu cuenta.!')
    else:
        saldo -= retiro
        print(f'Su saldo actual es de: {saldo}$')
elif opciones == 3:
    print (f'Su saldo actual es de: {saldo}$')
elif opciones == 4:
    print('Gracias por usar nuestro cajero automático')
else:
    print('error, no eligió una opción válida')

with open('myacount', 'w') as a:
    money = csv.writer(a)
    
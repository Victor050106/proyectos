print("Debes fritar un huevo")

huevo = input("¿Tienes huevos? (S/N) ").strip().capitalize()

if huevo == "S":
    print("Agarra uno de la despensa")
else:
    dinero = input("¿Hay dinero? (S/N) ").strip().capitalize()
    if dinero == "S":
        print("Comprar un huevo en la tienda")
    else:
        print("No tienes dinero")
        print("No se puede freír un huevo")
        exit()

print("Agarra un sartén")

gas = input("¿Hay gas? (S/N) ").strip().capitalize()

if gas == "N":
    print("No tienes gas")
    print("No se puede freír un huevo")
    exit()

print("Encenderlo en la estufa")
print("Colocarle aceite")
print("Romper y echar el huevo")

sal = input("¿Lo quieres con sal? (S/N) ").strip().capitalize()

if sal == "S":
    print("Agregale sal")

print("Poner tapa")
print("Esperar a que se cocine")

quemado = input("¿Se quemó? (S/N) ").strip().capitalize()

if quemado == "S":
    print("No se pudo freír un huevo")
    exit()

print("Servir en un plato")
print("Comer")
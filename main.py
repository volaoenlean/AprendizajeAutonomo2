import secrets
import string

def generar_contraseña(longitud):
    # Definir el conjunto de caracteres permitidos
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    # Generar una contraseña segura
    contraseña = ''.join(secrets.choice(caracteres) for i in range(longitud))
    
    return contraseña

#Pedimos al usuario que introduzca la longitud deseada para la contraseña. Si la entrada no es válida, mostramos un mensaje de error y volvemos a pedir la longitud.

if __name__ == "__main__":
    while True:
        try:
            longitud = int(input("Introduce la longitud de la contraseña: "))
            if longitud < 1:
                raise ValueError("La longitud debe ser un número positivo.")
        except ValueError as e:
            print(e)
            continue

#validacion de la contraseña

        while True:
            contraseña_segura = generar_contraseña(longitud)
            print(f"Contraseña segura generada: {contraseña_segura}")
            
            satisfecho = input("¿Está satisfecho con la contraseña? (y/n): ").strip().lower()
            if satisfecho == 'y':
                print("¡Gracias por usar el generador de contraseñas!")
                break
            elif satisfecho == 'n':
                print("Vamos a generar una nueva contraseña...")
                break
            else:
                print("Entrada no válida, por favor ingrese 'y' o 'n'.")
        
        if satisfecho == 'y':
            break

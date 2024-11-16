"""
· Sólo usa letras minúsculas y dígitos.
· Nunca usa dígitos después de una letra (Una vez aparecen letras, 
    la contraseña debe continuar solo con letras)
· Si usa dígitos, siempre los usa de forma igual o creciente 
    (si sale un 3, ya no usará después un número menor)
· Si usa letras, siempre las usa en orden alfabético igual o creciente 
    (si sale una "b" ya no podrá usar una "a", por ejemplo)
"""

def es_valido(contraseña):
    flag_letra = False
    last_letra = 0
    last_digit = -1

    for char in contraseña:
        if(not (char.isdigit() or char.islower())):
            return False
        
        if(char.isdigit()):
            if(flag_letra):
                return False
            else:
                if(int(char) < last_digit):
                    return False
                else:
                    last_digit = int(char)
        else: #es minúscula
            flag_letra = True
            if(ord(char) < last_letra):
                return False
            else:
                last_letra = ord(char)
    return True

intentos_validos = 0
intentos_no_validos = 0

filename = input("Give me the file name: ")
with open(f"{filename}", "r") as log:
    for linea in log:
        if(es_valido(linea.strip())):
            intentos_validos += 1
        else:
            intentos_no_validos += 1
        if(intentos_no_validos == 13):
            print(linea)

print(f"sumbit {intentos_validos}true{intentos_no_validos}false")
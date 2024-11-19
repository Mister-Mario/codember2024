"""
· Número positivo: ΩMEGA avanza ese número de posiciones.
· Número negativo: Retrocede ese número de posiciones.
· Cero: Se queda en la misma posición (pero cuenta como movimiento).
Importante: Cada vez que ΩMEGA lee una instrucción, 
    incrementa el valor de esa instrucción en 1 después de usarla.
"""

def processInstructions(instrucciones):
    pointer = 0
    pasos = 0
    max_pointer = len(instrucciones)
    min_pointer = 0
    while(pointer < max_pointer and pointer >= min_pointer):
        pasos += 1
        prev_pointer = pointer
        pointer += instrucciones[prev_pointer]
        instrucciones[prev_pointer] += 1
    return pasos



pasos_totales = 0
pasos_ultima_lista = 0

with open("trace.txt", "r") as trace:
    for linea in trace:
        linea = linea.strip().split(" ")
        instrucciones = [int(i) for i in linea]
        pasos_ultima_lista = processInstructions(instrucciones)
        pasos_totales += pasos_ultima_lista

print(f"submit {pasos_totales}-{pasos_ultima_lista}")
        
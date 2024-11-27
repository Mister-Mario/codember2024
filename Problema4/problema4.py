def savePair(num1, num2, mapa):
    if num1 in mapa and num2 in mapa:
        array1 = mapa[num1]
        array2 = mapa[num2]
        new_array = array1 + array2 
        new_set = set(new_array) #Hacemos set para quitar duplicados
        for number in new_set: 
            mapa[number] = list(new_set)
    elif num1 in mapa: #Hay una key con valor num1
        mapa[num1].append(num2) #Añadimos el nuevo nodo a la lista de nodos
        mapa[num2] = mapa[num1] #Como no existe el nodo le añadimos la lista
    elif num2 in mapa:
        mapa[num2].append(num1)
        mapa[num1] = mapa[num2] 
    else:
        array = [num1, num2]
        mapa[num1] = array
        mapa[num2] = array



with open("./Problema4/network.txt", "r") as nodes:
    line = nodes.readline().strip()
#Quitamos todos los [ y ] y nos queda una lista de números separados por comas
clean_line = line.replace("[", "").replace("]", "")

counter = 0
num1 = -1
num2 = -1
mapa = {}
mapa_nodos = {}
for number in clean_line.split(","):
    if counter == 1:
        num2 = int(number)
        counter = -1
        savePair(num1, num2, mapa)
        mapa_nodos[num1] = 1
        mapa_nodos[num2] = 1
    else:
        num1 = int(number)
    counter += 1

"""
Ahora vamos por cada nodo
Y miramos si el array de nodos asociado es < 2
Si lo es pues los guardamos en save_nodes
Y siempre quitamos todos los nodos de all_nodes
"""
all_nodes = list(mapa_nodos.keys())
save_nodes = []
while len(all_nodes) != 0:
    number = all_nodes[0]
    nodes = mapa[number]
    if len(nodes) == 2:
        save_nodes += nodes
    for node in nodes:
        all_nodes.remove(node)

print(len(save_nodes))
save_nodes.sort()
print(save_nodes)

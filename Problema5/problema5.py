#Esto agardezcamoslo a gepeto
primos = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199]

total = 0
lista = []
with open("./Problema5/nodos.txt", "r") as nodos:
    line_splitted = nodos.readline().strip().split(",")
    for number in line_splitted:
        if int(number)in primos:
            sum = 0
            for digit in number:
                sum += int(digit)
            if sum in primos:
                total +=1
                lista.append(int(number))

print(f"Total {total}")
print(lista)
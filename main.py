import string
import random

indicePopulatie = 8
lungimeIndivid = 16
numarParinti = 3


def InitPop():
    letters = string.ascii_lowercase
    populatie = []
    for i in range(indicePopulatie):
        individ = []
        for j in range(lungimeIndivid):
            individ.append(random.choice(letters))
        populatie.append(individ);
    return populatie


def fitness(population, indexpop):
    listaFitness = []
    for i in range(indexpop):
        litereCorecte = 0
        for j in range(lungimeIndivid):
            if j % 2 == 0:
                if population[i][j] in ('a', 'e', 'i', 'o', 'u'):
                    litereCorecte = litereCorecte + 1
            else:
                if not population[i][j] in ('a', 'e', 'i', 'o', 'u'):
                    litereCorecte = litereCorecte + 1
        listaFitness.append(litereCorecte)
    return listaFitness


def selectie():
    global populatie
    global fitnessPopulatie
    parinti = []
    fitnessPopulatie, populatie = (list(t) for t in zip(*sorted(zip(fitnessPopulatie, populatie))))
    for i in range(7, 4, -1):
        parinti.append(populatie[i])
    return parinti


def incrucisareDiscreta():
    for i in range(numarParinti):
        for j in range(lungimeIndivid):
            r = random.randint(0, numarParinti - 1)
            if j % 2 == 0:
                if not parinti[i][j] in ('a', 'e', 'i', 'o', 'u'):
                    parinti[i][j] = parinti[r][j]
            else:
                if (parinti[i][j] in ('a', 'e', 'i', 'o', 'u')):
                    parinti[i][j] = parinti[r][j]


def mutatia():
    pm = 0.25
    copii = []
    for i in range(numarParinti):
        copil = []
        for j in range(lungimeIndivid):
            probabilitate = random.random()  # [0,1]
            if probabilitate < pm:
                letters = string.ascii_lowercase
                copil.append(random.choice(letters))
            else:
                copil.append(parinti[i][j])
        copii.append(copil)
    return copii


def nouaPopulatie():
    fitnessCopii = fitness(copii, 3)
    for i in range(3):
        for j in range(indicePopulatie):
            if fitnessCopii[i] > fitnessPopulatie[j]:
                fitnessPopulatie[j] = fitnessCopii[i]
                populatie[j] = copii[i]
                break


populatie = InitPop()
print("Populatia initiala")
for i in range(8):
    print(populatie[i])

fitnessPopulatie = fitness(populatie, indicePopulatie)
print(fitnessPopulatie)
iteratii = 0
while (True):

    fitnessPopulatie = fitness(populatie, indicePopulatie)

    fitnessTotal = 0
    for i in fitnessPopulatie:
        fitnessTotal = fitnessTotal + i
    if fitnessTotal == lungimeIndivid * indicePopulatie:
        break
    parinti = selectie()
    incrucisareDiscreta()
    copii = mutatia()
    nouaPopulatie()
    iteratii = iteratii + 1

print("Populatia finala")
for i in range(8):
    print(populatie[i])
print(fitnessPopulatie)

print("Populatia finala s-a realizat dupa " + str(iteratii) + " iteratii!")
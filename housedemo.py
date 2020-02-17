import csv
import matplotlib.pyplot as plt

with open("data/house/house.csv") as f:
    reader = list(csv.DictReader(f))
    #for row in reader:
    #    print(row["loyer"], row["surface"], float(row["loyer"]) / float(row["surface"]))

    # liste en intention
    surfList = [float(row["surface"]) for row in reader]
    loyerList = [float(row["loyer"]) for row in reader]
    loyerParm2 = [ float(row["loyer"]) / float(row["surface"]) for row in reader]
    loyerParm2Moyen = sum(loyerParm2)/len(loyerParm2)

    #print(surfList)
    #print(loyerList)

    # Exercice
    # 1/ afficher le nuage de point x / y
    # 2/ Critiquer ce nuage de points
    # 3/ Trouver un modèle mathematique
    # 4/ calculer le loyer/m² moyen
    # 5/ recalculer la moyenne des loyers/m² en utilisant numpy

print("Le Loyer par m² moyen est de : " + str(loyerParm2Moyen))
plt.scatter(surfList, loyerList)
# remarque tri non necessaire...
sortedSurfList = sorted(surfList)
plt.plot(sortedSurfList, [ loyerParm2Moyen * myx for myx in sortedSurfList], 'y')
plt.show()
#print(loyerParm2Moyen)

# 5/ avec numpy
import numpy as np
loyerArr = np.array(loyerList)
surfArr = np.array(surfList)
loyerParm2MoyenArr = loyerArr/surfArr
print("\nAvec numpy...")
print("Le Loyer par m² moyen est de : " + str(np.mean(loyerParm2MoyenArr)))
print("L'écart type du Loyer par m² est de : " + str(np.std(loyerParm2MoyenArr)))

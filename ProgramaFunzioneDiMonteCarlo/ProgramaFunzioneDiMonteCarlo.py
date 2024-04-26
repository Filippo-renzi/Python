from code import interact
import math
import random

raggio = 100000
raggio_SQR = raggio * raggio;

print("Determinazione di Pi-Greco con metodo di Montecarlo")

interazioni= 2000000
Random = random.Random()
dentro = 0

for i in range(interazioni):
    x = Random.randint(0,raggio)
    y = Random.randint(0,raggio)
    if(x*x + y*y < raggio_SQR):
        dentro +=1

Pi_montecarlo = 4 * dentro / interazioni;
print("Pigreco stimato = {}".format(Pi_montecarlo))

print("Pigreco esatto ={}".format(math.pi))


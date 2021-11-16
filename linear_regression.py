from matplotlib import pyplot as plt
import random
train = [[0, 15], [1, 13], [2, 11], [3, 9], [4, 7], [5, 5]]
plot = []

w = random.randrange(-100,100)
b = random.randrange(-100,100)

for i in range(len(train)):
    plt.scatter(train[i][0], train[i][1])

def mse(dataset, reg1, reg2):
    msev = 0
    for i in range(len(dataset)):
        msev = msev + (dataset[i][1] - (reg1 * dataset[i][0]) - reg2) ** 2
    return msev / len(dataset)

def msedw(dataset, reg1, reg2):
    msedv = 0
    for i in range(len(dataset)):
        msedv = msedv + 2 * (reg1 * (dataset[i][0] ** 2) - (dataset[i][1] * dataset[i][0]) + reg2 * dataset[i][0])
    return msedv / len(dataset)

def msedb(dataset, reg1, reg2):
    msedv = 0
    for i in range(len(dataset)):
        msedv = msedv + 2 * (reg2 - dataset[i][1] + (reg1 * dataset[i][0]))
    return msedv / len(dataset)

while True:
    for k in range(50):
        w = w - (msedw(train, w, b) * 0.01)
        b = b - (msedb(train, w, b) * 0.01)
    x = range(0, 5)
    y = [v*w+b for v in x]
    plt.plot(x, y)
    if abs(mse(train, w, b)) < 0.01: break



print("w:", w)
print("b:", b)


plt.show()





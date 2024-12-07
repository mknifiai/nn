
import random
import matplotlib.pyplot as plt

def findRoot(f, xmin, xmax, maxSteps=1000):
    bestSoFar = (0, f(0))
    trace = [bestSoFar]
    for step in range(maxSteps):
        x = random.uniform(xmin, xmax)
        fx = f(x)
        if (abs(fx) < abs(bestSoFar[1])):
            bestSoFar = (x, fx)
            trace.append(bestSoFar)
    return (bestSoFar, trace)

if __name__ == '__main__':
    
    def f(x):
        return x**3 - 4*x**2 - 11*x + 30
    
    result = findRoot(f, -10, 10, 10000)
    print(result)
    values = [bests[1] for bests in result[1]]
    plt.plot(values,'o-')
    plt.plot([0, len(values)-1], [0, 0], 'r--')

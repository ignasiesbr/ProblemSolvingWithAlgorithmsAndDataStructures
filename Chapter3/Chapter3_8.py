#8 . Consider a real life simulation
# Customers at a grocery store check-out
# Question: How many articles have to check-out the cashier to dispatch the customers fluently.

#A line is going to consist in the articles per minute that can process in average (aprox. 25) and the articles will
# be processed in a queue way.

#We consider that the cashier takes 1.5 second for each article in the car and that every customer have an average of
# 1 to 40 articles in the cart

#A random client can appear each minute.

# To process the articles through the line, we will use carts, each cart will have a random nnumber of items
import random
from pythonds.basic.queue import Queue
class Line:
    def __init__(self, tfa):
        self.speed = tfa
        self.currentCart = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentCart is not None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentCart = None

    def busy(self):
        return self.currentCart is not None

    def startNext(self, newcart):
        self.currentCart = newcart
        self.timeRemaining = newcart.getArticles() * self.speed

class Cart:
    def __init__(self, time):
        self.articles = random.randint(1,40)
        self.timestamp = time

    def getStamp(self):
        return self.timestamp
    def getArticles(self):
        return self.articles
    def waitTime(self, current):
        return current - self.timestamp


def newCart():
    return random.randint(1,60) == random.randint(1,60)


def simulation(speed, totaltime):
    l = Line(speed)
    cartQueue = Queue()
    waitTimes = []

    for i in range(totaltime):

        if newCart():
            c = Cart(i)
            cartQueue.enqueue(c)
        if (not l.busy()) and (not cartQueue.isEmpty()):
            cart = cartQueue.dequeue()
            waitTimes.append(cart.waitTime(i))
            l.startNext(cart)
        l.tick()

    avgWait = sum(waitTimes) / len(waitTimes)
    print("Average wait time for each cart is %6.2f secs, %3d tasks remaining" %(avgWait, cartQueue.size()))

for i in range(10):
    simulation(1.5,3600)








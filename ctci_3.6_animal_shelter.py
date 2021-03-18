class Animal(object):
    def __init(self, animalName, animalType, number):
        self.animalName = animalName
        self.animalType = animalType
        self.timestamp = number

class AnimalShelter(object):
    def __init__(self):
        self.dogQueue = []
        self.catQueue = []
        self.animalNumber = 0

    def enqueue(self, animalName, animalType):
        self.animalNumber += 1
        newAnimal = Animal(animalName, animalType, self.animalNumber)
        if animalName == "Cat": self.catQueue.append(newAnimal)
        elif animalName == "Dog": self.dogQueue.append(newAnimal)

    def dequeueAny(self):
        if len(self.dogQueue) == 0 and len(self.catQueue) == 0: return "None"
        elif len(self.dogQueue) == 0: return self.catQueue.pop().animalName
        elif len(self.catQueue) == 0: return self.dogQueue.pop().animalName
        else:
            if self.catQueue[0].timestamp < self.dogQueue[0].timestamp:
                return self.catQueue.pop().animalName
            else:
                return self.dogQueue.pop().animalName
    
    def dequeueDog(self):
        return self.dogQueue.pop().animalName

    def dequeueCat(self):
        return self.catQueue.pop().animalName
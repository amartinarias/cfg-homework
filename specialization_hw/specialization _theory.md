# Theory Questions Assignment

## 1. How does Object Oriented Programming differ from Process Oriented Programming?
In Object oriented programming(OOP), programs are divided into objects. Each object has got its own attributes and methods. Objects can inherit these from a parent class, but they can also have their own ones. In contrast, in Process Oriented Programming(POP),programs are divided into functions. Each function contains a series of instructions. Functions can be called by their names.

POP functions can access all the data as the information is shared globally within the program. However, OOP keeps data encapsulated, which means that data can only be read by the parts of the program that need to access it. This makes using OOP more secure than POP, where data is accessible at a global level. Another difference is that OOP allows for inheritance, meaning that Objects can inherit from a parent class but inheritance doesn't exist in POP. 

OOP can also be extended by adding new data easily whereas it’s more complicated to do so in POP.

OOP takes a lot of space in memory, which is why POP was a preferred programming paradigm when memory was a more common issue, but now that memory is cheaper and more accessible OOP has become more popular.

Finally, POP is a top-down programming paradigm, which means that big problems get broken down into chunks. On the contrary, OOP has a bottom up approach, meaning that smaller parts of the program link together to make up a bigger program.

## 2. What's polymorphism in OOP?
Polymorphism means that an object can perform the same action in different ways. In OOP, this means that if we have a parent class object, we can call its properties and methods through the child class methods and objects but altering them based on the information in the child class. 
For example, below we have the class *animals* which has a method called *make noise*. This method is then inherited by its child classes but with different properties:
```python
class Animals:  # This is a parent class

	    def __init__(self, name, noise):
        self.name = name
        self._noise = noise

			def make_noise(self):
				print(f"{self.name} says {self.noise}!")

class Dog(Animals): # This is a child class of Dog
			def __init__(self, name):
        super().__init__(name, "woof")



class Cat(Animals):  # This is another child class of Dog
			def __init__(self, name):
        super().__init__(name, "meow")

lassie = Dog("Lassie")
lassie.make_noise() # returns Lassie says woof"

elsa = Cat("Elsa")
elsa.make_noise() # returns Elsa says meow"
```
The ability to use the method _make noise_ in different ways by different child classes is what we know as Polymorphism.

## 3. What's inheritance in OOP?
Inheritance is one of the main features of OOP. It means that child classes can receive the attributes and methods from their parent class. As well as inheriting their attributes and methods, child classes can also have their own which are unique to them.
```python
class Dog:  # This is a parent class
    
	def __init__(self, name, age):
        self.name = name
        self._age = age

	def bark(self): # These are things dogs can do 
	    print(f"{self.name} says woof!")

class BorderCollie(Dog): # This is a child class of Dog
	def __init__(self, name, age, bark):
        super().__init__(name, age, bark)

	def agility(self):
	    print(f"{self.name} can jump high!")

class Chihuahua(Dog):  # This is another child class of Dog
	def __init__(self, name, age, bark):
        super().__init__(name, age, bark)

	def sit_in_handbag(self):
	    print(f"{self.name} can sit pretty in a handbag!")
```
E.g. A BorderCollie class can have its own method called “agility” and can also inherit the method “bark” from Dog(its parent class). However, the Chihuahua class won’t have the agility method as that is limited to BorderCollie, but it will inherit the Bark method from its parent class, Dog.

## 4. If you had to make a program that could vote for the top three funniest people in the office, how would you do that? How would you make it possible to vote on those people?
1. Use _input_ to find out how many people want to vote.
2. Initialize a variable with an empty list for the names of the people who are being voted.
3. Ask users to input the three names of the funniest people in the office.
4. Add the names that people input into the list we initialized on step 2.
5. Join those names into one list.
6. Use the itertools module to count all the instances of a name.
7. Finally, return the name of the winner.

Bellow is a rough and unfinished idea of how it could be done:
```python
finalists = []
names_funny_people = []
office_voters = input("How many people is going to vote? ")


def office_vote():
    for person in range(int(office_voters)*3):
        funniest_people_in_office = input\
("Who are the funniest people in the office? Enter one name at a time and only vote for up to three people. ")
        finalists.append(funniest_people_in_office.lower())
    return finalists


def preparing_list(funny_people: list):
    for item in funny_people:
        names_funny_people.append(item)
    return names_funny_people


def counting_votes(lst: list):
    counting = [item for item in Counter(names_funny_people).most_common()]
    print(f"The funniest person in the office is {counting[0]}.")


office_vote()
preparing_list(finalists)
counting_votes(names_funny_people)
```
## 5. What's the software development cycle?
SDLC is a methodology which follows a series of steps with the aim of delivering high-quality projects. 
These steps go from the beginning, assessing the project, to the delivery of the final version. The phases for SDLC can vary slightly and depending on the model, some may even happen in parallel or in fast sequence, as happens with agile. The standard phases defined within SDLC are: 

- Planning: During the planning phase, the team assesses the resources and risks that are part of the project. The team will look at viability, costs, etc.
- Requirements: Gathering requirements from the stakeholders and producing a document with them. If it’s an Agile methodology, this phase will produce a backlog but this differs from one model to another.
- Design: The design is based on the requirements. At this stage, the team focuses on architectural modes for the project.
- Implementation: This is the actual coding part, where the dev team create the project.
- Testing: The product gets tested and won’t be deployed until it passes all the tests.
- Deployment: The product gets released to the users. Some companies have several deployment environments. E.g. development, testing, production, etc. 
- Maintenance: After the product has been released, it still needs maintenance throughout its life.

Within SDLC there are different models of development; for example, Waterfall, Agile, Spiral or Iterative.

## 6. What's the difference between agile and waterfall?
Waterfall development is based on a linear development of projects. That means that project requirements are clearly established before the project starts and the project follows through every phase of development without advancing to the next phase until the previous one has been completed. 
In contrast, agile methodologies follow a circular pattern, meaning that they start with the project once they have a basic idea of what the stakeholders want to build. The development team goes through every phase in the creation of the project taking in new feedback each time. The first version of the project is the minimum viable product. Then, this process is repeated over and over, making changes and improving the project until the stakeholders/team are happy with the results. 

###Waterfall: 
_START_- Requirements → Design → Development → Testing → Deployment -_FINISH_

###Agile: 
_START_- Requirements → Design → Development → Testing → Deployment -_VERSION 1_

_START_- Requirements → Design → Development → Testing → Deployment -_VERSION 2_

_START_- Requirements → Design → Development → Testing → Deployment -_VERSION 3_

_START_- Requirements → Design → Development → Testing → Deployment -_FINISH_* \
*(This is just an example as there is no limit on the number of cycles a project may have)

This way of working makes Agile projects harder to budget for as there are no strict requirements and these will change over time: however, with waterfall is easier to budget as the requirements are clearly specified before moving onto the next phase. This also affects the time it takes to build the product, as waterfall projects take usually longer because the team cannot move onto the next stage until the previous one is finished.

A great advantage of agile is that it allows for flexibility and the project can change as it gets built. This means that agile teams are able to implement feedback from stakeholders/users; whereas with waterfall, the dev team have to wait until the project is finished to get feedback from stakeholders. Sometimes, by the time the project has finished it may already be outdated.

## 7. What is a reduced function used for?
To use the reduce() function, we need to import the module functools. In Python 2, it used to be a built-in function but it was moved to functools in Python 3.

The reduce() function takes two parameters, a function and an iterable(list, tuple, dictionary, etc.). It also has an optional argument which is an initializer.

This function works as a for loop by looping through the iterable whilst passing the function to it. 
It returns the same results as if the user had directly looped through that function with the given iterable.
```python
from functools import reduce

numbs = [10, 2, 2, 1]


def minus_numbers(a, b):
    return a - b

print(reduce(minus_numbers, numbs))
```
## 8. How does merge sort work
1. The first step with merge sort is to divide the original unsorted list until we only have unsorted lists with only one item in them. 
2. Next, the algorithm compares two of the unsorted sublists and joins them in order.
3. The algorithm keeps comparing the rest of the unsorted items turning them into sorted pairs.
4. Then the pairs are compared with each other forming sorted sublists and those sorted sublists keep being compared and sorted until we have a final sorted list.
```markdown
Unsorted List                         -> 3562
Divide list until there are           -> 35    62
multiple lists with one unsorted item -> 3  5  6  2
Compare the items in pairs            -> 35    26
Sorted List    			      -> 2356
```

## 9. Generators - Generator functions allow you to declare a function that behaves like an iterator, i.e. it can be used in a for loop. What is the use case?
Generators are used to create custom iterators. A generator looks like a normal function but, it uses the keyword _yield_ instead of _return_. 
- One use case, is to create our own custom iterators. 
- They are also simpler to use than creating an iterator.
- Generators only produce the next item on the list once the previous one has been used. This means that we can use them if we need to be memory efficient.
- They can be used for infinite loops.
```python
def gen(n):
    for i in range(n):
        yield i*i

print(list(gen(3)))
```

## 10. Decorators - A page for useful (or potentially abusive?) decorator ideas. What is the return type of the decorator?
Decorators are used to give extra functionality to an already existing function. A decorator can return any type of object depending on its functionality.

The issue with decorators is that they can be misused as, with their help, users can alter the final output of a function in ways that it wasn't meant to change. 
For example, they could alter a function’s privacy or print information that wasn't intended.
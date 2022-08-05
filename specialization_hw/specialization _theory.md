# Theory Questions Assignment

## 1. How does Object Oriented Programming differ from Process Oriented Programming?
In Object oriented programming(OOP), programs are divided into objects. Each object has got its own attributes and methods. Objects can inherit these from their classes as well as having their unique ones. In contrast, in Process Oriented Programming(POP),programs are divided into functions. Each function contains a series of instructions. A function can be called by its name.

POP functions can access all the data as the information is shared globally within the program. However, OOP keeps data encapsulated which means that data can only be read by the parts of the program that need it. This makes using OOP more secure than POP where any all the data is accessible at global level. Another difference is that OOP allows for inheritance, meaning that Objects can inherit from their classes but inheritance doesn’t exist in POP.  OOP can also be extended by adding new data easily whereas it’s more complicated to do so in POP.

 OOP takes a lot of space in memory which is why POP was a preferred paradigm when memory was an issue but now that memory is cheaper and easier to get OOP has become more popular.

Finally, POP is a top-down programming paradigm, which means that a big problem gets broken down into chunks. On the contrary OOP has a bottom up approach, meaning that smaller parts of the program link together to make up a bigger program.

## 2. What's polymorphism in OOP?
Polymorphism means that an object can perform some action in different ways. In OOP this means that if we have a parent class object, we can call its properties and methods through the child objects but changing them depending on the information in the child class. 
For example, if we have the class *animals* which **has a method called *make noise.* This method is then inherited by the children classes but with different noises:
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
```
The ability of using something like the method make noise in different ways by different child classes is what we know as Polymorphism.

## 3. What's inheritance in OOP?
Inheritance is one of the features of OOP. It means that Child Classes receive their parent class’ atributes and methods. As well as that, Child Classes can also have their own attributes which are unique to them.
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
E.g. a Border Collie can have its own method called “agility” and also will inherit the method “bark” from the class dog. However, the Chihuahua class won’t have the agility method as that is only for the BorderCollie but they will have the Bark method from their parent class Dog.

## 4. If you had to make a program that could vote for the top three funniest people in the office, how would you do that? How would you make it possible to vote on those people?
1. Use _input_ to find out how many people want to vote.
2. Initialize a variable with an empty list for the names of the people who are being voted.
3. Ask users to input the three names of the funniest people in the office
4. Add the names that people input into the list we initialized on step 2.
5. Convert those names into one list
6. Use the itertools module to count all the instances of a name
7. Finally, return the name of the winner

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
SDLC is a methodology which follows a series of steps with the aim of delivering a high-quality project. 
These steps go from the beginning, assessing the project to the delivery of the final version of it. The phases for SDLC can vary slightly and depending on the model, some may even happen at the same time or really fast, like in agile. The standards phases defined within SDLC are: 

- Planning: During the planning phase the team takes into account resources and risks with regards to the project. They look at viability, costs, etc.
- Requirements: Gathering requirements from the stakeholders and producing a document with them. If it’s an Agile methodology it’ll produce a backlog but this differs from one model to another.
- Design: The design is based on the requirements. At this stage, the team focusses on architectural modes for the program.
- Implementation: This is the actual coding part, where the dev team create the project.
- Testing: The product gets tested and won’t be deployed until it passes the tests.
- Deployment: The product gets released to the users. Some companies have several deployment environments
- Maintenance: After the product has been released, it still needs maintenance.

Within SDLC there are different models of development, for example, Waterfall, Agile, Spiral or Iterative.

## 6. What's the difference between agile and waterfall?
Waterfall development is based on a linear development of projects. That means that project requirements are clearly established before the project starts and the project follows through every step of development without advancing to the next step until the previous one has been completed. 
In contrast, agile methodologies follow a circular pattern, meaning that they start with the project once they have a basic idea of what the stakeholders wants. The development team goes through every step in the creation on the project taking in new feedback each time. This process is repeated over and over, making changes and improving the project until the stakeholders/team are happy with the result. 

###Waterfall: 
_START_- Requirements → Design → Development → Testing → Deployment -_FINISH_

###Agile: 
_START_- Requirements → Design → Development → Testing → Deployment -_VERSION 1_

_START_- Requirements → Design → Development → Testing → Deployment -_VERSION 2_

_START_- Requirements → Design → Development → Testing → Deployment -_VERSION 3_

_START_- Requirements → Design → Development → Testing → Deployment -_FINISH_* \
*(This is just an example as there is no limit on the number of cycles a project may have)

This way of working make Agile projects harder to budget for as there are no strict requirements and these will change over time: however, with waterfall is easier to budget as the requirements are clearly specified before the  project has began. This also affects times as waterwall projects take usually longer because the team cannot move onto the next stage until the previous one is finished.

A great advantage of agile is that it allows for flexibility and the project can change as it gets built. This results on being able to implement feedback from stakeholders/users, whereas with waterfall, the dev team have to wait until the project is finished to get feedback from stakeholders.

## 7. What is a reduced function used for?

## 8. How does merge sort work
1. The first step with merge sort is to divide the original unsorted list until we only have unsorted lists with only one item in them. 
2. Next, the algorithms compares two of the unsorted sublists and joins them in order.
3. The algorithm keeps comparing the rest of the unsorted items into sorted pairs.
4. Then the pairs are compared with each other forming sorted sublists and those sorted sublists keep being compared and sorted until we have a final sorted list.
```markdown
Unsorted List                         -> 3562
Divide list until there are           -> 35    62
multiple lists with one unsorted item -> 3  5  6  2
Compare the items in pairs            -> 35    26
Sorted List    			      -> 2356
```

## 9. Generators - Generator functions allow you to declare a function that behaves like an iterator, i.e. it can be used in a for loop. What is the use case?
Generators are used to create custom iterators. A generator looks like a normal function but it uses the keyword _yield_ instead of _return_. 
- One of the use cases is that they are used when we want to create our own custom iterators. 
- They are also simpler to use than creating an iterator.
- Generators only produce 
- the next item on the list when the previous one has been used. This means that we can use them if we need to be memory efficient.
- They can be used for infinite loops.
```python
def gen(n):
    for i in range(n):
        yield i*i

print(list(gen(3)))
```

##10. Decorators - A page for useful (or potentially abusive?) decorator ideas. What is the return type of the decorator?
"""

TASK 1

Write a class to represent a Cash Register.
Your class should keep the state of price total and purchased items

Below is a starter code:
------------------------
1. you can add new variables and function if you want to
2. you will NEED to add accepted method parameters where required.
For example, method add_item probably accepts some kind of an item?..
3. You will need to write some examples of how your code works.

"""


class CashRegister:

    def __init__(self):
        self.total_items = {}  # {'item': 'price'}
        self.total_price = 0
        self.percentage_discounted = 0

    def add_item(self, item):  # This function adds items to the dictionary. It takes one parameter
        self.total_items.update(item)

    def remove_item(self, item):  # This function removes items from the dictionary. It takes one parameter
        self.total_items.pop(item)

    def apply_discount(self, percentage_discounted):
        """
        Calculates the quantity of the discount.

        Param: percentage_discounted, an integer that represents the percentage of the discount.
        Return: self.discount, the amount to be discounted of the total.
        """
        self.discount = (sum(self.total_items.values()) * percentage_discounted) / 100
        return self.discount

    def get_total(self):
        """
        Calculates the total price after the discount has been applied.

        Return: final price.
        """
        total_price = round(sum(self.total_items.values()) - self.discount, 2)
        return f"The price for your shop is: {total_price}"

    def show_items(self):
        """
        This function returns a breakdown of the items added to the Cash Register and the price per item.

        Return: A printed statement
        """
        if self.total_items == {}:
            print("There are no items in the Cash Register.")
        else:
            for item, price in self.total_items.items():
                print(f"1 x {item} at £{price}\n")

    def reset_register(self):  # Clears all the items on a list
        self.total_items.clear()


# Client One shows to the register with a toothbrush:
client_one = CashRegister()
client_one.add_item({"Toothbrush": 2})
client_one.add_item({"Melon": 2.6})
client_one.add_item({"Tomatoes": 1.5})

# Client One checks their shopping list
client_one.show_items()

# Client One realises that they don't have teeth anymore and don't actually need a toothbrush
client_one.remove_item("Toothbrush")

# Client One has a coupon for a 20% discount which gets applied to the total price
client_one.apply_discount(20)
print(client_one.get_total())

# After Client One has finished the Cash Register gets reset and the items disappear from the dictionary
client_one.reset_register()
client_one.show_items()


"""

TASK 2

Write a base class to represent a student. Below is a starter code. 
Feel free to add any more new features to your class. 
As a minimum a student has a name and age and a unique ID.

Create a new subclass from student to represent a concrete student doing a specialization, for example:
Software Student and Data Science student. 

"""
import math


class Student:

    def __init__(self, name, age, id, specialization, pet=None):
        self.name = name
        self._age = age
        self._id = id
        self.specialization = specialization
        self.pet = pet
        self.subjects = dict()

    def school_file(self):  # Prints the student's information
        print(f"Student {self._id}'s full name is: {self.name}. Specialization: {self.specialization}")

    def introduction(self):  # Student's introduction
        if self.pet is None:
            print(f"Hello, my name is {self.name} and I'm {self._age}.")
        else:
            print(f"Hello, my name is {self.name} and I'm {self._age}. My pet is a {self.pet}")


class CFGStudent(Student):

    def __init__(self, name, age, id, specialization):
        super().__init__(name, age, id, specialization)

    def add_subject(self, subjects):
        self.subjects.update(subjects)

    def remove_subject(self, subjects):
        self.subjects.pop(subjects)

    def students_subjects(self):  # Prints the list of subjects a student is taking
        print(f"{self.name} studied:")
        for item in self.subjects.keys():
            print(f"- {item}")

    def student_mark(self):
        """
        This function uses adds the grades of the student and calculates the average grade,

        Return: A printed statement with the student's final grade.
        """
        average_grade = sum(self.subjects.values()) / len(self.subjects)
        print(f"{self.name} has achieved a {math.floor(average_grade * 100) / 100}")


# Student One gets initialized and his information printed
peter = Student("Peter Pettigrew", 16, "001", "Software", "rat")
peter.school_file()
peter.introduction()

# Student Two gets initialized. This is a CFG student and inherits from the Student class
emma = CFGStudent("Emma Watson", 22, "002", "Data")

# Student Two's subjects get added and printed to the console
emma.add_subject({"Building an API": 9.2})
emma.add_subject({"SQL": 8})
emma.add_subject({"Iterators": 8.7})
emma.students_subjects()

# We need to remove a subject from the list and print it again
emma.remove_subject("SQL")
emma.students_subjects()

# We need to know the student's average grade
emma.student_mark()

# class CFGStudent(<should inherit from Student>)
#     create new methods that manage student's subjects (add/remove new subject and its grade to the dict)
#     create a method to view all subjects taken by a student
#     create a method  (and a new variable) to get student's overall mark (use average)

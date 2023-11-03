# Object 
class Sample():
    pass

my_sample = Sample()

# print(my_sample)

class Dog():
    # CLASS OBJECT ATTRIBUTE
    # SAME FOR ANY INSTANCE OF A CLASS
    species = 'mammal'
    def __init__(self, breed, name, spots):
        # Attribute
        # We take in the argument
        # Assign it using self.attribute_name
        self.breed = breed
        self.name = name
        # expect boolean True/False
        self.spots = spots
    
    def display_info(self):
        print(f'Breed: {self.breed}, Name: {self.name}, Spots: {self.spots}')

# my_dog = Dog(mybreed='lab')
my_dog = Dog('jerman', 'pinky', False)

# print(my_dog)
# print(my_dog.breed)
# print(my_dog.name)
# print(my_dog.spots)
# my_dog.display_info()





# create a class Circle and method which gives circumference of the circle.

class Circle():
    # Class defined attributes
    pi = 3.14

    def __init__(self, radius):
        # User defined attributes
        self.radius = radius

    def circumference(self):
        result = 2 * self.pi * (self.radius)
        print('The Circumference of a Circle of radius {} is {}.'.format(self.radius, result))

# result = Circle(30)
# result.circumference()


class Animal():

    def __init__(self):
        print('Animal Species')
    # Methods
    def who_am_i(self, animal="animal"):
        print(f'I am a {animal}')
    def eating_time(self):
        print('feed me!')


# Dog is an animal, so we can inherit the properties of Animal inside the Dog class and don't need to rewrite these properties again.

# 1. Inheritance

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Dog class created')

    # we can also overwrite the methods and edit or change inside the method
    def eating_time(self):
        print('feed me ! I am a dog !')

# my_dog = Dog()
# my_dog.who_am_i('dog')



#
class Book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def display(self):
        print(f'The Book {self.title} of {self.pages} pages was written by {self.author} !')

    # for displaying information in a string format we create display() method, but gives more suitability, it gives __str__ method write the output in a f string format. It uses return keyword instead of print. So use return for printin output.

    def __str__(self):
        return f'The Book {self.title} of {self.pages} pages was written by {self.author} !'
    
    def __len__(self):
        return self.pages
    
my_book = Book('Bahubali', 'S.S. Rajamoli', 60)
print(my_book)
print(len(my_book))

# Top 10 Magic functions in python
# __init__, __str__, __eq__, __repr__, __ne__, __add__, __getitem__, __setitem__, __len__, __del__




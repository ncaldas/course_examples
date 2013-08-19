#RequestContext is a class in python
    #RequestContext(request, {}) -> the class with the object request and the context {}
   #PersonWee --> camel case only for naming classes
   #person_wee --> not camel case only for naming functions
#class Person(object)
    #create a class called person that is an object
#can define the class:
    #class Person(object):
    
    
    #javi = Person(name='Javier', age=31)
    #javi.name => will give you Javier
    #javi.age => will give you 31
    #but it can be changed javi.name = 'Roberto' or javi.age = 29

# def __init__(self, name, age): --> this is a function of yourself, that's what the 'self' means

#it should look like this:
    
    #class Person(object):
        #def __init__(self, name, age):
            #self.name = name
            #self.age = age

#class Person(object):
    #def __init__(self, name, age):
        #self.name = name
        #self.age = age

#nandita = Person(name="Nandita", age=23) --> Person now becomes the object

#nandita
#<__main__.Person at Ox1fa0690>

#nandita.age
#23

#nandita.hair_colour = "black"
#nandita_hair_colour
#'black'

#buuut you cannot add the new type in the object:
#Person("Nandita", hair_colour="black")
    #it will come back as __init__() got an unexpected keyword argument 'hair_colour'


#to make a new class with teacher that inherits the objects of Person
#class Teacher(Person):
    #pass

#now the class teacher will have all the objects and parameters as Person

#to add new object within Teacher
class Teacher(Person):
    def__init__(self, name, age, course):
        super(Teacher, self).__init__(name, age) #search for me the father of Teacher, which is person, and create a new and now create a new object of the father with __init__
        self.course = course

#
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.year_of_birth = year_of_birth
            def get_age(self): #to get the year of birth of any person; this def function will only worl with the Person
                return current_year - self.year_of_birth

















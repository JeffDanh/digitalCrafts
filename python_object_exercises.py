# 1. Basics
class Person: 
    def __init__(self, name, email, phone): 
        self.name = name 
        self.email = email 
        self.phone = phone 
        self.friends = []
        self.greeting_count = 0 # Count number of greetings
        self.people_greeted = []
    def greet(self, other_person):
        self.greeting_count += 1 
        self.people_greeted.append(other_person)
        print('Hello {}, I am {}!'.format(other_person.name, self.name))
    def print_contact_info(self):
        print(self.name + '\'s email: ' + self.email + ', ' + self.name + '\'s phone number: ' + self.phone)
    # add friend
    def add_friend(self, friend):
        self.friends.append(friend)
    # number of friends
    def num_friends(self):
        print(len(self.friends))
    def __str__(self):
        return 'Person: {}; {}; {}'.format(self.name, self.email, self.phone)    
    # Bonus Challenge
    def num_unique_people_greeted(self):
        uniq_people_greeted = []
        for i in self.people_greeted:
            if i not in uniq_people_greeted:
                uniq_people_greeted.append(i)
        print(len(uniq_people_greeted))

sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')
jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')

sonny.greet(jordan)
jordan.greet(sonny)

print('Sonny: ' + sonny.email + ', ' + sonny.phone)
print('Jordan: ' + jordan.email + ', ' + jordan.phone)

# 2. Make your own class
class Vehicle:
    def __init__(car, make, model, year):
        car.make = make
        car.model = model
        car.year = year
    def print_info(car):
        print(car.year, car.make, car.model)
    


car1 = Vehicle('Toyota', 'Tundra', 2014)
print(car1.make, car1.model, car1.year)
car1.print_info()

sonny.print_contact_info()

jordan.friends.append(sonny)
sonny.friends.append(jordan)
print(len(jordan.friends))

jordan.add_friend(sonny)
print(len(jordan.friends))
jordan.num_friends()

sonny.greet(jordan)
sonny.greet(jordan)
sonny.greet(jordan)
print(sonny.greeting_count)

print(sonny.__str__())

sonny.num_unique_people_greeted()
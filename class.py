# class Car:
#     def __init__(self,brand,year,speed):
#         self.brand = brand
#         self.year = year
#         self.speed = speed

#     def brake(self):
#         return f'{self.speed - 50} km/h'
    
# car1 = Car('toyota', 15, 100)
# car2 = Car('lamborgini', 10, 450)

# print(car1.brand, car1.brake())
# print(car2.speed) 

# import datetime

# class Person:
#     def __init__(self, name, date) -> None:
#         self.name = name
#         self.date = date

#     def age(self): 
#         current_year = datetime.date.today().year
#         return current_year - self.date

# person1 = Person('sandro', 2001)

# print(person1.name, person1.age()) 


# import datetime

# class Person:
#     def __init__(self, name, birth_year, birth_month, birth_day) -> None:
#         self.name = name
#         self.birth_year = birth_year
#         self.birth_month = birth_month 
#         self.birth_day = birth_day

#     def age(self): 
#         current = datetime.date.today()
#         print(current)
#         year_answer = current.year - self.birth_year
#         month_answer = current.month - self.birth_month
#         day_answer = current.day - self.birth_day
#         if day_answer < 0:
#             month_answer -= 1
#             day_answer += 31        
#         if month_answer < 0:
#             year_answer -=1
#             month_answer += 12
#         return year_answer, month_answer, day_answer

# person1 = Person('mea', 2005, 3, 1)

# print(person1.name, person1.age())       


# class MyContextManager:
#     def __enter__(self):
#         print("Entering the context")
#         return self
    
#     def __exit__(self, exc_type, exc_value, traceback):
#         print("Exiting the context")

# # Using the context manager
# with MyContextManager() as cm:
#     print("Inside the context")

# # Outside the context manager
# print("Outside the context")
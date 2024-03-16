import time
from abc import ABCMeta, abstractstaticmethod
 #Dunders
 
class Person:
     #Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    #DeConstructor
    def __del__(self):
        print('object is being desconstructed')
        
        
class Vector:
    def __init__(self, x, y ):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __repr__(self):
        return f'[PrintOut] {self.x}'
    
    def __len__(self):
        return 10
    
    def __call__(self):
        print('Hello I was called!')
        return True
        

v1 = Vector(10, 30)
v2 = Vector(20, 50)
v3 = v1 + v2

print(v3)
print(len(v3))
print(v3())
  
         
p = Person('jeff', 42)

del p











#Decorators



def mydecorator(function):
    def wrapper(*args, **kwargs):
        print(f'I am decorating the function Called \'{function.__name__}\'')
        function(*args, **kwargs)
    return wrapper

@mydecorator
def add_stuff():
    print('This function was decorated')
    
add_stuff()


def jeffs_logger_decorator(func):
    def wrapper(*args, **kwargs):
        function_name = f'Logging output of function \'{func.__name__}\' '
        with open('logger1.txt', 'a') as log:
            log.write(f' {function_name} the returned value for function {func.__name__} is {func(*args,**kwargs)} \n')
        return function_name
    return wrapper
        
@jeffs_logger_decorator
def person(name):
    return name

person('jeffrey')


   
class CheApiCaller:
    def __init__(self, username, token, url):
        self.url = url
        self.__token = token
        self.__username = username
        self.__response = None
        self.__headers = 'headers'
        print(f'Successfully connected to your API with your credentials to {self.url}')
        
    def log_api_call(self, func):
        def wrapper(self, **kwargs):
            print(f"Calling the api with the following credentials URL -  {kwargs['url']} - TOKEN: {kwargs['token']} -- USERNAME: {kwargs['username']} for function \' ")
            json_response_from_api = print(f"THIS IS THE JSON RESPONSE FROM \"{self.url}")
            return json_response_from_api
        return wrapper
    
    def start_api_call(self, **kwargs):
        api_response = print(f"This is the RAW for the GET request using the following input {kwargs}")
        self.__response = 'This is the response converted to JSON'
    
    @property
    def auth_token(self):
        return self.__token
    
    @property
    def username(self):
        return self.__username
    
    @property
    def response(self):
        return self.__response
    
    def __repr__(self):
        print(f"This is the response for instance {self} \n\n\n {self.resposne}")



class CheGmailEmailFinder(CheApiCaller):
    def check_inbox(self):
        self.start_api_call(token=self.auth_token, username=self.username, url=self.url)
        return self.resposne

    def parse_gmail_data(self):
        # This is where it will determin if its a AWS or Twilio ticket.
        #verify this using the From domain
            #you will have use REgex to avoid replied to emails.        
        return #Twilio or #AWS

class JiraTicketCreator(CheApiCaller):
    def __init__(self, ticket_data):                  
        self.__ticket_data = ticket_data
        
    def create_ticket(self):
        self.start_api_call(token=self.auth_token, username=self.username, url=self.url)
        return self.response
    

 
class TwilioDataProcessing(CheApiCaller):
    @staticmethod
    def clean_email_data():
        #SPECIFIC Logic for cleaning Twilio compliance email data
        #Then you will need to create the injected data to submit to the jira api call.
        return #returns email data in dictionary format


class AwsEc2DataProcessing(CheApiCaller):
    @staticmethod
    def clean_email_data():
        # SPECIFIC Logic for cleaning EC2 Abuse email data
        #Then you will need to create the injected data to submit to the jira api call.
        return #returns email data in dictionary format

    
class JiraTicketInstanceFactory:
    #Dynamically creates either an Aws instance or twilio instance upon running the script.
    @staticmethod
    def build_ticket_instance(ticket_type):
        # Create ticket instance
        if ticket_type == 'aws':
            return AwsEc2DataProcessing()
        if ticket_type == 'twilio':
            return TwilioDataProcessing()
        raise "Something Went wrong while creating ticket instance."



if __name__ == "__main__":
    gmail_instance = CheGmailEmailFinder('jeffrey.mcintyre@salesloft', 'JSDFISJDF24902j20j', 'https://api.gmail.mail')       
    inbox_data = gmail_instance.check_inbox()
    data_type = inbox_data.parse_gmail_data()
    ticket_type = JiraTicketInstanceFactory.build_ticket_instance(data_type)
    ticket_data = ticket_type.clean_email_data()
    jira_ticket = JiraTicketCreator('jeffrey.mcintyre@salesloft', 'JIRA4234252-TOKEN234523', 'https://api.JIRA.issue', ticket_data) 
    jira_ticket.create_ticket()
    
# jira_api_caller = CheApiCaller()
# gmail_api_caller = CheApiCaller('jefrey.mcintyre@salesloft.c0om', 'SJDFJSODJF@(#$(@J$F))', 'https://mail.gmail.com')

# class CheJira(CheApiCaller):
    
#      @jira_api_caller.call_api
#     def jira_stuff(*queries, **kwargs):
#         print('here are my jira queries')
#         return queries, kwargs.keys()

# @gmail_api_caller.call_api
# def gmail_stuff(*queries, **kwargs):
#     print('running email app')
#     return kwargs



class TimeStuffPlease:
    def __init__(self):
        print(f"TURNING ON FUNCTION TIMER....")
    
    def function_stopwatch(self, func, *args, **kwargs):
        def wrapper(*args, **kwargs):
            print(f"Get ready... we're going to time your function {func.__name__}!!")
            before = time.time()
            run_function = func(*args, **kwargs)
            after = time.time() - before
            print(f'Your function named \'{func.__name__} look {after} seconds to run!!!')
            return
        return wrapper


# jeff_func = TimeStuffPlease()

# @jeff_func.function_stopwatch
# def jeffs_function(*args, **kwargs):
#     time.sleep(*args)
#     return None

# jeffs_function(3)




#Encapsulation

class Vehical:
    def __init__(self, vim_number, serial_number):
        self.__serial_number = serial_number
        self.__vim_number = vim_number
    
    @property
    def serial_number(self):
        return self.__serial_number
    
    @serial_number.setter
    def serial_number(self, new_serial):
        if type(new_serial == str):
            self.__serial_number = new_serial
        return self.__serial_number
    
    @property
    def vim_number(self):
        return self.__vim_number
    
    @vim_number.setter
    def vim_number(self, new_vim):
        if isinstance(new_vim, str):
            self.__vim_number = new_vim
            print(f'NEW VIM NUMBER SET TO {new_vim}')
            return self.__serial_number
        raise "I dunno what that is try another VIM number!"

    
    @staticmethod
    def my_static_method():
        print("This is the StaticMethod")
    
    def __repr__(self):
        return f"This is the special print for your object -- your values are VIM_NUMBER={self.__vim_number} and SERIAL_NUMBER={self.__serial_number}."
        

    
# beemer = Vehical('VIM_NUMBER', 'SERIAL_NUMBER-222888444SGSG4485825')
# beemer.vim_number = "NEW_VIM--234234"
# beemer.my_static_method()



#Dealing with Abstract classes using the FACTORY DESIGN PATTERN.. and abstract class is a class where you connot crate instances from
from abc import ABCMeta, abstractstaticmethod

# in python if something is an interface you preceed the name of the abstract class with "I"
# so in the below example for the "Person" class there is an "I" in from of it.
class IPerson(metaclass=ABCMeta):
    @abstractstaticmethod
    def person_method():
        """This is an interface method."""
        
class Student(IPerson):
    def __init__(self): 
        self.name = "Basic student name"
        
    def person_method(self):
        print("I am a student.") #since we're inheriting fromt he abstract class we have to overRide the "person_method"
    
class Teacher(IPerson):
    def __init__(self):
        self.name = "Basic teacher name"
        
    def person_method(self):
        print("I am a techer.") 
        

#so the goal is this...what we want is to dynamically create either a student object or TEACHER OBJECT..
# to do this we wil need to create a factory class that actually builds this because we want it
#to decide which one to create at run-time.

class PersonFactory:
    @staticmethod
    def build_person(person_type):
        if person_type == "Student".lower():
            return Student()
        if person_type == "Teacher".lower():
            return Teacher()
        raise "Invalid type please check your input."
    
# if __name__ == "__main__":
#     choice = input("what type of person do you want to create?\n").lower()
#     person = PersonFactory.build_person(choice)
#     person.person_method()


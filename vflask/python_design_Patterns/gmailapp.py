from abc import abstractmethod, ABC

#Open Close Principle
class Specification:
    def is_satisfied(self):
        pass
    
class SearchQuery(Specification):
    def search(self, *arg, **kwargs):
        pass
    
class GmailSearchQuery(SearchQuery):
    def search(self, *search_operators):
        self.search_operators = search_operators
        

#LiskovSubtitutionPrinciple
class AddStuff:
    def __init__(self, number_1, number_2):
        self.__number_1 = number_1
        self.__number_2 = number_2
        self.__total = None
        
    def add_it_together(self):
        self.__total = self.__number_1 + self.__number_2
        return self.__number_1 + self.__number_2
    
    def __str__(self):
        return f'The Total is {self.total}'
    
    @property
    def total(self):
        return self.__total
            
    @property
    def value_sum(self):
        return self.__total
    
    @value_sum.setter
    def value_sum(self, num1):
        self.__number_1 = num1
        self.__total = num1 + 55
        return self.total
        
        
#The interface
def numbers_and_stuff(object):
    the_sum = object.add_it_together()
    expected_output = 300
    return expected_output == object.total

if __name__ == '__main__':
    obj1 = AddStuff(100, 200)
    obj1.value_sum = 4500
    print(numbers_and_stuff(obj1))
    
        

# # Interface Segreagation Principle
class CheApiConnect(ABC):
    @abstractmethod
    def connect_to_api(self, url, token, username):
        pass

class GmailApi(CheApiConnect):
    def __init__(self, url, username, auth_token):
        self.url = url
        self.username = username
        self.__auth_token = auth_token
        self.response = None
    
    def connect_to_api(self, url, token, username):
        pass
    
class JiraApi(CheApiConnect):
    def __init__(self, url, username, auth_token):
        self.url = url
        self.username = username
        self.__auth_token = auth_token
        self.response = None
    
    def connect_to_api(self):
        pass

class SearchQuery(ABC):
    @abstractmethod
    def search(self, *search_criteria):
        pass

class GmailSearchQuery(SearchQuery):
    def __ini__(self, gmail_api=GmailApi('https://api.jira.com','JSDFJ24902j9f0j2fw' 'Jeffrey.mcintyre@salesloft.com')):
        self.gmail_api = gmail_api
    
    def search(self, gmail_search_ops):
        pass

class JiraSearchQuery(SearchQuery):
    def __ini__(self, jira_api=GmailApi('https://mail.gmail.com','lskjdf09203j20' 'Jeffrey.mcintyre@salesloft.com')):
        self.jira_api = jira_api
    
    def search(self, jira_search_ops):
        pass
    
    
    
        
#Example of Duck Typeing

class Cow:
    def say_moo(self):
        print('Mooooo!!!!')
        
class Person:
    def __init__(self, name):
        self.name = name
        
    @property
    def persons_name(self):
        return self.name
        
    def say_moo(self):
        print(f'{self.persons_name} is MOOING like a CoW!!!')

# Interface
def moo(object):
    return object.say_moo()

if __name__ == '__main__':
    cow_1 = Cow()
    jeffrey = Person('Jeff')
    moo(cow_1)
    moo(jeffrey)


#Recursion counting to 50
def count_to_50(number=0):
    #Base Condition
    if number > 51: return number
    
    print(number)
    number += 1
    return count_to_50(number)

count_to_50()




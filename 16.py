__author__ = 'Ayla'
#Class Employee
#1. Create a class Employee
#```python

class InvalidSocial(ValueError):
    pass
class Employee:
    pass
#Input SS#
#2. Create a procedure that accepts a variable of type employee and inputs their SS#. Your code should validate that a
#valid SS# is put in.
#3. Create an exception InvalidSocial. In the event that an invalid ss# is typed in raise this exception.


def socialsecuritynumber(employee_class):
    employee_class.ss = input("Input Social Security number")
    try:
        aaa,gg,ssss = employee_class.ss.split('-')
        if len(aaa) != 3 or len(gg) != 2 or len(ssss) != 4:
            #print('Invalid social security number')
            raise InvalidSocial
        if aaa == '000' or gg =='00' or ssss == '0000':
            #print("Invalid social security number")
            raise InvalidSocial
        if aaa =='666' or '900'>='999':
            #print("Invalid social security number")
            raise InvalidSocial
        if aaa =='078' or gg =='05' or ssss =='1120':
            #print("Invalid social security number")
            raise InvalidSocial

        #check that employee_class.ss is valid
        #Anywhere that you find the ss is invalid raise InvalidSocial

        aaa=int(aaa)
        gg=int(gg)
        ssss=int(ssss)

        return aaa, gg, ssss
    except ValueError:
        #print("Enter a valid social security number")
        raise InvalidSocial


#def getsocial(employee_class):
#    employee_class.ss = input("Social: ")
#    try
 #       validatess(employee_class)
 #   except InvalidSocial:
 #       print("Invalid SS, please try again\n")
 #       getsocial(employee_class)

emp = Employee()
socialsecuritynumber(emp)
print(emp.ss)


























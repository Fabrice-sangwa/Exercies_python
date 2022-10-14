from inspect import _void


name = "Fabrice"
age = 32
level = 8
Qi = 200

def printAll():
    print(f"{name} have {age} and he is in {level} level with {Qi} points of Qi")
    
"""This function calulates the sum odf two numbers""" 
def somme(a : int , b : int)  :
    print(f"{a+b}")
    
if __name__ == "__main__" : 
    somme (4, 9)
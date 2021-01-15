import math, random, sys
 
def sci():
  # Aestetic part
  print('''\nYou chose the scientific calculator, are You Einstein?\n
=======================================================\n
•Here there are all your possibilities:
-Square root: enter \'√\' or \'sqrt\';
-Exponentiation: enter \'pow\';
-Sine: enter \'sin\' or \'sen\';
-Cosine: enter \'cos\';
-Tangent: enter \'tan\';
-Scientific notation (n1 × 10^n): enter \'scino\';
-Pi greek π: enter \'pi\';4324⁴
-Nepero\'s number: enter \'e\';
-If you want to stop the program, enter \'stop\'.\n
=======================================================
  ''')
  
  # Choice
  choicescifi = input('Choose what do you want to do: ')
  
  if choicescifi == 'stop':
    print('\nGoodbye')
    sys.exit() # Program breaks
   
  # Pi greek and Nepero's number   
  elif choicescifi == 'pi':
    print('\nPi greek value is... ' + str(math.pi))
  elif choicescifi == 'e':
    print('\nNepero\'s number is... ' + str(math.e))
  
  # Scientific operators with one needed input
    
  elif choicescifi == 'sqrt':
    valscifi = float(input('\nOk... choose your value: '))
    print('\nYour solution is... ' + str(math.sqrt(valscifi)))
  elif choicescifi == 'sin' or choicescifi == 'sen':
    valscifi1 = float(input('\nOk... choose your value: '))
    print('\nYour solution is... ' + str(math.sin(valscifi1)))
  elif choicescifi == 'cos':
    valscifi2 = float(input('\nOk... choose your value: '))
    print('\nYour solution is... ' + str(math.cos(valscifi2)))
  elif choicescifi == 'tan':
    valscifi3 = float(input('\nOk... choose your value: '))
    print('\nYour solution is... ' + str(math.tan(valscifi3))) 
    
  # Scientific operators with two needed inputs
  elif choicescifi == 'pow':
    base1 = float(input('\nChoose the base to elevate: '))
    exp = float(input('Choose the exponent: '))
    print('\nYour exponentiation is... ' + str(math.pow(base1, exp)))
  elif choicescifi == 'scino':
    base2 = float(input('\nChoose the base: '))
    x10 = float(input('Choose the exponent of 10: '))
    print(str(base2) + '×10^' + str(x10))    
    print('Your solution is... ' + str(base2 * (math.pow(10, x10))))

  reset()
   
#================================================================================     
#================================================================================   

   
  
def nor():
  # Aestetic part
  print('''\n=======================================================\n
•Here there are all your possibilities:
-Addition: enter \'+\' or \'sum\';
-Subtraction: enter \'-\' or \'diff\';
-Multiplication: enter \'*\' or \'x\' or \'mult\';
-Division: enter \'/\' or \':\' or \'div\';
-Extract a random integer number: enter \'randInt\';
-Extract a random float number: enter \'randFlo\';
-Roll a dice: enter \'dice\';
-To stop the program enter \'stop\'.\n
=======================================================
  ''')
 
  # Choice
  choice = input('Ok, so choose what you want to do: ')
  
  if choice == 'stop': 
    print('\nGoodbye')
    sys.exit() # Program breaks     
 
  # Random numbers' part
  elif choice == 'randInt' or choice == 'randint':
    print('\nYour random number is... ' + str(random.randint(0, 100000)))
  elif choice == 'randFlo' or choice == 'randflo':
    print('\nYour random number is... ' + str(round(random.uniform(0, 100000), 2)))
  elif choice == 'dice':
    print('\nThe dice says: ' + str(random.randint(1, 6)))  
  elif choice != 'randint' and choice != 'randInt' and choice != 'randflo' and choice != 'randFlo' and choice != 'dice':

    # Simple matemathic operators
    val1 = float(input('\nInsert your first value: '))
    val2 = float(input('Insert your second value: '))
  
    if choice == '+' or choice == 'sum':
      print('\nYour solution is... ' + str(val1 + val2))
    elif choice == '-' or choice == 'diff':
      print('\nYour solution is... ' + str(val1 - val2))
    elif choice == '*' or choice == 'x' or choice == 'molt':
      print('\nYour solution is... ' + str(val1 * val2))
    elif choice == '/' or choice == ':' or choice == 'div':
      print('\nYour solution is... ' + str(val1 / val2))  
  
  reset()
  

#================================================================================     
#================================================================================   


def ask():
  
  # Scientific calculator: yes or no?
  scifi = input('\nDo you want to use the scientific calculator?\n-Enter y/n ')
 
  if scifi == 'y' or scifi == 'Y':
    sci()  
  elif scifi == 'n' or scifi == 'N':
    nor()  
  else:
    print('\nERROR!!!\n')
    ask()


#================================================================================     
#================================================================================   


def reset():
  res = input('\nDo you want to use the calculator again?\n-Enter y/n ')
  if res == 'y' or res == 'Y':
    ask()
  elif res == 'n' or res == 'N':
    print('\nGoodbye')
    sys.exit()
    

#================================================================================     
#================================================================================   

  
# Hello
print('Welcome in my calculator!')

while True:
  ask()
  reset()      
################################################################################
#     ____                          __     _                          _____
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          |__  /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \          /_ < 
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        ___/ / 
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /____/  
#                                                                          
#  Question 3
################################################################################
#
# Instructions:
# Make a Python class for a magical oven that can combine ingredients at 
# different temperatures to craft special materials.
# 
# The oven class should have the methods:
# - add(item) to add an oven to be combined
# - freeze() to freeze the ingredients
# - boil() to boil the ingredients
# - wait() to combine the ingredients with no change in temperature
# - get_output() to get the result 
#
# You will need to change the `make_oven()` function to return a new instance
# of your oven.
#
# The `alchemy_combine()` function will use your oven. You can see the expected 
# formulas and their outputs in the test file, `question3_test.py`.

# This function should return an oven instance!
def agregar(self,elemento):
  self.ingredients.append(elemento)
def congelar(self):
  self.output = "congelado"
def hervir(self):
  self.output="hervido"
def esperar(self):
  if "cheese" in self.ingredients and "dough" in self.ingredients and "tomato" in self.ingredients:
    self.output= "pizza"
def get_output(self):
  return self.output
  def make_oven():
  return oven()
def alchemy_combine(oven, ingredients, temperature):
    for item in ingredients:
    oven.agregar(item)
if temperature < 0:
    oven.congelar()
elif temperature >= 100:
    oven.hervir()
else:
    oven.esperar()
return oven.get_output()

import random
class Set_Class():
   def __init__(self):
      self.set = set([])

   def add(self, number):
      self.set.add(number)

   def remove(self, number):
      if number in self.set:
         self.set.remove(number)

   def return_random(self):
      random_int = random.randrange(len(self.set))
      return list(self.set)[random_int]

   def get_all(self):
      return self.set

set_class = Set_Class()
set_class.add(1)
set_class.add(2)
set_class.add(3)
set_class.add(4)
set_class.add(5)
set_class.remove(3)

#%%
print(set_class.return_random())
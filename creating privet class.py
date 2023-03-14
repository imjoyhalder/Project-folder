# p2.py
class person:
   def __init__(self, name, alias):
      self.__name = name       # public
      self.__alias = alias   # private

   def who(self):
      print('name  : ', self.__name)
      print('alias : ', self.__alias)

   def __foo(self):          # private method
      print('This is private method')

   def foo(self):            # public method
      print('This is public method')
      self.__foo()
off = person("joy","Hlader")
off.foo()
off.who()
off.__foo()
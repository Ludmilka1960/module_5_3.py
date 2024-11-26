from xml.etree.ElementPath import xpath_tokenizer


class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __str__(self):
            return f"Название: '{self.name}', кол-во этажей:{self.number_of_floors}"

    def __eq__(self ,other):
             if isinstance(other, House):

                return self.number_of_floors == other.number_of_floors
             return False

    def __lt__(self, other):
             if  isinstance(other,House):
                return self.number_of_floors < other.number_of_floors
             return False

    def __le__(self ,other):
             if  isinstance(other,House):
                 return self.number_of_floors  <= other.number_of_floors
             return False

    def __gt__(self ,other):
            if isinstance(other,House):
                 return   self.number_of_floors >=other.number_of_floors
            return False

    def __ge__(self ,other):
             if isinstance(other,int):
                return self.number_of_floors < other
             return False

    def __ne__(self ,other):
             if isinstance(other,int):
                return self.number_of_floors != other.number_of_floors
             return True

    def __add__(self,value):
            if isinstance(value, int):
              return self.number_of_floors + value
            return self


    def __iadd__(self, other):
         if isinstance(other, House):

            return
    def __radd__(self, other):
         if isinstance(other, House):
            return self


h1 = House('Запад', 3)
h2 = House('ЖЭУ-27', 5)
print(f"Название: '{h1.name}', кол-во этажей:{h1.number_of_floors}")
print(f"Название: '{h2.name}', кол-во этажей:{h2.number_of_floors}")
print(h1 == h2)
print(h1 < h2)
print(h1 <= h2)
print(h1 > h2)
print(h1 >= h2)
print(h1!=h2)
h1=h2 + 2
print(h1)

















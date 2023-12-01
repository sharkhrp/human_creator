import random


class human:
    # class attribute !!
    hope = 9
    total_humans = []
    population = ()

    def __init__(self, color: str, self_sense: float, clean: bool, country: str,
                 money: int, name: str, age: int, good=True):

        color = color.lower()
        name = name.lower()
        country = country.lower()
        assert self_sense < 10, f"range is 1 ~ 10"
        assert age >= 0, f"human cant posses this age : {age}"
        assert age <= 130, f"humans cant live this longer these day :>"
        assert color == "purple" or "rainbow" or "green" or "blue" or "pink", f"humans dont have this color {color}"

        self.__good = good
        self.__name = name
        self.__clean = clean
        self.__age = age
        self.__color = color
        self.__country = country
        self.__money = money
        self.__self_sense = self_sense


        human.total_humans.append(self)
        human.population = len(human.total_humans)


    @property
    def name(self):
        return self.__name
    
    @property
    def good(self):
        return self.__good
        

    @property
    def money(self):
        if self.__money >= 45000:
            print("is rich")
        elif self.__money <= 1500:
            print("is poor")

        return self.__money
    
    @property
    def clean(self):
        return self.__clean
    
    @property
    def age(self):
        if self.__age >= 60:
            print("is old")
        elif self.__age <= 30:
            print("is in adult")
        elif self.__age <= 20 and self.__age >= 13:
            print("is in teenager")
        elif self.__age <= 10 and self.__age >= 6:
            print("is in child")
        elif self.__age <= 5:
            print("is in baby")
        elif self.__age > 100:
            print("is dead")

        return self.__age
    
    @property
    def color(self):
        return self.__color
    
    @property
    def country(self):
        print(f"he/she lives in {self.__country}")
        return self.__country
    
    @property
    def self_sense(self):
        print("yes he/she is kinda smart")
        return self.__self_sense
        

    def __repr__(self):
        return self.name

    @classmethod
    def create_population(cls, x):
        for i in range(x):
            # color
            color = random.choice(["white", "black", "yellow", "brown"])
            # True or False
            tf = random.choice([True, False])
            # for name
            words = [str(x) for x in "abcdefghijklmnopkrstwxvyz"]
            # self_sense
            n = random.randint(0, 10)
            # age
            z = random.randint(0, 120)
            # money
            r = random.randint(0, 20000000)
            # name
            e = '        '
            for o in range(6):
                d = random.randint(0, 24)
                e = e.replace(" ", words[d], 1)
            # @
            human(color, n, tf, "pakistan", r, e.strip(), z, tf)

    def see_age(self):
        if self.age >= 60:
            return "is old"
        else:
            return "isn't old"

    def hard_times(self):
        """there is no self.Hope that's why object who will use this def
          will find self.Hope in class (which has hope) from which it is created 
          and use it as its own
          this is called inheritance
          """
        self.hope = self.hope - 1

class male(human):
    def __init__(self, color: str, self_sense: float, clean: bool, country: str,
                 money: int, name: str, age: int, good=True):
        super().__init__(color, self_sense, clean, country, money, name, age, good)
    @classmethod
    def __repr__(cls):
        return "male"

class female(human):
    def __init__(self, color: str, self_sense: float, clean: bool, country: str,
                 money: int, name: str, age: int, good=True):
        super().__init__(color, self_sense, clean, country, money, name, age, good)
    @classmethod
    def __repr__(cls):
        return "female"

class gay(male):
    def __init__(self, color: str, self_sense: float, clean: bool, country: str,
                 money: int, name: str, age: int, good=True, likes="attract to male"):
        super().__init__(color, self_sense, clean, country, money, name, age, good)
        super().__repr__()
        self.likes = likes
        
class lesbian(female):
    def __init__(self, color: str, self_sense: float, clean: bool, country: str,
                 money: int, name: str, age: int, good=True, likes="attract to female"):
        super().__init__(color, self_sense, clean, country, money, name, age, good)
        super().__repr__()
        self.likes = likes


sam = male("WHITE", 5, True, "norway", 200000, "sam", 49, True)
keny = female("WHITE", 5, True, "norway", 200000, "sam", 49, True)
shahdil = male("white", True, True, "pakistan", 200, "shahdil", 14, True)
mitchel = lesbian("white", 8, True, "usa", 8000, "mitchel", 38, True)





print(mitchel

class ExampleMetaClass1(type):
    def __new__(classitself, *args):
        print("class itself: ", classitself)
        print("Others: ", args)
        return type.__new__(classitself, *args)



class ExampleMetaClass2(type):
    def __new__(classitself, classname, baseclasses, attributes):
        print("class itself: ", classitself)
        print("class name: ", classname)
        print("parent class list: ", baseclasses)
        print("attribute list: ", attributes)
        return type.__new__(classitself, classname, baseclasses, attributes)


class ExampleParentClass1:
    def test1():
        print("parent1 - test1")


class ExampleParentClass2:
    def test2():
        print("parent2 - test2")


class ExampleClass2(
    ExampleParentClass1, ExampleParentClass2, metaclass=ExampleMetaClass2
):
    int1 = 123
    str1 = "test"

    def test3():
        print("child1 - test3")




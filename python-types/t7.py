class Person:
    def __init__(self, name: str):
        self.name = name


def get_person_name(one_person: Person):
    return one_person.name


print(get_person_name(Person('foobar')))
# 类 类型提示

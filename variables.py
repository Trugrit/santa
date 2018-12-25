"""
Secret Santa Randomize Generator
Will not pair people with same family members
"""

import random


class Family:

    def __init__(self, name, family_relation):
        self.name = name
        self.family_relation = family_relation


def main():
    intro()
    txt = open('Santa.txt', 'w')
    for person in everyone:
        first = random.choice(everyone_pool)
        while first.family_relation == person.family_relation:
            first = random.choice(everyone_pool)
        everyone_pool.remove(first)
        second = random.choice(everyone_pool)
        while second.family_relation == person.family_relation or second.name == first.name:
            second = random.choice(everyone_pool)
        everyone_pool.remove(second)
        display(person, first, second)
        write(person, first, second, txt)
    txt.close()


def intro():
    print('--------------------------')
    print(' Secret Santa Randomize')
    print('--------------------------')


def display(person, first, second):
    print('{p}:'.format(p=person.name))
    print(first.name)
    print(second.name)
    print()


def write(person, first, second, txt):
    txt.write('{}:\n'.format(person.name))
    txt.write(first.name + '\n')
    txt.write(second.name + '\n' + '\n')


# Creating an instance of each person
dylan = Family('Dylan', 'Griffith')
bryan = Family('Bryan', 'Griffith')
kristi_james = Family('Kristi & James', "Griffith")
karen_rob = Family('Karen & Rob', 'Griffith')
erika = Family('Erika', 'Anderson')
susie = Family('Susie', 'Anderson')
marcia_mark = Family('Mark & Marcia', 'Gerardi')
jessica_tim = Family('Jessica & Tim', 'Gerardi')
dexter_randy = Family('Dexter & Randy', 'Dexter')

everyone = [dylan, bryan, kristi_james, karen_rob, erika, susie, marcia_mark, jessica_tim, dexter_randy]
everyone_pool = everyone + everyone

if __name__ == '__main__':
    main()
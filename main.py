# no one can get family member
# get two people cant be same person
#
import random


def main():
    intro()
    txt = open('Santa.txt', 'w')
    for person in everyone:
        fam = find_family(person, family)
        first = random.choice(everyone_pool)
        while first in fam:
            first = random.choice(everyone_pool)
        everyone_pool.remove(first)
        second = random.choice(everyone_pool)
        while second in fam or second == first:
            second = random.choice(everyone_pool)
        everyone_pool.remove(second)
        print('{p}:'.format(p=person))
        print(first)
        print(second)
        print()
        txt.write('{}:\n'.format(person))
        txt.write(first + '\n')
        txt.write(second + '\n' + '\n')
    txt.close()


def intro():
    print('--------------------------')
    print(' Secret Santa Randomize')
    print('--------------------------')


def find_family(person, family_name):
    for fam in family_name:
        if person in fam:
            return fam


gerardi = ['Marcia & Mark', 'Jessica & Tim']
griffith = ['Kristi & James', 'Karen & Rob', 'Dylan', 'Bryan & Olivia']
dexter = ['Dexter & Randy']
anderson = ['Susie', 'Erika']

family = [gerardi, griffith, dexter, anderson]
everyone = [person for surname in family for person in surname]
everyone_pool = everyone + everyone

if __name__ == '__main__':
    main()


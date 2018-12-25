# no one can get family member
# get two people cant be same person
#
import random


def main():
    intro()
    test = open('Santa.txt', 'w')
    for person in e:
        fam = find_family(person, family)
        first = random.choice(everyone)
        while first in fam:
            first = random.choice(everyone)
        everyone.remove(first)

        second = random.choice(everyone)
        while second in fam or second == first:
            second = random.choice(everyone)
        everyone.remove(second)
        print('{p}:'.format(p=person))
        print(first)
        print(second)
        print()
        test.write('{}:\n'.format(person))
        test.write(first + '\n')
        test.write(second + '\n' + '\n')
    test.close()


def intro():
    print('--------------------------')
    print(' Secret Santa Randomize')
    print('--------------------------')


def find_family(person, family_name):
    for fam in family:
        if person in fam:
            return fam


gerardi = ['Marcia & Mark', 'Jessica & Tim']
griffith = ['Kristi & James', 'Karen & Rob', 'Dylan', 'Bryan & Olivia']
dexter = ['Dexter & Randy']
anderson = ['Susie', 'Erika']

family = [gerardi, griffith, dexter, anderson]

everyone = ['Marcia & Mark', 'Jessica & Tim', 'Kristi & James', 'Karen & Rob', 'Dylan', 'Bryan & Olivia', 'Dexter & Randy',
     'Susie', 'Erika', 'Marcia & Mark', 'Jessica & Tim', 'Kristi & James', 'Karen & Rob', 'Dylan', 'Bryan & Olivia', 'Dexter & Randy',
     'Susie', 'Erika']

e = ['Marcia & Mark', 'Jessica & Tim', 'Kristi & James', 'Karen & Rob', 'Dylan', 'Bryan & Olivia', 'Dexter & Randy',
     'Susie', 'Erika']

if __name__ == '__main__':
    main()


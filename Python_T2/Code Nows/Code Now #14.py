verb = raw_input("Enter a verb: ")
print verb

exp = ['be', 'see', 'flee', 'knee']


if verb[-2:] == 'ie':
    print verb.replace('ie','y')+"ing"

if verb in exp:
    print verb+'ing'

    if verb[-1] == 'e':
        print verb.replace('e','ing')

else:
    print verb+'ing'
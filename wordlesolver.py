import cyrtranslit
import regex as re

def filter5chars():
    file1 = open('sr-Latn.txt', 'r')
    Lines = file1.readlines()

    L_lt = []
    L_cr = []

    for line in Lines:
        if len(line) == 6:
            L_lt.append(line.lower())
            L_cr.append(cyrtranslit.to_cyrillic(line.lower(), 'sr'))

    file2 = open('5_chars_words_LT.txt', 'w')
    file2.writelines(L_lt)
    file2.close()
    file4 = open('5_chars_words_CR.txt', 'w')
    file4.writelines(L_cr)
    file4.close()


def onSpot():

    guess_corr = ""
    while True:
        print("Unesi rec sa donjom crtom umesto slova (na mestu): ")
        guess_corr = input()

        if (len(guess_corr) != 5):
            print("Molim te unesi rec od 5 slova!")
        else:
            break

    print("Unesi ostala pogodjena slova koja nisu mestu: ")
    guess_valid = input()
    polu_pogodjena = list(guess_valid)
    print("Unesi slova koja nisu u reči: ")
    slova_nema = input()
    nema_ih = list(slova_nema)
    file3 = open('5_chars_words_LT.txt', 'r')
    Lines = file3.readlines()
    L = []
    re_guess_corr = re.compile("^" + guess_corr.replace("_", ".") + "\n")
    count = 0
    for line in Lines:
        List1 = [e for e in nema_ih if e in line]
        
        if List1:
            continue
        
        List = [e for e in polu_pogodjena if e in line]

        if re.match(re_guess_corr, line):
            if len(List) == (len(guess_valid)):
                print(line)
                count += 1

        
    print(str(count) + " results found.")

filter5chars()
onSpot()

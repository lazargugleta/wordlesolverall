from curses import keyname
import cyrtranslit
import regex as re
import streamlit as st

st.title('Wordle solver for all languages')

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
    guess_corr = st.text_input(label = "Unesi rec sa donjom crtom umesto slova (na mestu): ", key = "str1")

    guess_valid = st.text_input("Unesi ostala pogodjena slova koja nisu mestu: ", key = "str2")
    polu_pogodjena = list(guess_valid)
    slova_nema = st.text_input("Unesi slova koja nisu u reči: ", key = "str3")
    nema_ih = list(slova_nema)
    file3 = open('5_chars_words_LT.txt', 'r')
    Lines = file3.readlines()
    L = []
    Z = []
    re_guess_corr = re.compile("^" + guess_corr.replace("_", ".") + "\n")
    count = 0
    
    
    for line in Lines:
        List1 = [e for e in nema_ih if e in line]
        
        if List1:
            continue
        
        List = [e for e in polu_pogodjena if e in line]

        if re.match(re_guess_corr, line):
            if len(List) == (len(guess_valid)):
                # print(line)
                Z.append(line)
                count += 1

    st.caption("Press enter to update!")
    Z = [sub.replace('\n', '') for sub in Z]
    for i in range(round(len(Z)/10)):
        st.text('   '.join(Z[i*10:i*10+10]))
    st.text(str(count) + " results found.")

filter5chars()
onSpot()

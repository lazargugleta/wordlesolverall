from curses import keyname
import cyrtranslit
import regex as re
import streamlit as st

st.set_page_config(page_title='Wordle solver all languages',page_icon = "wordle.png", layout = 'centered')
col1, col2, col3, col4, col5 = st.columns(5)
with col3:
    st.image('wordle.png', width = 120)
st.title('Wordle solver for all languages')

language = st.selectbox(
     'Please select the language.',
     ('English', 'German', 'Serbian'))

# st.write('You selected:', language)

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

    guess_corr_text = ""
    if language == "English":
        guess_corr_text = "Placed letters"
    elif language == "German":
        guess_corr_text = "Buchstaben platziert"
    else:
        guess_corr_text = "Unesi rec sa donjom crtom umesto slova (na mestu)"
    guess_corr = st.text_input(label = guess_corr_text, key = "str1")

    guess_valid_text = ""
    if language == "English":
        guess_valid_text = "Valid letters"
    elif language == "German":
        guess_valid_text = "Gültige Briefe"
    elif language == "Serbian":
        guess_valid_text = "Unesi ostala pogodjena slova koja nisu mestu"
    guess_valid = st.text_input(guess_valid_text, key = "str2")
    polu_pogodjena = list(guess_valid)
    
    slova_nema_text = ""
    if language == "English":
        slova_nema_text = "Bad letters"
    elif language == "German":
        slova_nema_text = "Schlechte Buchstaben"
    elif language == "Serbian":
        slova_nema_text = "Slova koja nisu u reči"
    slova_nema = st.text_input(slova_nema_text, key = "str3")
    nema_ih = list(slova_nema)
    file_name = ""
    if language == "Serbian":
        file_name = "5_chars_words_LT.txt"
    elif language == "English":
        file_name = "wordle-nyt.txt"
    elif language == "German":
        file_name = "german-5.txt"
    file3 = open(file_name, 'r')
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

    update_text = ""
    if language == "Serbian":
        update_text = "Pritisnite enter da ažurirate!"
    elif language == "English":
        update_text = "Press enter to update!"
    elif language == "German":
        update_text = "Drücken Sie die Eingabetaste, um zu aktualisieren!"
    st.caption(update_text)
    Z = [sub.replace('\n', '') for sub in Z]
    for i in range(round(len(Z)/10)):
        st.text('   '.join(Z[i*10:i*10+10]))
    if len(Z) < 10:
        st.text('   '.join(Z[0:10]))

    results_num_text = ""
    if language == "Serbian":
        results_num_text = " pronađenih rezultata."
    elif language == "English":
        results_num_text = " results found."
    elif language == "German":
        results_num_text = " gefundene Ergebnisse."
    st.text(str(count) + " results found.")

filter5chars()
onSpot()

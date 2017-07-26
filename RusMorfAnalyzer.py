
# -*- coding: utf-8 -*-
import nltk
import pymorphy2
from tkinter.filedialog import *
import tkinter as tk
import fileinput

m = pymorphy2.MorphAnalyzer()


def open_file():
    op = askopenfilename()
    txt.delete(1.0, END)
    for i in fileinput.input(op):
        txt.insert(END, i)


def run_text():
    text = txt.get(1.0, END)
    s = " "
    for i in text:
        if i != "." and i != ")" and i != "(":
            s = s + i
    words = nltk.tokenize.word_tokenize(s)
    yy = int(ent.get(1.0, END))
    y = [w for w in words if len(w) > yy]
    fdist = nltk.FreqDist(y)
    vocab = list(fdist.keys())
    n = 0
    for k in vocab:
        n = n + fdist[k]

    t = ""
    t1 = ""
    i = 0
    q = 0
    u = ""
    sk = ""
    for v in vocab:
        try:
            p = m.parse(v)[0]
            z = str(p.tag)
            a = float(fdist[v] * 100)
            sk = sk + v + '--' + str(round(a / n, 2)) + "%--" + z + "\n"
            i += 1
            l = list(z)[:4]
            st = ""
            for t in l:
                st = st + t
            u = u + st + " "
        except:
            q += 1
            t1 = t1 + v + "\n"
            pass
    u = u.split(' ')
    fdist = nltk.FreqDist(u)
    voc = list(fdist.keys())
    st = ""
    kl = 0
    for c in voc:
        if c != "":
            st = st + "\n" + c + "-" + str(fdist[c])
            kl = kl + fdist[c]

    txt1.delete(1.0, END)
    txt2.delete(1.0, END)
    txt1.insert(1.0, "Quantity of the processed words -" + str(i) + "\n" + sk)
    txt1.insert(1.0, "Frequency distribution tags:" + st + "\n" + "Total tags-" + str(kl))
    txt2.insert(1.0, "Quantity of the not processed words -" + str(q) + "\n" + t1)
    fdist.plot(10)


def run_words_test():
    text = txt1.get(1.0, END)
    s = " "
    for i in text:
        s = s + i
    words = nltk.tokenize.word_tokenize(s)
    sk = " "
    for v in words:
        try:
            p = m.parse(v)[0]
            z = str(p.tag)
            sk = sk + v + "-- " + z + "\n"
        except:
            pass
    txt.delete(1.0, END)
    txt.insert(1.0, "\nTest example-\n" + sk)


def run_lexeme():
    text = txt1.get(1.0, END)
    s = " "
    for i in text:
        s = s + i
    words = nltk.tokenize.word_tokenize(s)
    sk = " "
    for v in words:
        try:
            p = m.parse(v)[0]
            q = str(p.lexeme)
            sk = sk + q + "\n"
        except:
            pass
    txt2.insert(1.0, "\n We receive lexeme -\n" + sk)


def run_normal_form():
    text = txt1.get(1.0, END)
    s = " "
    for i in text:
        s = s + i
    words = nltk.tokenize.word_tokenize(s)
    sk = " "
    for v in words:
        try:
            p = m.parse(v)[0]
            r = p.normal_form
            sk = sk + r + "\n"
        except:
            pass
    txt2.insert(1.0, "\n We receive the initial form of a word-\n" + sk)


def run_words_cases():
    text = txt1.get(1.0, END)
    s = " "
    for i in text:
        s = s + i
    words = nltk.tokenize.word_tokenize(s)
    sk = " "
    sk1 = " "
    a = ['nomn', 'gent', 'datv', 'accs', 'ablt', 'loct', 'voct', 'gen2', 'acc2', 'loc2']
    b = ['sing', 'plur']
    for c in a:
        for v in words:
            try:
                p = m.parse(v)[0].inflect({b[1], c}).word
                sk = sk + p + "\n"
            except:
                pass
    txt2.insert(1.0, " 1. Part of speech -\n" + str(sk1) + "Declination of words on nine cases -\n" + sk)


def p_tag_pos():
    text = txt1.get(1.0, END)
    s = " "
    for i in text:
        s = s + i
    words = nltk.tokenize.word_tokenize(s)
    sk = " "
    for v in words:
        try:
            p = m.parse(v)[0]
            r = p.tag.POS
            sk = sk + r + "\n"
        except:
            pass
    txt2.insert(1.0, "\n 1. Part of Speech:\n" + sk)


def p_tag_animacy():
    text = txt1.get(1.0, END)
    s = " "
    for i in text:
        s = s + i
    words = nltk.tokenize.word_tokenize(s)
    sk = " "
    for v in words:
        try:
            p = m.parse(v)[0]
            r = p.tag.animacy
            sk = sk + r + "\n"
        except:
            pass
    txt2.insert(1.0, "\n 2. Presence of alive soul:\n" + sk)


def p_tag_aspect():
    text = txt1.get(1.0, END)
    s = " "
    for i in text:
        s = s + i
    words = nltk.tokenize.word_tokenize(s)
    sk = " "
    for v in words:
        try:
            p = m.parse(v)[0]
            r = p.tag.aspect
            sk = sk + r + "\n"
        except:
            pass
    txt2.insert(1.0, "\n 3. Kind: perfect or imperfect:\n" + sk)


def p_tag_case():
    text = txt1.get(1.0, END)
    s = " "
    for i in text:
        s = s + i
    words = nltk.tokenize.word_tokenize(s)
    sk = " "
    for v in words:
        try:
            p = m.parse(v)[0]
            r = p.tag.case
            sk = sk + r + "\n"
        except:
            pass
    txt2.insert(1.0, "\n 4. To define case:\n" + sk)


def p_tag_gender():
    text = txt1.get(1.0, END)
    s = " "
    for i in text:
        s = s + i
    words = nltk.tokenize.word_tokenize(s)
    sk = " "
    for v in words:
        try:
            p = m.parse(v)[0]
            r = p.tag.gender
            sk = sk + r + "\n"
        except:
            pass
    txt2.insert(1.0, "\n 5. Sort (man's, female, average):\n" + sk)


def p_tag_involvement():
    text = txt1.get(1.0, END)
    s = " "
    for i in text:
        s = s + i
    words = nltk.tokenize.word_tokenize(s)
    sk = " "
    for v in words:
        try:
            p = m.parse(v)[0]
            r = p.tag.involvement
            sk = sk + r + "\n"
        except:
            pass
    txt2.insert(1.0, "\n 6. Acceptance speaking in action:\n" + sk)


def p_tag_mood():
    text = txt1.get(1.0, END)
    s = " "
    for i in text:
        s = s + i
    words = nltk.tokenize.word_tokenize(s)
    sk = " "
    for v in words:
        try:
            p = m.parse(v)[0]
            r = p.tag.mood
            sk = sk + r + "\n"
        except:
            pass
    txt2.insert(1.0, "\n 7. Inclination (imperative, expression):\n" + sk)


def p_tag_number():
    text = txt1.get(1.0, END)
    s = " "
    for i in text:
        s = s + i
    words = nltk.tokenize.word_tokenize(s)
    sk = " "
    for v in words:
        try:
            p = m.parse(v)[0]
            r = p.tag.number
            sk = sk + r + "\n"
        except:
            pass
    txt2.insert(1.0, "\n 8. Number (unique, multiple):\n" + sk)


def p_tag_person():
    text = txt1.get(1.0, END)
    s = " "
    for i in text:
        s = s + i
    words = nltk.tokenize.word_tokenize(s)
    sk = " "
    for v in words:
        try:
            p = m.parse(v)[0]
            r = p.tag.person
            sk = sk + r + "\n"
        except:
            pass
    txt2.insert(1.0, "\n 9. Person  (1, 2,3):\n" + sk)


def p_tag_tense():
    text = txt1.get(1.0, END)
    s = " "
    for i in text:
        s = s + i
    words = nltk.tokenize.word_tokenize(s)
    sk = " "
    for v in words:
        try:
            p = m.parse(v)[0]
            r = p.tag.tense
            sk = sk + r + "\n"
        except:
            pass
    txt2.insert(1.0, "\n 10.Time (present, past, future):\n" + sk)


def p_tag_transitivity():
    text = txt1.get(1.0, END)
    s = " "
    for i in text:
        s = s + i
    words = nltk.tokenize.word_tokenize(s)
    sk = " "
    for v in words:
        try:
            p = m.parse(v)[0]
            r = p.tag.transitivity
            sk = sk + r + "\n"
        except:
            pass
    txt2.insert(1.0, "\n 11.Transitivity (transitive, intransitive):\n" + sk)


def p_tag_voice():
    text = txt1.get(1.0, END)
    s = " "
    for i in text:
        s = s + i
    words = nltk.tokenize.word_tokenize(s)
    sk = " "
    for v in words:
        try:
            p = m.parse(v)[0]
            r = p.tag.voice
            sk = sk + r + "\n"
        except:
            pass
    txt2.insert(1.0, "\n 12. Pledge (valid, passive):\n" + sk)


def save_file():
    sa = asksaveasfilename()
    x = 'The initial text:\n' + txt.get(1.0, END) +\
        '\n The analysis tegs:\n' + txt1.get(1.0, END) +\
        '\n The not processed words:\n' + txt2.get(1.0, END)
    f = open(sa, "w")
    p = x.encode('utf8')
    f.write(p)
    f.close()


def save_file_w():
    sa = asksaveasfilename()
    x = 'Analyzed words:\n' + txt1.get(1.0, END) + '\n Results of the analysis of words:\n' + txt2.get(1.0, END)
    f = open(sa, "w")
    p = x.encode('utf8')
    f.write(p)
    f.close()


def close_win():
    root.destroy()


def del_all():
    txt.delete(1.0, END)
    txt1.delete(1.0, END)
    txt2.delete(1.0, END)


def del_all_N():
    txt1.delete(1.0, END)
    txt2.delete(1.0, END)


root = tk.Tk()
main_menu = Menu(root)
root.config(menu=main_menu)
file_menu = Menu(main_menu)
main_menu.add_cascade(label="Теги", menu=file_menu)
file_menu.add_command(label="Загрузить текст", command=open_file)
file_menu.add_command(label="Анализ тегов", command=run_text)
file_menu.add_command(label="Сохранить результаты", command=save_file)
file_menu.add_command(label="Очистить все поля", command=del_all)
file_menu.add_command(label="Закрыть програму", command=close_win)
hm = Menu(main_menu)
main_menu.add_cascade(label="Анализ слова часть 1", menu=hm)
hm.add_command(label="Очистить поля для анализа слова", command=del_all_N)
hm.add_command(label="Получить лексему слова", command=run_lexeme)
hm.add_command(label="Получить начальную форму слова", command=run_normal_form)
hm.add_command(label="Склонение слов по шести падежам", command=run_words_cases)
hm.add_command(label="Сохранить результаты", command=save_file_w)
hmh = Menu(main_menu)
main_menu.add_cascade(label="Анализ слова часть 2", menu=hmh)
hmh.add_command(label="Сводные данные о слове", command=run_words_test)
hmh.add_command(label="1.Часть речи", command=p_tag_pos)
hmh.add_command(label="2.Одушевлённость", command=p_tag_animacy)
hmh.add_command(label="3.Вид: совершенный или несовершенный", command=p_tag_aspect)
hmh.add_command(label="4.В каком падеже слово", command=p_tag_case)
hmh.add_command(label="5.Род (мужской, женский, средний)", command=p_tag_gender)
hmh.add_command(label="6.Включенность говорящего в действие", command=p_tag_involvement)
hmh.add_command(label="7.Наклонение (повелительное, изъявительное)", command=p_tag_mood)
hmh.add_command(label="8.Число (единственное, множественное)", command=p_tag_number)
hmh.add_command(label="9.Лицо (1, 2, 3)", command=p_tag_person)
hmh.add_command(label="10.Время (настоящее, прошедшее, будущее)", command=p_tag_tense)
hmh.add_command(label="11.Переходность (переходный, непереходный)", command=p_tag_transitivity)
hmh.add_command(label="12.Залог (действительный, страдательный)", command=p_tag_voice)
lab = tk.Label(root, text="Исходный текст для морфологическогоо анализа ", font="Arial 12")
lab.pack()
txt = tk.Text(root, width=128, height=10, font="Arial 12", wrap=WORD)
txt.pack()
lab1 = tk.Label(root, text="Теги:Результаты анализа тега каждого слова. Анализ слова: Слово для анализа",
                font="Arial 12")
lab1.pack()
txt1 = tk.Text(root, width=128, height=10, font="Arial 12", wrap=WORD)
txt1.pack()
lab2 = tk.Label(root, text="Теги:Слова текста,которые не вошли в анализ.Анализ слова: Результаты", font="Arial 12")
lab2.pack()
txt2 = tk.Text(root, width=128, height=5, font="Arial 12", wrap=WORD)
txt2.pack()
lab3 = tk.Label(root, text="Теги:Пропускать слова корочше устаннновленого значения", font="Arial 12")
lab3.pack()
ent = tk.Text(root, width=5, height=1, font="Verdana 12")
x = 0
ent.insert(END, x)
ent.pack()
root.title("Автоматизированный морфологический анализ")
root.tk.mainloop()

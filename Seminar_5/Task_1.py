# Напишите программу, удаляющую из текста все слова, содержащие ""абв""
file1 = open('C:\\Users\\Михаил\\Desktop\\GB\\Python\\Python\\Seminar_5\\Text.txt', 'r', encoding='UTF-8')
text = file1.read()

def del_words(text):
    list = [i for i in text.split() if 'абв' not in i]
    return " ".join(list)

file =  open('C:\\Users\\Михаил\\Desktop\\GB\\Python\\Python\\Seminar_5\\Text_new.txt', 'w' , encoding='UTF-8')
file.writelines(del_words(text))
file.close()

# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

file1 = open('C:\\Users\\Михаил\\Desktop\\GB\\Python\\Python\\Seminar_5\\Text_for_RLE.txt', 'r', encoding='UTF-8')
text = file1.read()


def coding(text):
    count = 1
    result = ''
    for i in range(len(text)-1):
        if text[i] == text[i+1]:
            count += 1
        else:
            result = result + str(count) + text[i]
            count = 1
    if count > 1 or (text[len(text)-2] != text[-1]):
        result = result + str(count) + text[-1]
    return result

def decoding(text):
    number = ''
    result = ''
    for i in range(len(text)):
        if not text[i].isalpha():
            number += text[i]
        else:
            result = result + text[i] * int(number)
            number = ''
    return result

file2 = open('C:\\Users\\Михаил\\Desktop\\GB\\Python\\Python\\Seminar_5\\Text_after_RLE.txt', 'w', encoding='UTF-8')
file2.writelines(coding(text))
file2.close()
file3 = open('C:\\Users\\Михаил\\Desktop\\GB\\Python\\Python\\Seminar_5\\Text_after_RLE.txt', 'r', encoding='UTF-8')
text2 = file3.read()
print(text)
print(coding(text))
print(decoding(text2))
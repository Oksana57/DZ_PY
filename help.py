text = input('введи текст: ')
if str.isdigit(text):
    print(bin(int(text)), oct(int(text)), hex(int(text)))
elif str.isascii(text):
    print('текст содержит ASCII')
else:
    print('текст содержит не только символы ASCII')
data = open("scientist.txt")
otchet = open("scientist_origin.txt","w")

"""
Чтение данных из текстового файла.
"""

new_data=[i.strip().split("#") for i in data]

"""
Создание массива с прочтенными данными.
"""

for_police=[]
"""
Создание массива для отчета полиции.
"""

for i in range(len(new_data)):
    if new_data[i][1]=="Аллопуринол":
        for_police.append([new_data[i][0],new_data[i][2]])

for_police=sorted(for_police,key=lambda x:x[1])
"""
Наполнение массива данными о людьми, создавшими препарат.

"""
otchet.write("Разработчиками Аллопуринола были такие люди: ")
for i in for_police:
    otchet.write("\n")
    otchet.write(f"{i[0]} {i[1]}")
"""
Все данные о всех врачах вписаны в файл.
"""
otchet.write("\n")
otchet.write("Оригинальный рецепт принадлежит: ")
otchet.write(for_police[0][0])
print(for_police)
"""
Дописана информация о создателе препарата, осуществляется вывод в терминал.
"""



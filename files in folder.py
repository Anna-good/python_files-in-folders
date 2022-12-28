from os import walk #os - библиотека, позволяющая определять тип операционной системы и получать доступ к переменным, а walk возвращает список из 3 элементов
from shutil import move #shutil - бработка файлов и папок, а move - озможность перемещать файлы 

def filenames(dir):
    filenames = []
    for root, dirs, files in walk(dir): #root - окно, но можно любое слово
        for filename in files:
            filenames.append(filename)
    return filenames

def main():
    papka1 = "C:/Users/Небо/Desktop/Новая папка/1"
    papka2 = "C:/Users/Небо/Desktop/Новая папка/2"
    papka3 = "C:/Users/Небо/Desktop/Новая папка/3"
    dir1 = filenames(papka1)
    dir2 = filenames(papka2)
    for file in dir2:
        if file not in dir1:
            move(papka2+'/'+file, papka3+'/')

main()

from random import *
def arvud_loendis():
    print("Данные:")
    n=abs(int(input("Сколько целых чисел генерируем в список? => ")))
    mini=int(input("Введите минимальное число диапазона => "))
    maxi=int(input("Введите максимальное число диапазона => "))
    if mini>maxi:
        mini,maxi=vahetus(mini,maxi)
    s=[]
    generaator(n,s,mini,maxi)
    print()
    print("Результаты:")
    print("Полученный список от",mini,"до",maxi,s)
    s.sort()
    print("Отсортированный список",s)
    pos=neg=null=[]
    jagamine(s,pos,neg,null)
    print("Список положительных элементов",pos)
    print("Список отрицательных элементов",neg)
    print("Список нулевых элементов",null)
    kesk=keskmine(pos)
    lisamine(s,kesk)
    print("Среднее положительных:",kesk)
    kesk=keskmine(neg)
    lisamine(s,kesk)
    print("Среднее отрицательных:",kesk)
    print("Добавляем средние в изначалный массив:")
    s.sort()
    print(s)

def vahetus(a:int,b:int):
    """Kui min suurem kui max, siis vahetame neid omavahel
    :param int a: minimaalne arv
    :param int b: maximaalne arv
    :rtype: int,int
    """
    abi=a
    a=b
    b=abi
    return a,b

def generaator(n:int,loend:list,a:int,b:int):
    """Genereerib juhuslikud täisarvud antud vahemikus
    :param int n: 
    :param list loend: teie loend
    :param int a: minimaalne arv
    :param int b: maksimaalne arv
    """
    for i in range(n):
        loend.append(randint(a,b))
    

def jagamine(loend:list,p:list,n:list,nol:list):
    """Määrab, kas arv on positiivne või negatiivne või null, ja lisab selle vastavasse loendisse
    :param list loend: ühine loend
    :param list p: positiivsete arvude loend
    :param list n: negatiivsete arvude loend
    :param list null: nullidega loend
    """
    for el in loend:
        if el>0:
            p.append(el)
        elif el<0:
            n.append(el)
        else:
            nol.append(el)

def keskmine(loend:list):
    """Leiab loendist arvude keskmise (kui loendi pikkus on 0, siis on ka keskmine väärtus 0)
    :param list loend: teie loend
    :rtype: var
    """
    n=len(loend)
    if n==0: 
        kesk=0 
    else:
        sum=0
        for i in loend:
            sum+=i
        kesk=round(sum/n,2)
    return kesk

def lisamine(loend:list,el:float):
    """Lisab üldisesse loendisse keskmise väärtuse
    :param list loend: teie loend
    :param var el: loendisse lisatav üksus
    """
    loend.append(el)
    loend.sort()

arvud_loendis

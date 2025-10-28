# Учебные задания по Python V6 String and Method

## Внимание начиная с этого задания все репозитариии будут приватными.
Для клонирования в случае остуствия доступа используйте команду:
**git clone https://ваш токен@ссылка на ваш репозиторий**

Выполните следующие задания. Решения для каждого задания пишите в отдельном файле в папке `tasks/`.

---

## Задание 1.
В файле `tasks/task1.py`

Программа получает на вход строку. Ваша задача — вывести все символы этой строки, которые имеют четные индексы.

```
Sample Input 1:
Монти Пайтон

Sample Output 1:
МниПйо

Sample Input 2:
Цой жив!

Sample Output 2:
Цйжв
```
---

## Задание 2. 
В файле `tasks/task2.py` 

Программа получает на вход строку. Ваша задача — вывести все символы этой строки, которые имеют нечетные индексы.

```
Sample Input:
Donald Trump

Sample Output:
oadTup
```
---

## Задание 3.
В файле `tasks/task3.py` 

Программа получает на вход строку. Ваша задача — развернуть строку и вывести ее на экран.

```
Sample Input:
leetcode.com

Sample Output:
moc.edocteel
```
---

## Задание 4.
В файле `tasks/task4.py` 

Программа получает на вход строку.

Выведите каждый третий символ строки в обратном порядке, начиная с последнего.

```
Sample Input 1:
The Big Bang Theory

Sample Output 1:
ye ag T

Sample Input 2:
there is no doubt that money in the form

Sample Output 2:
mfhnyottbdnirt
```
---
## Задание 5.

В файле `tasks/task5.py` 

Программа получает на вход одно слово. Ваша задача — перенести последнюю букву в начало, тем самым сдвинуть все остальные буквы вправо на один разряд. В качестве ответа нужно вывести полученное слово.

```
Sample Input 1:
become

Sample Output 1:
ebecom

Sample Input 2:
come

Sample Output 2:
ecom

Sample Input 3:
qwertY

Sample Output 3:
Yqwert

Sample Input 4:
AbracadabrA

Sample Output 4:
AAbracadabr
```
## Задание 6.

В файле `tasks/task5.py` 

На вход программе поступает строка, состоящая как из заглавных, так и из строчных букв. Ваша задача — преобразовать строку так, чтобы все строчные символы заменились на заглавные, все заглавные - на строчные. Символы пунктуации и цифры не нужно преобразовывать.

В качестве ответа нужно вывести полученную строку.
```
Sample Input 1:
PyThoN besT of The BeST

Sample Output 1:
pYtHOn BESt OF tHE bEst

Sample Input 2:
Я у мАмы ХацКер

Sample Output 2:
я У МаМЫ хАЦкЕР

Sample Input 3:
lED zEPPELiN

Sample Output 3:
Led ZeppelIn
```
## Задание 7.

В файле `tasks/task7.py` 

На вход программе поступает строка, состоящая как из заглавных, так и из строчных букв. Ваша задача — преобразовать строку так, чтобы первая буква у каждого слова стала маленькой, а остальные буквы превратились в заглавные. Символы пунктуации и цифры не нужно преобразовывать.
В качестве ответа нужно вывести полученную строку.

```
Sample Input 1:
Every You Every Me

Sample Output 1:
eVERY yOU eVERY mE

Sample Input 2:
RunnING up That HILL

Sample Output 2:
rUNNING uP tHAT hILL

Sample Input 3:
Sleeping with GHOSTS

Sample Output 3:
sLEEPING wITH gHOSTS
```
## Задание 8.

В файле `tasks/task8.py` 

На вход программе поступает строка, ваша задача — вывести на экран индекс последней найденной латинской буквы a.
Если такого символа во введенной строке нет, выведите значение -1.

```
Sample Input 1:
banana

Sample Output 1:
5

Sample Input 2:
cat

Sample Output 2:
1

Sample Input 3:
zoo

Sample Output 3:
-1
```

## Требования
1. Используйте только то, что мы изучили (переменные, ввод `input`, срезы, методы строк).
2. Решения пишите в отдельных файлах в папке `tasks/`.
3. Проверка идёт автоматически через автотесты.

## Не забудь команды для git:
```
git clone -клонировать репозитарий
git status - проверить состояние файлов перед индексом и коммитом
git add <имя файла> - добавить файл в индекс
git commit -m"собщение" - добавить файлы и собщение в репозитарий
git push origin main- "запушить" отправить репозитарий на удаленный сервер (Github)
```
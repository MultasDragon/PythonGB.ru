# Командная строка linux
1. [[##Команды для установки программ]]
	1. [[##Распространенные программы]]
	2. [[##Редакторы текста]]
2. [[##Ключи общего назначения]]
3. [[##Горячие клавиши и команды для окна терминала]]
4. [[##Управление и переходы по директориям файлам]]
5. [[##Просмотровщики текстовые]]

## Команды для установки программ
- `sudo` - запуск команд справа от `sudo` от имени администратора ^sudo
- `apt` - ^apt
- `install` - ^install
- ^update
- ^upgrade
### Распространенные программы
- ^perl
- ^make
- ^gcc
- ^mc
- ^open-vm-tools
### Редакторы текста
- `nano` - запускает редактор текста Nano: `nano +200,15 some_file.txt` - запускает файл `some_text.txt` на `200`ой строке, `15`ый символ ^nano
	- Комбинация клавиш `ctrl`+`c` - вывод помощи
	- Комбинация клавиш `ctrl`+`x` - выход из программы
	- Комбинация клавиш `ctrl`+`o` - записать файл
	- Комбинация клавиш `ctrl`+`k` - вырезать в буфер обмена
	- `-b` - открывает файл с бекапом изначальным - бэкап сохраняется с тильдой в конце
- `vim` - запускает редактор текста Vim. ^vim
	- `:q!` или `:q` - выход из программы	
	- `:w` - сохранить
	- Клавиша `i` - редактирование, отображается как вставка
	- Клавиша `Esc` - выход из режима редактирования
	- `d`  - вырезать строку или `8d` - вырезать 8 строк
	- `p` - вставить из буфера обмена
	- `u` - отменить действие
	- `w` - сместиться вправо
	- `h` - сместиться влево
	- `j` - сместиться на строку ниже
	- `k` - сместиться на строку выше

- `systemctl` - Специальная команда для управления службами SSH ^systemctl
- ^openssh-server
- ^hostnamestl

## Ключи общего назначения
- Ключ `-y` - передает командам всегда подтверждать запрос во время выполнения ^-y
- ^-a
- Ключ `--help` - сообщает доступную справочную информацию по каждому оператору, после которого использована "`more --help`" ^--help

## горячие клавиши и команды для окна терминала
- `clear` - скроллит экран вверх - чтобы не было видно бардака - очищает видимую часть экрана от записей ^clear
- Комбинация клавиш `ctrl`+`u` - стирает всё что написано в строке слева от курсора ^ctrl-u
- Комбинация клавиш `ctrl`+`k` - стирает всё что написано в строке справа от курсора ^ctrl-k
-  Комбинация клавиш `ctrl`+`l` - то же самое, что и ![[Commands##^clear]] ^ctrl-l
- `reset` - очищает полностью всё введенное в окно терминала и перегружает терминал - сбрасывая настройки ^reset
- `history` - выводит все введенные команды ^history
- ^uname
- ^cat
- ^lsb-release

## Управление и переходы по директориям, файлам
- `man` - сообщает подробный мануал по команде указанной дальше ^man
- `pwd` - сообщает адрес папки, где мы находимся (образовано от аббревиатуры print working directory) ^pwd
- `cd` - перемещается в указанную директорию: "`cd /home/student`" - переместит в папку `student` в папке `home`, можно указывать "`cd ..`" или "`cd ../`" - перемещает на уровень выше, при достижении потолка не переместится, "`cd /`" - переместит в корневой каталог, "`cd ~`" - переместит в домашний каталог `/home/student` ^cd
- `ls` - выводит список файлов, папок в текущем местонахождении через tab ^ls
	- `ls -l` - выводит список файлов и папок в виде таблицы, имена будут находиться в последней колонке
	- `ls -a` - выводит в том числе скрытые файлы и папки
	- `ls /home` - выводит список файлов по указанному пути
- `ll` - то же самое, что `ls -la` ^ll
- `mkdir` - создает директории с именами введенными после `mkdir` через пробел: `mkdir lesson1 lesson2 lesson2` ^mkdir
	- `mkdir 2/3/4 -p` - создаёт директории с уровнем вложенности указанном справа от `mkdir`
	- `mkdir` нельзя применять в корневой папке без прав админа - то есть надо применять команду `sudo mkdir /myt` -  только в этом случае он разрешит ее там создавать
- `touch` - создает файл поименованный словыми правее команды `touch`: `touch new.txt`^touch
- `>` - создает файл поименованный словыми правее знака `>`: `> new2.txt` ^rght
- `echo` - выводит на печать в командной строке всё что правее, если необходимы спец-символы - можно заключить в кавычки " или ' : `echo "Hello world"` ^echo
	- `echo Hello world > new.txt` - запишет слова "Hello world" в файл new.txt, который создаст в той папке, из которой был запущен
- `tree` - показывает в псевдографическом виде дерево каталогов, может быть потребует установку командой `sudo apt install tree` ^tree
- `cp` - копирует файл в первом указании в каталог во втором указании: `cp file1.txt folder1/` ^cp
	- `cp folder1/ 2/3/ -r` -ключ `r` позволяет копировать каталоги
- `mv` - перемещает файл в первом указании в каталог во втором указании: `mv file1.txt folder1/` ^mv
	- если вместо второго указания указать другое имя файла - он переименует файл из первого указания во второе: `mv file1.txt filokadavr`
- `rm` - удаляет файлы по маске указанной правее `rm` - "`rm *.txt`" - удалит все *.txt* файлы из текущей папки ^rm
	- `rm f* -r` - удалит все каталоги и файлы из текущей директории благодарю ключу `r` (рекурсивно)
### Просмотровщики текстовые
- `more` - текстовый просмотрщик ^more
- `whatis` - ^whatis
- `less` - продвинутый текстовый просмотрщик ^less
	- `-N` - пронумеровать строки
	- `-I` - поиск вне зависимости от регистра
	- `-p`
- `head` - просмотрщик первых десяти строк ^head
- `tail` - просмотрщик последних десяти строк ^tail
	- `-f` - поставляет данные в режиме реального времени (часто для логирования данных)
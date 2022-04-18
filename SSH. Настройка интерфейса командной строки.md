[[linux]] [[SSH]] [[file_management]]
[[Commands#^systemctl|systemctl]], [[Commands#^enable|enable]], [[Commands#^status|status]], [[Commands#^hostname-I|hostname -I]], [[Commands#^ip-addr|ip addr]], [[Commands#^whoami|whoami]], [[Commands#^echo|echo]], [[Commands#^clear|clear]]
[[_TOC_]]

### Main programm
##### Работа по протоколу SSH
``` mermaid
graph TB

main[Основная машина]
cloud[Машина в облаках]

``` 
``` mermaid
sequenceDiagram

main->>+cloud: auth_key - auth_key.pub
cloud->>main: Response from cloud access
main->>cloud: команда по SSH
cloud->>main: результат выполнения (если есть)
```
1. Установить ssh client на облачной машине
2. `sudo apt update`
3. Enter adsudsmin password 
4. Установка пакета `sudo apt install openssh-server -y`
5. Чтобы его запустить `sudo systemctl start ssh` 
6. Чтобы установить в автозагрузку `sudo systemctl enable ssh`
7. Проверить статус SSH `systemctl status ssh`
8. Узнать IP address `ip addr`, `hostname -I`
9. Могут быть проблемы, если не настроены сетевые свойства ![[VirtualBox#^network-preferences]] ![[VmWare]]
10. ![[MobaXterm#^ssh-connection]] ![[Putti#^start-ssh]] ![[Windows#^ssh]] ![[Windows#^trouble-shutting]]
##### Команды для работы с файлами и папками
1. ![[Commands#^echo]]
2. ![[Commands#^clear]]
3. ![[Commands#^ctrl-u]]
4. ![[Commands#^ctrl-k]]
5. ![[Commands#^ctrl-l]]
6. ![[Commands#^reset]]
7. ![[Commands#^pwd]]
8. ![[Commands#^cd]]
9. ![[Commands#^ls]]
10. ![[Commands#^ll]]
11. ![[Commands#^history]]
12. ![[Commands#^mkdir]]
13. ![[Commands#^touch]]
14. ![[Commands#^rght]]
15. ![[Commands#^tree]]
16. ![[Commands#^cp]]
17. ![[Commands#^mv]]
18. ![[Commands#^rm]]
##### Текстовые просмотровщики и редактора
###### Просмотровщики
1. ![[Commands#^--help]]
2. ![[Commands#^more]]
3.  ![[Commands#^man]]
4. ![[Commands#^whatis]]
5. ![[Commands#^less]]
6. ![[Commands#^head]]
7. ![[Commands#^tail]]
###### Редакторы nano и vim
1. ![[Commands#^nano]]
2. Установить vim:
`sudo apt install vim`
`sudo apt install vim-runtime`
3. ![[Commands#^vim]]
4. Инструкция по vim - `vimtutor ru`  на русском языке

### Home task
1. Создать каталоги students и mentors в домашней директории, а в них - текстовые файлы students_list.txt и mentors_list.txt соответственно
2. Открыть созданные в п.1 файлы в любом текстовом редакторе и заполнить их (в соответствии с названием) списком Ваших одногруппников и наставников на данном потоке.
3. Переместите файл mentors_list.txt в папку students.
4. Удалите папку mentors.
5. Переименуйте папку students в students_and_mentors
6. Удалите папку students_and_mentors вместе с содержимым
7. Подключитесь к машине с Linux по протоколу SSH.
8. (\*) Используя дополнительный материал, настроить авторизацию по SSH с использованием ключей.
В качестве решения необходимо прислать текстовый файл (\*.txt) с набором используемых команд и их результатами (можно скопировать текст из консоли)

```cmd
makedir students mentors
> students/students_list.txt
> mentors/mentors_list.txt
Анисимов >> students/students_list.txt
mv mentors/mentors_list.txt students/
rm mentors
mv students students_and_mentors -r
ssh abu@192.168.40.23
123
```
# Vista Med
Для запуска приложения необходимо установить <b>MySQL!</b>

Далее для корректного запуска необходимо в файле main.py вместо "*" вставить данные своей DB в 7 строке, а именно: 

<code> user = "*", password = "*", database = "*****" </code>

После чего данный проет необходимо собрать через <b>pyinstaller</b>.
<h3>Установка pyinstaller через pip</h3>
<code>apt pip3 install pyinstaller</code>
<h3>Сборка проекта через pyinstaller</h3>
<code>pyinstaller --onefile  main.py</code>

Всё готово! Можно пользоваться приложением, которое находится в папке <b>dist</b>

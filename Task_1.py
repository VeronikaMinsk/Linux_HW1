# Задание 1.
#
# Условие:
# Написать функцию на Python, которой передаются в качестве параметров команда и текст.
# Функция должна возвращать True, если команда успешно выполнена и текст найден в её выводе и False в противном случае.
# Передаваться должна только одна строка, разбиение вывода использовать не нужно.

import subprocess
import re

def execute_and_check(command, text_to_find):
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
        if result.returncode == 0:
            pattern = re.compile(r'\b{}\b'.format(re.escape(text_to_find)))
            if pattern.search(result.stdout):
                return True
        return False
    except Exception as e:
        print(f"Ошибка при выполнении команды: {str(e)}")
        return False

command_to_execute = "cat /etc/pnm2ppa.conf"
text_to_find = "suppress bidirectional printing"

if execute_and_check(command_to_execute, text_to_find):
    print(f"True. Текст '{text_to_find}' найден в выводе команды.")
else:
    print(f"False. Текст '{text_to_find}' не найден в выводе команды или команда не была успешно выполнена.")

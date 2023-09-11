# Задание 2. (повышенной сложности)
#
# Доработать функцию из предыдущего задания таким образом, чтобы у неё появился дополнительный режим работы,
# в котором вывод разбивается на слова с удалением всех знаков пунктуации (их можно взять из списка string.punctuation модуля string).
# В этом режиме должно проверяться наличие слова в выводе.


import subprocess
import string

def execute_and_check(command, text_to_find, check_word_mode=False):
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)

        if result.returncode != 0:
            return False, []

        if check_word_mode:
            output_without_punctuation = result.stdout.translate(str.maketrans('', '', string.punctuation))

            words_without_punctuation = output_without_punctuation.split()

            if text_to_find in words_without_punctuation:
                return True, words_without_punctuation
            else:
                return False, words_without_punctuation
        else:

            if text_to_find in result.stdout:
                return True, []

        return False, []
    except Exception as e:
        print(f"Ошибка при выполнении команды: {str(e)}")
        return False, []

command_to_execute = "cat /etc/pnm2ppa.conf"
text_to_find = "GammaIdx"
check_word_mode = True

found, words_without_punctuation = execute_and_check(command_to_execute, text_to_find, check_word_mode)

if found:
    print(f"True. Текст '{text_to_find}' найден в выводе команды.")
    if words_without_punctuation:
        print("Разбитые слова без пунктуации:", words_without_punctuation)
else:
    print(f"False. Текст '{text_to_find}' не найден в выводе команды или команда не была успешно выполнена.")

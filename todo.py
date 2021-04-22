#импорт библеотек



TOKEN = ""

HELP = """
help - вывод списка команд
add - добавление 
show - показать все задачи 
done - задача выполнена
"""
todo = {}

print("Привет! Введите команду help для вывода списка команд")

while True:
  userAnswer = input("Введите команду:\n")

  if userAnswer == "add":
   print('Работает!')
  elif userAnswer == "help":
    print('Работает!')
  elif userAnswer == "show":
    print('Работает!')
  elif userAnswer == "done":
    print('Работает!')
  elif userAnswer == "exit":
    print('Работает!') 
  else:
    print("Error.Нет такой команды")   
    print("Введите help для вывода списка команд")



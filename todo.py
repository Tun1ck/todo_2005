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
   userDate = input("введите дату:\n") 
   userTask = input("Что нужно сделать?\n")


   todo[userDate] = userTask
   print(f"На{userDate}число добавлена задача'{userTask}'")
  elif userAnswer == "help":
    print(HELP)
  elif userAnswer == "show":
    print('Работает!')
  elif userAnswer == "done":
    print('Работает!')
  elif userAnswer == "exit":
    break
  else:
    print("Error.Нет такой команды")   
    print("Введите help для вывода списка команд")



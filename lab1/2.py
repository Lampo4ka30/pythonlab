from sys import argv
dictionary = {'add': '+', 'subtract': '-', 'multiply': '*', 'divide': '/'}
try:
    print(eval(argv[2]+dictionary[argv[1]]+argv[3]))
except ValueError:
    print("The script should be launched like this:\n >>python my_task.py add 1 2")
except Exception:
    print("The script should be launched like this:\n >>python my_task.py add 1 2")
else:
    print("Good work, Oleg.")
finally:
     print("Goodbye.")
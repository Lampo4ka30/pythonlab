from sys import argv
try:
    print(eval(' '.join(argv[1:])))
except ValueError:
    print("The script should be launched like this:\n >>python my_task.py 1 * 2")
except Exception:
    print("The script should be launched like this:\n >>python my_task.py 1 * 2")
else:
    print("Good work, Oleg.")
finally:
     print("Goodbye.")
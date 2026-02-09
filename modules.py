# A module is simply a Python file (.py) that contains code you can reuse — like functions, variables, or classes.
#Core Module     #when you import something it is already build by someone(pre-build)
#datetime.datetime.now() gives you the current date and time.
#datetime.datetime.now().time() gives you only the time.

# datetime
import datetime

today=datetime.date.today()#date
month=datetime.date. today().month
day=datetime.date.today().day
time=datetime.datetime.now().time()
#math
import math
#pip modules





print(today)
print(month)
print(day)
print(time)
print(math.sqrt(25))
print(math.sqrt(9))
print(math.sqrt(64))
print(math.pi)

#pip-Installs Packages and manage external modules or libraries that are not built into Python.
import camelcase

c = camelcase.CamelCase()
text = "hello kabelo"
print(c.title(text))



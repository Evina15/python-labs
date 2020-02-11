'''
Write a script that demonstrates a try/except/else.

'''

try:
    for i in range(5):
        var = error_var
except NameError as ne:
    print(ne)
except Exception:
    print("Uh oh, something went terribly wrong!")
else:
    print("Hello how are you today?")

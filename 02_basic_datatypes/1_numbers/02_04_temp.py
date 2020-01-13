'''
Fahrenheit to Celsius:

Write the necessary code to read a degree in Fahrenheit from the console
then convert it to Celsius and print it to the console.

    C = (F - 32) * (5 / 9)

Output should read like - "81.32 degrees fahrenheit = 27.4 degrees celsius"


'''
fahrenheit = float(input("Please enter the degree in Fahrenheit: "))
celcius = round(((fahrenheit-32)*5/9),2)
print(fahrenheit, "degree fahrenheit = " , celcius, "degree celcius")

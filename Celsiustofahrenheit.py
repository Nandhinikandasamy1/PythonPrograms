'''You are given with a number A i.e. the temperature in Celcius. Write a program to convert this into Fahrenheit. 

Note: In case of decimal values, round-off to two decimal places.'''

Celcius =int(input())
fahrenheit = (Celcius * 1.8) + 32
print(round(fahrenheit,2))

# Задача 1. Создайте файл. Запишите в него N первых
# элементов последовательности Фибоначчи.
# 6 –> 1 1 2 3 5 8 
def fibonacci(q):
   result = [1,1]
   for i in range(2,q):
      fib=result[i-1]+result[i-2]
      result.append(fib)
   return(result)
print('Задайте количество первых элементов')
number=int(input(' последовательности Фибоначчи:  '))
fibonacci_result= str(fibonacci(number))
data = open('Fibonacci.txt', mode = 'w')
data.writelines(fibonacci_result)
data.close()
# print(f'Ряд Фибоначчи {fibonacci(number)}')
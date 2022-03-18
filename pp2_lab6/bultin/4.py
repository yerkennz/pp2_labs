from time import sleep
import math
def f(fn, ms):
  sleep(ms / 1000)
  return math.sqrt(fn)
print("Square root after specific miliseconds:") 
print(f(100, 10000))
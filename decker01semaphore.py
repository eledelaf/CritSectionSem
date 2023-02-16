# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 12:23:35 2023

@author: marla
"""

from multiprocessing import Process
# from multiprocessing import current_process
from multiprocessing import Value #Array
import threading
import time
import random 

# lock = threading.Lock()
# sem = threading.Semaphore(1)
N = 8

def task(common, tid, turn):
     sem = threading.Semaphore(1)
     for i in range(10):
         print(f"{tid}−{i}: Non−critical Section", flush=True)
         time.sleep(random.random()) # Para no entrar continuamente en la seccion critica 
         print(f"{tid}−{i}: End of non−critical Section", flush=True)
         print("\n")
         ######## SECCION CRITICA ########
         sem.acquire()
         print(f"{tid}−{i}: Critical section", flush=True)
         v = common.value + 1
         print(f"{tid}−{i}: Inside critical section", flush=True)
         common.value = v
         print(f"{tid}−{i}: End of critical section", flush=True)
         print("\n")
         turn.value = (tid + 1) % N
         sem.release()
     
     
def main():
     lp = []
     common = Value("i", 0)
     turn = Value("i", 0)
     for tid in range(N):
         lp.append(Process(target=task, args=(common, tid, turn)))
     print (f"Valor inicial del contador {common.value}")
     for p in lp:
         p.start()
     for p in lp:
         p.join()
     print (f"Valor final del contador {common.value}")
     print ("fin")
if __name__ == "__main__":
     main()

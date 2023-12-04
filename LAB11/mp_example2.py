from memory_profiler import profile
import random

@profile
def main_fun():
    arr1=[random.randint(1,10) for i in range(100000)]
    arr2=[random.randint(1,10) for i in range(100000)]
    arr3= [arr1[i]+arr2[i] for i in range(100000)]

    del arr1
    del arr2
    total= sum(arr3)
    
    del arr3
    print(total)
    
if __name__=="__main__":
    main_fun()
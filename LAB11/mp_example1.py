##Example 1
from memory_profiler import profile

@profile
def defFunc():
    var1= [1]*(6**4)
    var2= [1]*(2**3)
    var3= [2]*(4*6**3)
    
    del var3
    del var1
    return var2
if __name__=="__main__":
    defFunc()
    print("We have successfully inspectd memory usage from")
    
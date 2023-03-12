import time
start_time=time.time()
li=[1,3,4,5,6,1000000000000000000000000000000000000000000000000000,2000000000000000000000000000000000000000000]

def sumi():
    sum=0
    for num in li:
        sum=sum+num
        print(sum)
sumi()
end_time=time.time()    
print(abs(start_time-end_time))
import random
import time
import sys

def main():


    looperCPU = 500
    start = time.time()
    while (looperCPU != 0):
        #start = time.time()

        #this is the computation for 3 secs
        time.sleep(3)
        random_number = random.randint(0,1000)

        #Send to printer for processing
        #.75 secs to 4.75 secs to generate a pause before printing
        secondsPause = random.uniform(.75,4.75)


        #This is the printer function
        printerLooper = True
        while printerLooper == True :
            print("Sleeping for ", secondsPause, " seconds")
            print(random_number)
            printerLooper = False


        #
        print("total time taken this loop: ", time.time() - start)
        looperCPU -= 1    



main()

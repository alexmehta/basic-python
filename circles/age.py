import os
import random
from datetime import datetime
import asyncio
now = datetime.now()
import time

name = input( "Whats's your name sir/madam? " )

def age_valid():





    print( "Hello " + name + ", please proceed!" )

    # gets users birthday and converts it to an age
    age_yr = int( input( "What year were you born? " ) )
    actual_age = int( now.year ) - int( age_yr )
    age_diff = int( 13 ) - actual_age
    if actual_age>=13:
        print(f"your age is {actual_age} and you are permitted to be here")
        time.sleep(10)
        pi()

    else:
        print("you are not allowed in here")
def pi():
    x = 100
    num_point_circle=0
    num_point_total=0
    for _ in range(x):
        x=random.uniform(0,1)
        y=random.uniform(0,1)
        distance=x**2+y**2
        if distance <= 1:
            num_point_circle+=1
        num_point_total+=1

        return 4*num_point_circle/num_point_total







age_valid()
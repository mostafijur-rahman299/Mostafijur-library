import random

#randint function
number = random.randint(1,100)
print(number)

#range function
number = random.randrange(10)
print(number)

number = random.randrange(5,10)
print(number)

number = random.randrange(10,100,10)
print(number)

"""
random it can't take any argument
it give floting point number 0.0 upto 1.0
"""
number = random.random()
print(number)

"""
The uniform function also returns
a random floating-point number,
but allows you to specify the range
of values to select from
"""
number = random.uniform(10,20)
print(number)

"""
In this example, the value 10 is
specified as the seed value. If a
program calls the random.seed function,
passing the same value as an argument each
time it runs, it will always produce the
same sequence of pseudorandom number
"""
random.seed(10)

#sample function
print(random.sample("erer3434343jkrjekrjererj",6))

import string
random_generate = (random.choice(string.ascii_lowercase + string.digits)for _ in range(10))

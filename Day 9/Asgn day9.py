# %%
#part 1
import numpy as np
# Part 1
def random_num():
    sum=0
    n=np.random.randint(1,101)
    while(n>0):
        a = n%10
        sum=sum+a
        n = n//10
    return sum


print(random_num())

# %%
# Part 2

# someone approaches you saying i will give you 5$ if you get 7 and take 1 $ if you get a number other that 7
# How do we know what will happen? Our own "Monte Cralo Simulation" like function 

def monte_carlo  (runs=1000):
    results = np.zeros(2) # Array results[0] and results[1] inittialized to two zeroes
    for _ in range(runs):
        if random_num() > 12:
            results[0] += 1
        else:
            results[1] += 1
    return results

print(monte_carlo())
print(monte_carlo())
print(monte_carlo())

# Results may be favourable to us, but was that by luck?

# %%
#Part 3

# Now do it for 1000 times
results = np.zeros(1000)

for i in range(1000):
    results[i] = monte_carlo()[0]
print(results)

import matplotlib.pyplot as plt 
fig, ax = plt.subplots()
ax.hist(results, bins=15)
plt.show()

print(results.mean())           # General mean
print(results.mean()*3)         # What we will get as win on an average
print(1000 - results.mean())    # What we will pay on an average
print(results.mean()/1000)      # Probability of the 'we will pay' result

# The last probability should be close to the theouretical probability of gettin a 7 when we throw two dice




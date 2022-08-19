import matplotlib.pyplot as plt

x = [200000,1000000,5000000,10000000,20000000]
y = [0.0, 
    0.0,
    0.0, 
    0.25,
    0.5]

plt.plot(x,y, "b")
plt.xlabel("Inputs")
plt.ylabel("Time Taken")
plt.title("Jump Search")
plt.show()

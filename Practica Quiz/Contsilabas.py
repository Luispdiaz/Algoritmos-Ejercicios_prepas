x = "Outside of that, Hu argues that the royalties can be more reliable than the entropy of Wall Street. No matter what happens to the stock market, people are always going to be listening to music."
y = "CBD, which comes from either a marijuana or hemp plant, is non-psychoactive, so it won’t get you high like THC (tetrayhydrocannabinol). It may, however, offer anti-inflammatory, antioxidant, anti-psychotic, anti-convulsant, and antidepressant properties. Because it can hemp is legal in all 50 states, hemp-derived CBD products are becoming more readily available online and in stores all over the country."
z = "According to a report published by Fast Company, apparel sales have plummeted by 50 percent. It’s a margin that will be difficult to recover from, especially for small businesses that don’t have the backing of major conglomerates. These independent companies rely on seasonal buys from retailers to stay afloat. But with the bevy of store closures and restrictions on online sales, these behemoth retailers are facing hard times of their own."
print("En x:")
cont1=0
for i in range(len(x)):
    if ((x[i].lower() == "a") and (x[i+1].lower() == "t")):
        cont1 += 1
        print(f"EL indice es {i}-{i+1}")
print("Repeticiones" , cont1)
print("En y:")
cont2 = 0
for i in range(len(y)):
    if y[i] == "o" and y[i+1] == "m":
        cont2 += 1
        print(f"El indice es {i}-{i+1}")
print(f"Las repeticiones son {cont2}")
print("En z:")
cont3 = 0
for i in range(len(y)):
    if z[i] == "i" and z[i+1] == "n":
        cont3 += 1
        print(f"El indice es {i}-{i+1}")
print(f"Las repeticiones son {cont3}")

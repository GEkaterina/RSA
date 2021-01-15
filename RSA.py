p=3# известное число
g=7 # известное число число
n = p*g
print("n:", n)

f= (p-1) * (g-1)
print("Функция Эйлера:", f)

e=5
d= (2 * f + 1) /e
print("d:", round(d))

print("\n" + "Bob")
M = 19
c= M**e % n
print("Сообщение:", M)
print("Зашифрованное сообщение:", c)

m = c**d % n
print("\n" + "Alice")
print("Расшифрованное:", m)
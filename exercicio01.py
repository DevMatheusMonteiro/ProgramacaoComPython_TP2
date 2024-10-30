people = {'Alice': 22, 'Bob': 17, 'Carol': 19, 'David': 16}
adults = {}
for name, age in people.items():
    if(age >= 18):
        adults[name] = age
print(adults)
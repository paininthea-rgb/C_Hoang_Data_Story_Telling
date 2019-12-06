import matplotlib.pyplot as plt 

people = [3944, 1826 ]
gender = ['MEN quantity - 3944', 'FEMALE quantity - 1826']
colors = ['blue', 'yellow']

plt.title("Men and Women who earn Olympic medals from 1896-2016")
plt.pie(people, labels=gender, colors=colors, startangle=90)
plt.show()
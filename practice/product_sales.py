import matplotlib.pyplot as plt
import random as rnd

products = ['Face Cream', 'Face Wash', 'Toothpaste', 'Shampoo', 'Conditioner', 'Deodorant']
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

#product sales
# Face_Cream_sales = [2500, 2700, 3000, 2800, 3200, 4000, 4200, 3800, 3600, 3900, 4100, 4500]
# Face_Wash_sales = [1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600]
# Toothpaste_sales = [3500, 3600, 3700, 3800, 3900, 4000, 4100, 4200, 4300, 4400, 4500, 4600]
# Shampoo_sales = [2000, 2200, 2400, 2600, 2800, 3000, 3200, 3400, 3600, 3800, 4000, 4200]
# Conditioner_sales = [1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900]
# Deodorant_sales = [1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300]

Face_Cream_sales = [rnd.randint(2000,5000) for _ in range(12)]
Face_Wash_sales = [rnd.randint(1000,3000) for _ in range(12)]
Toothpaste_sales = [rnd.randint(3000,6000) for _ in range(12)]
Shampoo_sales = [rnd.randint(1500,4500) for _ in range(12)]
Conditioner_sales = [rnd.randint(1000,3500) for _ in range(12)]
Deodorant_sales = [rnd.randint(800,2500) for _ in range(12)]   



plt.title('Monthly Product Sales Data')
plt.xlabel('Month')
plt.ylabel('Sales Units')

# plt.plot(months, Face_Cream_sales, marker='o')
# plt.plot(months, Face_Wash_sales, marker='o')
# plt.plot(months, Toothpaste_sales, marker='o')
# plt.plot(months, Shampoo_sales, marker='o')
# plt.plot(months, Conditioner_sales, marker='o' )
# plt.plot(months, Deodorant_sales, marker='o' )

plt.plot(months, Face_Cream_sales, marker='o', label='Face Cream Sales')
plt.plot(months, Face_Wash_sales, marker='o', label='Face Wash Sales')
plt.plot(months, Toothpaste_sales, marker='o', label='Toothpaste Sales')
plt.plot(months, Shampoo_sales, marker='o', label='Shampoo Sales')
plt.plot(months, Conditioner_sales, marker='o', label='Conditioner Sales')
plt.plot(months, Deodorant_sales, marker='o', label='Deodorant Sales')

plt.xticks(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], [1,2,3,4,5,6,7,8,9,10,11,12])
plt.xticks(rotation=45)

plt.grid()
plt.legend()
plt.show()



plt.scatter(months, Face_Cream_sales, color='red', label='Toothpaste Sales')
plt.title('Toothpaste Sales Data')
plt.xlabel('Month')
plt.ylabel('Number of units sold')
plt.xticks(rotation=45)
plt.grid()
plt.legend()
plt.show()



# plt.pie()
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('company_sales_data - company_sales_data.csv')

# months = df['month_number']
# face_cream_sales = df['facecream']
# face_wash_sales = df['facewash']
# toothpaste_sales = df['toothpaste']
# bathingsoap_sales = df['bathingsoap']
# shampoo_sales = df['shampoo']
# moisturizer_sales = df['moisturizer']


# products = ['Face Cream', 'Face Wash', 'Toothpaste', 'Bathing Soap', 'Shampoo', 'Moisturizer']
# month_names = ['January', 'February', 'March', 'April', 'May', 'June', 
#                'July', 'August', 'September', 'October', 'November', 'December']

# plt.title('Monthly Product Sales Data')
# plt.xlabel('Months')
# plt.ylabel('Sales Units')


df.plot(
    x='month_number', y=['facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo', 'moisturizer'],
    kind='line', marker='o')

# plt.plot(months, face_cream_sales, marker='o', label='Face Cream')
# plt.plot(months, face_wash_sales, marker='o', label='Face Wash')
# plt.plot(months, toothpaste_sales, marker='o', label='Toothpaste')
# plt.plot(months, bathingsoap_sales, marker='o', label='Bathing Soap')
# plt.plot(months, shampoo_sales, marker='o', label='Shampoo')
# plt.plot(months, moisturizer_sales, marker='o', label='Moisturizer')

# plt.xticks(months, rotation=45)

plt.grid()
plt.legend()
plt.show()




#2nd Plot - Toothpaste Sales Data
df.plot(
    x='month_number', y=['toothpaste','facecream'],kind='line', marker='o', legend=True
    )

# plt.scatter(months, toothpaste_sales, color='red', label='Toothpaste Sales')
# plt.title('Toothpaste Sales Data')
# plt.xlabel('Months') 
# plt.ylabel('Sales Units')
# plt.xticks(months, rotation=45)
plt.grid()
# plt.legend()
plt.show()


#3rd Plot - facecream & fashwash Sales Data
# plt.bar(months, face_cream_sales, label='Face Cream')
# plt.bar(months, face_wash_sales, label='Face Wash')
# clear current axes and draw grouped bars side-by-side

# easier: let pandas draw grouped bars for you
# df.set_index('month_number')[['facecream', 'facewash']].plot(kind='bar', rot=45)

# df.plot(
#     x='month_number', y=['facecream', 'facewash'],
#     kind='bar',
#     color=['purple', 'orange'],
#     # width=0.8,
#     grid=True,
# )

# plt.title('Face Cream & Face Wash Sales Data')
# plt.xlabel('Months')
# plt.ylabel('Sales Units')
# plt.xticks(months, rotation=45)
# # plt.grid()
# # plt.legend()
# plt.show()
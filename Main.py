import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# print(matplotlib.__version__)



# x = np.array([2023, 2024, 2025, 2026])
# y = np.array([ 10, 20, 30, 40])

# plt.plot(x, y)

# plt.show()


# plot customization 

# x = np.array([2023, 2024, 2025, 2026])
# y1 = np.array([10, 20, 30, 40])
# y2 = np.array([17, 25, 34, 34])
# y3 = np.array([12, 15, 25, 20])
# line_style = dict(marker="o", 
#                   linestyle="solid", 
#                   linewidth=4, 
#                   label="my plot", 
#                   markersize=10,
#                   markerfacecolor="blue")


# plt.plot(x, y1, color="blue", **line_style)
# plt.plot(x, y2, color="red", **line_style)
# plt.plot(x, y3, color="yellow", **line_style)

# plt.show()


# labels

# x = np.array([2023, 2024, 2025, 2026])
# y1 = np.array([10, 20, 30, 40])
# y2 = np.array([17, 25, 34, 34])
# y3 = np.array([12, 15, 25, 20])


# plt.title("Class size",
#           fontsize=20, 
#           family="serif", 
#           fontweight="bold", 
#           color="blue")

# plt.xlabel("Year", 
#            fontsize=15, 
#            family="serif", 
#            fontweight="bold", 
#            color="red")

# plt.ylabel("Students", 
#            fontsize=15, 
#            family="serif", 
#            fontweight="bold", 
#            color="red")


# plt.tick_params(axis="both",
#                 color="red")

# plt.plot(x, y1)
# plt.plot(x, y2)
# plt.plot(x, y3)


# plt.xticks(x)

# plt.show()


# grid lines = helps plots easier to read by adding reference lines.

# x = [1, 2, 3, 4, 5]
# y = [5, 10, 15, 20, 25]


# plt.grid(axis="both",
#          linewidth=3,
#          color="lightgray",
#          linestyle="dashed")

# plt.plot(x, y)

# plt.show()


# Bar charts

# categories = np.array(["Grains", "Fruit", "Vegetable", "Protein", "Dairy", "Sweets"])
# values = np.array([4, 3, 6, 3, 5, 2])

# plt.bar(categories, values, color="skyblue")
# # plt.barh(categories, values, color="skyblue")

# plt.title("Daily Consumption")
# plt.xlabel("food")
# plt.ylabel("Quantity")

# plt.show()

# pie charts

# categories = np.array(["Freshman", "Sophomore", "Junior", "Senior"])
# values = np.array([100, 250, 252, 300])
# colors = ["red", "green", "blue", "yellow"]


# plt.pie(values, labels=categories, 
#         autopct="%1.1f%%",
#         colors=colors,
#         explode=[0, 0, 0, 0.1],
#         shadow=True,
#         startangle=90)



# plt.title("Student Yearly Attendance")


# plt.show()

# scatter plots

# x1= np.array([0, 1, 1, 2, 3, 5, 6, 7, 7, 8]) # Hours studied
# y1 = np.array([0, 12, 23, 39, 58, 80, 6, 54, 27, 29]) # Grades


# x2= np.array([0, 1, 1, 2, 3, 5, 6, 7, 7, 8]) # Hours studied
# y2 = np.array([55, 54, 53, 52, 51, 48, 45, 40, 35, 30]) # Grades

# plt.scatter(x1, y1, 
#             color="skyblue",
#             alpha = 0.5,
#             s = 100,
#             label="Class average")

# plt.scatter(x2, y2, 
#             color="red",
#             alpha = 0.5,
#             s = 100,
#             label="Best student")


# plt.title("Student Grades")
# plt.xlabel("Hours studied")
# plt.ylabel("Grade")


# plt.legend()
# plt.show()


# histograms

# scores = np.random.normal(loc=80, scale=10, size=100)
# scores = np.clip(scores, 0, 100)

# plt.hist(scores, 
#          bins=10,
#          color="Green",
#          edgecolor="black",)

# plt.title("Student Grades")
# plt.xlabel("Score")
# plt.ylabel("Frequency")



# plt.show()


# subplots 

# x = np.array([1, 2, 3, 4, 5])


# figure, axes = plt.subplots(2, 2)

# axes[0, 0].plot(x, x*2, color="red")
# axes[0, 0].set_title("x*2")

# axes[0, 1].bar(x, x**2, color="blue")
# axes[0, 1].set_title("x**2")


# axes[1, 0].scatter(x, x**3, color="green")
# axes[1, 0].set_title("x**3")


# axes[1, 1].plot(x, x**4, color="orange")
# axes[1, 1].set_title("x**4")

# plt.tight_layout()

# plt.show()

# Pandas + Matplotlib 

# df = pd.read_csv("data.csv")

# type_count = (df["Type1"].value_counts(ascending=True)) 

# plt.barh(type_count.index, type_count.values, 
#          color="yellow", 
#          edgecolor="black")


# plt.title("# of Pokemon by Primary Type")
# plt.xlabel("Count")
# plt.ylabel("Type")
# plt.tight_layout()


# plt.show()
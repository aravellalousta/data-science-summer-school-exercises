import matplotlib.pyplot as plt

months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
]
avg_rainfall_mm = [78, 60, 92, 55, 110, 95, 75, 65, 85, 70, 80, 90]

plt.bar(months, avg_rainfall_mm)
plt.title("Average Monthly Rainfall")
plt.ylabel("Average Rainfall (mm)")
plt.xlabel("Months")

plt.show()

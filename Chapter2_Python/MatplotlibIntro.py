import matplotlib.pyplot as plt

grades = {
    "Jan": [56, 64, 78, 100],
    "Ben": [86, 94, 98, 90]
}

# Plot
plt.plot(range(len(grades["Jan"])), grades["Jan"], color="blue")
plt.plot(range(len(grades["Ben"])), grades["Ben"], color="red")
plt.legend(grades.keys())
plt.xlabel("Course")
plt.ylabel("Grade in %")
plt.title("Jan vs. Ben")
plt.show()


# Scatter
plt.scatter(range(len(grades["Jan"])), grades["Jan"], color="blue")
plt.scatter(range(len(grades["Ben"])), grades["Ben"], color="red")
plt.legend(grades.keys())
plt.xlabel("Course")
plt.ylabel("Grade in %")
plt.title("Jan vs. Ben")
plt.show()

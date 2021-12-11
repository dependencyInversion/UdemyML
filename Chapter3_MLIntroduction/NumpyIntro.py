import numpy as np

list1 = np.array([-2, 1, 2, -10, 22, -10])
list2 = np.array([-20, 123, 112, -10, 22, -120])

print(
    f"values: {list1}",
    f"min: {np.min(list1)}",
    f"max: {np.max(list1)}",
    f"mean: {np.mean(list1)}",
    f"median: {np.median(list2)}",
    sep="\n",
    end="\n\n"
)

print(
    f"values: {list2}",
    f"min: {np.min(list2)}",
    f"max: {np.max(list2)}",
    f"mean: {np.mean(list2)}",
    f"median: {np.median(list2)}",
    sep="\n",
    end="\n\n"
)

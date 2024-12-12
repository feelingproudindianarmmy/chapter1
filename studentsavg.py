import matplotlib.pyplot as plt
import numpy as np


students = ['Alice', 'Bob', 'Charlie', 'David', 'Eva']
marks = [85, 78, 92, 88, 76]


average_marks = np.mean(marks)


plt.figure(figsize=(8, 6))
plt.bar(students, marks, color='yellow', label='Marks')


plt.axhline(y=average_marks, color='red', linestyle='--', label=f'Average: {average_marks:.2f}')


plt.title('Students\' Marks and Average', fontsize=14)
plt.xlabel('Students', fontsize=12)
plt.ylabel('Marks', fontsize=12)


plt.legend()


plt.show()
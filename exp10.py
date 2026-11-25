import matplotlib.pyplot as plt

subjects = ['Python', 'Data Struct', 'Maths', 'Web Dev', 'DB Console']
marks = [88, 75, 92, 85, 78]

plt.figure(figsize=(8, 4.5))
plt.bar(subjects, marks, color='skyblue', edgecolor='black')
plt.title("Student Marks Evaluation", fontsize=14, fontweight='bold')
plt.xlabel("Subjects", fontsize=12)
plt.ylabel("Marks Obtained", fontsize=12)
plt.ylim(0, 100)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

import pandas as pd
data={'Name':['Oratile','Gale'],'Age':[19,20]}
df= pd.DataFrame(data)
print(df)

import pandas as pd

# Step 1: Create a DataFrame
books = pd.DataFrame({
    'Title': ['Python Basics', 'Data Science Handbook', 'AI for Beginners', 'Machine Learning Guide', 'Deep Learning'],
    'Author': ['Oratile Lang', 'Gale Smith', 'Kabelo', 'Oratile Lang', 'Gale Smith'],
    'Pages': [250, 450, 300, 500, 600],
    'Price': [200, 500, 300, 450, 700]
})

# Step 2: Show all books
print("All Books:\n", books)

import numpy as np

scores = np.array([
    [85, 90, 78],
    [92, 88, 95],
    [75, 80, 70],
    [60, 65, 70]
])

print("Scores Array:", scores)




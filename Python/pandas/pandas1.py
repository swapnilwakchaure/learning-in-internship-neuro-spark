import pandas as pd
import numpy as nm

students = {
    "name": ["Rahul", "Ramesh", "Suresh"],
    "subject": ["Physics", "Maths", "Chemistry"],
    "marks": [92, 84, 49]
}

data = pd.DataFrame(students)

print(data)

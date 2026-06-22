import pandas as pd
import numpy as np
import random

# -----------------------------
# Helper lists
# -----------------------------
first_names = ["Aarav", "Vivaan", "Aditya", "Kabir", "Reyansh", "Arjun", "Sai", "Rohan", "Ishaan", "Krish",
               "Ananya", "Diya", "Myra", "Aadhya", "Saanvi", "Ira", "Meera", "Riya", "Sara", "Navya"]

last_names = ["Sharma", "Verma", "Gupta", "Patel", "Reddy", "Nair", "Khan", "Singh", "Yadav", "Chopra",
              "Mehta", "Kapoor", "Bose", "Ghosh", "Das", "Pillai", "Shetty", "Rastogi", "Saxena", "Agarwal"]

cities = ["Mumbai", "Delhi", "Bangalore", "Hyderabad", "Chennai", "Pune", "Kolkata", "Ahmedabad", "Jaipur", "Lucknow"]

majors = ["Computer Science", "Mathematics", "Physics", "Biology", "Chemistry",
          "Economics", "English", "History", "Business", "Psychology"]

genders = ["Male", "Female"]

# -----------------------------
# Generate dataset
# -----------------------------
num_rows = 500

data = {
    "student_id": np.arange(1, num_rows + 1),
    "first_name": np.random.choice(first_names, num_rows),
    "last_name": np.random.choice(last_names, num_rows),
    "age": np.random.randint(17, 25, num_rows),
    "gender": np.random.choice(genders, num_rows),
    "grade_level": np.random.randint(1, 4, num_rows),  # 1=Freshman, 2=Sophomore, 3=Junior
    "major": np.random.choice(majors, num_rows),
    "gpa": np.round(np.random.uniform(2.0, 4.0, num_rows), 2),
    "city": np.random.choice(cities, num_rows),
    "enrollment_year": np.random.randint(2018, 2024, num_rows)
}

df = pd.DataFrame(data)

# Create email column
df["email"] = (
    df["first_name"].str.lower() + "." +
    df["last_name"].str.lower() +
    "@university.edu"
)

print(df.head(10))
print(df)


import json
import pandas as pd
import numpy as np


def handler(request):
    # Generate a sample dataset similar to sales.py and return JSON
    np.random.seed(0)
    first_names = ["Aarav", "Vivaan", "Aditya", "Kabir", "Reyansh", "Arjun", "Sai", "Rohan", "Ishaan", "Krish",
                   "Ananya", "Diya", "Myra", "Aadhya", "Saanvi", "Ira", "Meera", "Riya", "Sara", "Navya"]

    last_names = ["Sharma", "Verma", "Gupta", "Patel", "Reddy", "Nair", "Khan", "Singh", "Yadav", "Chopra",
                  "Mehta", "Kapoor", "Bose", "Ghosh", "Das", "Pillai", "Shetty", "Rastogi", "Saxena", "Agarwal"]

    cities = ["Mumbai", "Delhi", "Bangalore", "Hyderabad", "Chennai", "Pune", "Kolkata", "Ahmedabad", "Jaipur", "Lucknow"]

    majors = ["Computer Science", "Mathematics", "Physics", "Biology", "Chemistry",
              "Economics", "English", "History", "Business", "Psychology"]

    genders = ["Male", "Female"]

    num_rows = 200

    data = {
        "student_id": np.arange(1, num_rows + 1).tolist(),
        "first_name": np.random.choice(first_names, num_rows).tolist(),
        "last_name": np.random.choice(last_names, num_rows).tolist(),
        "age": np.random.randint(17, 25, num_rows).tolist(),
        "gender": np.random.choice(genders, num_rows).tolist(),
        "grade_level": np.random.randint(1, 4, num_rows).tolist(),
        "major": np.random.choice(majors, num_rows).tolist(),
        "gpa": np.round(np.random.uniform(2.0, 4.0, num_rows), 2).tolist(),
        "city": np.random.choice(cities, num_rows).tolist(),
        "enrollment_year": np.random.randint(2018, 2024, num_rows).tolist(),
    }

    df = pd.DataFrame(data)
    df["email"] = df["first_name"].str.lower() + "." + df["last_name"].str.lower() + "@university.edu"

    # Return first 100 records as JSON
    body = df.head(100).to_json(orient="records")

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": body,
    }

import csv
import random
from datetime import datetime, timedelta

def generate_random_date():
    start_date = datetime(1950, 1, 1)
    end_date = datetime(2015, 12, 31)
    random_days = random.randint(0, (end_date - start_date).days)
    return (start_date + timedelta(days=random_days)).strftime("%Y-%m-%d")

def generate_csv():
    male_names = ["Oleksandr", "Ivan", "Dmitro", "Serhiy", "Igor", "Andriy", "Volodymyr"]
    female_names = ["Maria", "Olena", "Anna", "Natalia", "Yulia", "Oksana", "Viktoria"]
    
    last_names = ["Melnyk", "Shevchenko", "Boyko", "Kovalenko", "Bondarenko", "Tkachenko", "Oliynyk"]
    histories = ["Healthy", "Chronic allergy", "Previous surgery", "Asthma", "No issues"]

    with open("patients.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "dob", "gender", "history"])

        for i in range(1000):
            gender = random.choice(["M", "F"])
            
            if gender == "M":
                first_name = random.choice(male_names)
            else:
                first_name = random.choice(female_names)
            
            full_name = f"{first_name} {random.choice(last_names)}"
            dob = generate_random_date()
            history = random.choice(histories)
            
            writer.writerow([full_name, dob, gender, history])

if __name__ == "__main__":
    generate_csv()

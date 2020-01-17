#!/usr/bin/env python3.8

# bmi = (weight in kg / height in meters squared)
# bmi * 703 for imperial

def gather_info():
    height = float(input("What is your height? (inches or meters) "))
    weight = float(input("What is your weight? (pounds or kilograms) "))
    system = input("Are your measurements in metric or imperial? ").lower().strip()
    return (height, weight, system)

def calculate_bmi(weight, height, system='metric'):
    """
    Return the body mass index (BMI) for given
    weight, height, and measuremnt system
    """
    if system == 'metric':
        bmi = (weight / (height ** 2))
    else:
        bmi = 703 * (weight / (height ** 2))
    return bmi

def bmi_level(bmi):
    if bmi < 18.5:
        return 'Underweight'
    elif bmi < 25:
        return 'Normal'
    elif bmi < 30:
        return 'Overweight'
    elif bmi >= 30:
        return 'Obese'

while True:
    height, weight, system = gather_info()
    if system.startswith('i'):
        bmi = calculate_bmi(weight, system=system, height=height)
        level = bmi_level(bmi)
    elif system.startswith('m'):
        bmi = calculate_bmi(weight, height)
        level = bmi_level(bmi)
    else:
        print("Error: Unknown system. Use imperial or metric")
        continue
    print(f"Your BMI is {bmi}, which makes you {level}")
    break


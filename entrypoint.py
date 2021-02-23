#!/usr/bin/env python3

import math
import pandas as pd


def calculate_premium_rate(gender, age, smoker):
    if gender and 18 <= age < 40 and smoker == 'NS':
        return 0.10
    if gender and 18 <= age < 40 and smoker == 'S':
        return 0.25
    if gender and 40 <= age <= 60 and smoker == 'NS':
        return 0.30
    if gender and 40 <= age <= 60 and smoker == 'S':
        return 0.55


def calculate_debits(health, smoker, alcohol, bmi):
    debit = 0
    # 15 point debit
    if 'DEPRESSION' in health:
        debit += 15
    if 'ANXIETY' in health:
        debit += 15
    if bmi < 18.5:
        debit += 15
    # 25 point debit
    if 'SURGERY' in health:
        debit += 25
    if smoker == 'S':
        debit += 25
    if 30.01 > bmi > 25:
        debit += 25
    if 26 > alcohol > 10:
        debit += 25
    # 25 point debit
    if 'HEART' in health:
        debit += 30
    if bmi > 30:
        debit += 30
    if alcohol > 25:
        debit += 30
    return debit


def main():
    results = pd.DataFrame(columns=["name", "BMI", "score", "monthly premium"])

    df = pd.read_csv('input.csv')
    for index, row in df.iterrows():
        name = row["name"]
        gender = row["gender"]
        age = row["age"]
        health = row["health"]
        smoker = row["smoker"]
        alcohol = row["alcohol"]
        policy = row["policyrequested"]

        bmi = round(row["weight"] / math.sqrt(row["height"] / 100), 1)

        debits = calculate_debits(health, smoker, alcohol, bmi)
        rate = calculate_premium_rate(gender, age, smoker)

        premium = policy / 1000 * rate
        if 75 < debits <= 100:
            premium *= 1.15
        if 100 < debits:
            premium *= 1.25
        monthly_premium = round((premium / 12), 2)

        results.loc[len(results)] = [name, bmi, debits, monthly_premium]

    results.to_csv('output.csv', index=False)

if __name__ == "__main__":
    main()

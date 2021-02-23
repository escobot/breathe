The insurance company would like to build a new system that will enable it to underwrite term life insurance policies for potential customers in realtime.

You have been hired to build this system.

Overview
--------
The system will take the input in the file input.csv and implement the various calculations described below. The output can be a table on a web page or a simple file named output.csv or output.json.

You should feel free to use any technology you think might showcase your skills best.


Insurance Qualification Rules
-----------------------------

* A potential customer will be accepted with a regular premium if they have a perfect score
* A potential customer will be referred to a follow up interview if they have more than 50 debits
* A potential customer will be charged 1.15x if they have more than 75 debits
* A potential customer will be charged 1.25x if they have more than 100 debits

* Each of the following will cause a 15 point debit
  * A hit on DEPRESSION
  * A hit on ANXIETY
  * A BMI below 18.5

* Each of the following will cause a 25 point debit
  * A hit on SURGERY
  * Being a smoker
  * BMI above 25.0
  * Alcohol consumption above 10 drinks per week

* Each of the following will cause a 30 point debit
  * A hit on HEART
  * BMI above 30.0
  * Alcohol consumption above 25 drinks per week

BMI information is from this chart:
* https://www.cdc.gov/healthyweight/assessing/bmi/adult_bmi/index.html

The formula is: weight (kg) / [height (m)]<sup>2</sup>

Premium Calculation
-------------------
Here's a simplistic chart to calculate coverage price:

* Male, 18-40, Non Smoker: $0.10 
* Female, 18-40, Non Smoker: $0.10

* Male, 18-40, Smoker: $0.25
* Female, 18-40, Smoker: $0.25

* Male, 40-60, Non Smoker: $0.30
* Female, 40-60, Non Smoker: $0.30 

* Male, 40-60, Smoker: $0.55
* Female, 40-60, Smoker: $0.55

The dollar amount is the cost of insuring $1,000 per year.

Example: Male, 40-60, Smoker, 500k coverage => $275/year or $22.92/month


In the output of the program, please calculate the score for each potential customer and the prices per month they should pay.

Example output.csv:

```csv
name,BMI,score,monthly premium
david,28.1,30,4.38
```


Evaluation
----------
* Code readability
* Code organization
* All the business rules are considered
* Demonstrates knowledge of programming language

Bonus points for:
* Test coverage
* Error handling
* Data validation
* Interesting thoughtful details not described in the requirements

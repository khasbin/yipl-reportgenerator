
# Petroleum product report generator

This application performs the following operations:
1. Fetch data for Petroleum Products from the data.json file using an API call. API endpoint https://raw.githubusercontent.com/younginnovations/internship-challenges/master/programming/petroleum-report/data.json

2. Normalizes the data and stores the data in the database

3. Lists the sale of each petroleum product.

4. Lists top 3 countries with highest and the lowest sale.

5. Lists the average sale of each product for 4 years of interval.





## Installation

In order to run the application 
1. Install all the requirements as specified in the project folder requirements.txt
2. Run the command 
```bash
pip install -r requirements.txt

```

## Run the application

To run the application go the project folder and then run the following command

```bash
  python manage.py makemigrations
```
```bash
  python manage.py migrate
```
```bash
  python manage.py runserver


## Reflection

**1. What does a boolean filter do?**

A boolean filter checks each row against a condition and only keeps the rows that meet that condition. For example, filtering for South only keeps orders from the South region.

**2. What is the difference between df["revenue"] and df[["revenue"]]?**

df["revenue"] returns a Series, which is a single column of data. df[["revenue"]] returns a DataFrame, which is a table containing that column. This matters when working with functions that expect a DataFrame instead of a Series.

**3. Why choose pandas instead of Excel?**

I would choose pandas because it makes working with large datasets easier. I can filter, organize, calculate, and analyze thousands of orders using just a few lines of code.

# ISM2411 Lab 13 — First DataFrame — Retail Sales Explorer

Name: Wasee Jafri

## How to Run

Run the following command in Terminal:

python3 explore.py
EOF

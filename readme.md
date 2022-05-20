# problem statement
In a university, your attendance determines whether you will be allowed to attend your graduation ceremony. 
You are not allowed to miss classes for four or more consecutive days. 
Your graduation ceremony is on the last day of the academic year, which is the Nth day.

Your task is to determine the following:
1. The number of ways to attend classes over N days.
2. The probability that you will miss your graduation ceremony.
Represent the solution in the string format as "Answer of (2) / Answer of (1)", don't actually divide or reduce the fraction to decimal


```
n < 4;first 3 day free to go in any manner so total = 2^n, attending cermeny depend only on last day so 0.5

n>=4; nth day if consider last three day 
AAA = P
PAA = P/A
APA = P/A
PPA = P/A
AAP = P/A
PAP = P/A
APP = P/A
PPP = P/A
if AAA then have to P in class; on rest days can be A/P

sample solution : 
5=14/29
10=372/773
```

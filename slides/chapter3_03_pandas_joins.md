---
type: slides
---

# Joining data in Pandas

---

# Types of Joins

| Type | Description | Scheme |
|:--:|:--:|:--:|
| Inner Join | Returns records that have matching values in both tables | <img src="https://www.w3schools.com/sql/img_innerjoin.gif" width="100"> |
| Left Join | Returns all records from the left table, <br> and the matched records from the right table | <img src="https://www.w3schools.com/sql/img_leftjoin.gif" width="100"> |
| Right Join | Returns all records from the right table, <br> and the matched records from the left table | <img src="https://www.w3schools.com/sql/img_rightjoin.gif" width="100"> |
| Full Join | Returns all records when there is a match <br> in either left or right table | <img src="https://www.w3schools.com/sql/img_fulljoin.gif" width="100"> |

Notes: Imagine now that you have not just one data in a table format. You can join all the tables together to analyze everything at once.

There are three main ways of doing this:

1. Inner Join
2. Left Join or Right Join (*depending on which table you call "left" and "right"*)
3. Full Join

Note that it's important that you have a shared column to join the data.

*Credits: [W3Schools](https://www.w3schools.com/sql/sql_join.asp)*

---

# Inner Join

<center><img src="imgs/inner_join.png" width="600"></center>

Notes: In this example we have two tables:

* **Table A**: holds IDs and subjects' names
* **Table B**: holds IDs and subjects' occupation

We will join the data by the column `Id`. *Think what would happen if we didn't have the `Id` column in table B. Would we be able to join these two tables together?*

With the inner join, we take only those observations that have matching `Id` values in both tables (these observations are marked with green ticks). Note that there were two observations in table B with `Id` "1", so in a resulting table (bottom right) we have two observations for "Bob".

---

# Left Join

<center><img src="imgs/left_join.png" width="600"></center>

Notes: By performing a **left join** we have to define one table as "left" and the other one as "right". In this example, table A is "left" and table B is "right". We take **all** the observations from table A and join matching observations from table B (matched by the `Id` column).

Some observations from table A didn't have matching observations in table B, that's why we see missing values in a table.

An idea of the **right join** is basically the same, but in that case, we would take all the observations from the right table and add matches from the left table. So if we did a right join with table A is "right" and table B is "left" we would end up with the same results.

---

# Full Join

<center><img src="imgs/full_join.png" width="600"></center>

Notes: By joining the tables by full join we take all observations from both tables. In this example we have observations that don't have matching observations, that's why we see more missing values.

---

# Pandas command

```python
table1 = pd.DataFrame(
    {'Id': [1, 2, 3, 4],
    'Name': ['Bob', 'Jack', 'Jill', 'Ben']})

table2 = pd.DataFrame(
    {'Id': [1,1,3,5,7,7],
    'Occupation': ['IT', 'Finance', 'IT', 'Healthcare', 'Agriculture', 'Finance']})

pd.merge(
    left=table1, right=table2,
    on='Id', # or left_on='Id', right_on='Id',
    how='left')
```
```out
    Id  Name Occupation
0   1   Bob         IT
1   1   Bob    Finance
2   2  Jack        NaN
3   3  Jill         IT
4   4   Ben        NaN
```

Notes: To perform joining in Pandas we can use `pd.merge()` function. If the joining column has the same name in both DataFrame you can use `on` argument. If names were different (for example `Id` for table1 and `subj_Id` for table2), then we would have to use `left_on` and `right_on` arguments (`left_on="Id"`, `right_on="subj_Id"`).

The missing values are represented as `np.NaN` objects.

Note that Full Join is called "outer" is Pandas (`how="outer"`).

---

# Let's code!

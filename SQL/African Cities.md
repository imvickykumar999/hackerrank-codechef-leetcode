# `African Cities`

https://www.hackerrank.com/challenges/african-cities/problem?isFullScreen=true

<br>

>Given the CITY and COUNTRY tables, query the names of all cities where the CONTINENT is 'Africa'.
>
>Note: CITY.CountryCode and COUNTRY.Code are matching key columns.

<br>

## `Input Format`

    The CITY and COUNTRY tables are described as follows:

![image](https://github.com/imvickykumar999/hackerrank-codechef-leetcode/assets/50515418/b22993f8-7bc8-41ca-acd6-cef7976e5b8e)

![image](https://github.com/imvickykumar999/hackerrank-codechef-leetcode/assets/50515418/4a447e4a-789e-4f82-a2d7-852ecc4db695)

<br>

# `Solution`

```sql
select ct.name from city as ct inner join country as co on ct.CountryCode = co.Code where co.continent = 'Africa';
```

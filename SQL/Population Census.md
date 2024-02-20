
# `Population Census`

https://www.hackerrank.com/challenges/asian-population/problem?isFullScreen=true

<br>

>Given the CITY and COUNTRY tables, query the sum of the populations of all cities where the CONTINENT is 'Asia'.
>
>Note: CITY.CountryCode and COUNTRY.Code are matching key columns.

<br>

# `Input Format`

The CITY and COUNTRY tables are described as follows:

![image](https://github.com/imvickykumar999/hackerrank-codechef-leetcode/assets/50515418/9b7e2233-6891-4c2d-908a-d923be3c6dc2)

![image](https://github.com/imvickykumar999/hackerrank-codechef-leetcode/assets/50515418/2a41e18f-1f59-4ae1-842f-56e619bf069b)

# `Solution`

```sql
select sum(city.population) from city inner join country on city.countrycode = country.code where country.continent = 'Asia';
```

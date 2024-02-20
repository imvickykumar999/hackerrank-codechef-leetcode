# `Revising the Select Query I`

>Query all columns for all American cities in the CITY table with populations larger than 100000. 
>
>The CountryCode for America is USA.

<br>

    The CITY table is described as follows:

>![image](https://github.com/imvickykumar999/hackerrank-codechef-leetcode/assets/50515418/e36c3712-e00d-4e27-a46a-ba9ce48fe79d)

<br>

### **`Solution`:**

```SQL
select * from city where population > 100000 and countrycode = 'USA';
```

<br>

***More*** [`Questions`](https://www.hackerrank.com/domains/sql?filters%5Bsubdomains%5D%5B%5D=select)

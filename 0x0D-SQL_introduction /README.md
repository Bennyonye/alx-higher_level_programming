# Introduction to SQL

This marked my initial foray into working with SQL and relational databases. I began by delving into introductory concepts of data definition and manipulation language, honing my skills in crafting subqueries, and leveraging functions to interact with databases effectively.

## Usage :dolphin:

* The scripts [3-list_tables.sql](./3-list_tables.sql) are designed to be used with the specified database for querying, taking it as a MySQL command line argument.

```
$ cat 3-list_tables.sql | mysql -h localhost -u root -p mysql
```

* Tasks 101-103 involve querying from the database [temperatures.sql](./temperatures.sql).

## Tasks :page_with_curl:

* **0. Listing databases**
  * [0-list_databases.sql](./0-list_databases.sql): A MySQL script to list all databases.

* **1. Creating a database**
  * [1-create_database.sql](./1-create_database.sql): A MySQL script to create the database `hbtn_0c_0`.

* **2. Deleting a database**
  * [2-remove_databases.sql](./2-remove_databases.sql): A MySQL script to delete the database `hbtn_0c_0`.

* **3. Listing tables**
  * [3-list_tables.sql](./3-list_tables.sql): A MySQL script to list all tables.

* **4. Creating the first table**
  * [4-first_table.sql](./4-first_table.sql): A MySQL script to create a table named `first_table`.
  * Description:
    * `id`: INT
    * `name`: VARCHAR(256)

* **5. Full table description**
  * [5-full_table.sql](./5-full_table.sql): A MySQL script to print the full description of the table `first_table`.

* **6. Listing all records in a table**
  * [6-list_values.sql](./6-list_values.sql): A MySQL script to list all rows of the table `first_table`.

* **7. Adding the first record**
  * [7-insert_value.sql](./7-insert_value.sql): A MySQL script to insert a new row into the table `first_table`.
  * Description:
    * `id` = `89`
    * `name` = `Best School`

* **8. Counting occurrences of ID 89**
  * [8-count_89.sql](./8-count_89.sql): A MySQL script to display the number of records with `id = 89` in the table `first_table`.

* **9. Full table creation with data**
  * [9-full_creation.sql](./9-full_creation.sql): A MySQL script to create and populate a table named `second_table`.
  * Description:
    * `id`: INT
    * `name`: VARCHAR(256)
    * `score`: INT
  * Records:
    * `id` = 1, `name` = "John", `score` = 10
    * `id` = 2, `name` = "Alex", `score` = 3
    * `id` = 3, `name` = "Bob", `score` = 14
    * `id` = 4, `name` = "George", `score` = 8

* **10. Listing by highest score**
  * [10-top_score.sql](./10-top_score.sql): A MySQL script to list the `score` and `name` of all records from the `second_table` in descending order of `score`.

* **11. Selecting records with scores greater than or equal to 10**
  * [11-best_score.sql](./11-best_score.sql): A MySQL script to list the `score` and `name` of all records with a `score >= 10` from the `second_table` in descending order of `score`.

* **12. Updating a record**
  * [12-no_cheating.sql](./12-no_cheating.sql): A MySQL script to update Bob's score to 10 in the `second_table`.

* **13. Removing records with low scores**
  * [13-change_class.sql](./13-change_class.sql): A MySQL script to remove all records with a `score <= 5` from the `second_table`.

* **14. Calculating the average score**
  * [14-average.sql](./14-average.sql): A MySQL script to compute the average `score` of all records in the `second_table`.

* **15. Grouping records by score**
  * [15-groups.sql](./15-groups.sql): A MySQL script to list the `score` and the number of records with the same score in the `second_table`, ordered by descending count.

* **16. Retrieving records with names**
  * [16-no_link.sql](./16-no_link.sql): A MySQL script to list the `score` and `name` of all records in the `second_table`, ordered by descending `score`. Rows without a `name` value are excluded.

* **17. Converting to UTF8**
  * [100-move_to_utf8.sql](./100-move_to_utf8.sql): A MySQL script to convert the `hbtn_0c_0` database to UTF8.

Tasks involving [temperatures.sql](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql):

* **18. Average Temperatures**
  * [101-avg_temperatures.sql](./101-avg_temperatures.sql): A MySQL script to display the average temperature (in Fahrenheit) by city in descending order.

* **19. Top Cities by Temperature**
  * [102-top_city.sql](./102-top_city.sql): A MySQL script to display the three cities with the highest average temperature from July to August in descending order.

* **20. Maximum Temperature by State**
  * [103-max_state.sql](./103-max_state.sql): A MySQL script to display the maximum temperature of each state ordered by state name.

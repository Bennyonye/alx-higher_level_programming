# Introduction to SQL

In this project, i dived into the realm of relational databases, where I investigated into practicing introductory SQL data definitions and data manipulation language. This involved crafting subqueries and leveraging functions to interact with databases effectively.

## Tasks :page_with_curl:

* **0. List Databases**
  * [0-list_databases.sql](./0-list_databases.sql): A MySQL script to list all databases.

* **1. Create a Database**
  * [1-create_database.sql](./1-create_database.sql): A MySQL script to create the database `hbtn_0c_0`.

* **2. Delete a Database**
  * [2-remove_databases.sql](./2-remove_databases.sql): A MySQL script to delete the database `hbtn_0c_0`.

* **3. List Tables**
  * [3-list_tables.sql](./3-list_tables.sql): A MySQL script to list all tables.

* **4. First Table**
  * [4-first_table.sql](./4-first_table.sql): A MySQL script to create a table named `first_table`.
  * Description:
    * `id`: INT
    * `name`: VARCHAR(256)

* **5. Full Description**
  * [5-full_table.sql](./5-full_table.sql): A MySQL script to print the full description of the table `first_table`.

* **6. List All Records in Table**
  * [6-list_values.sql](./6-list_values.sql): A MySQL script to list all rows of the table `first_table`.

* **7. Add the First Record**
  * [7-insert_value.sql](./7-insert_value.sql): A MySQL script to insert a new row into the table `first_table`.
  * Description:
    * `id` = `89`
    * `name` = `Best School`

* **8. Count Occurrences of ID 89**
  * [8-count_89.sql](./8-count_89.sql): A MySQL script to display the number of records with `id = 89` in the table `first_table`.

* **9. Full Creation**
  * [9-full_creation.sql](./9-full_creation.sql): A MySQL script to create and fill a table `second_table`.
  * Description:
    * `id`: INT
    * `name`: VARCHAR(256)
    * `score`: INT
  * Records:
    * `id` = 1, `name` = "John", `score` = 10
    * `id` = 2, `name` = "Alex", `score` = 3
    * `id` = 3, `name` = "Bob", `score` = 14
    * `id` = 4, `name` = "George", `score` = 8

* **10. List by Best**
  * [10-top_score.sql](./10-top_score.sql): A MySQL script to list the `score` and `name` of all records of the table `second_table` in descending order of `score`.

* **11. Select the Best**
  * [11-best_score.sql](./11-best_score.sql): A MySQL script to list the `score` and `name` of all records with a `score >= 10` in the table `second_table` in order of descending score.

* **12. Cheating is Bad**
  * [12-no_cheating.sql](./12-no_cheating.sql): A MySQL script to update Bob's score to 10 in the table `second_table`.

* **13. Score Too Low**
  * [13-change_class.sql](./13-change_class.sql): A MySQL script to remove all records with a `score <= 5` in the table `second_table`.

* **14. Average**
  * [14-average.sql](./14-average.sql): A MySQL script to compute the average `score` of all records in the table `second_table`.

* **15. Number by Score**
  * [15-groups.sql](./15-groups.sql): A MySQL script to list the `score` and the number of records with the same score in the table `second_table` in descending order of count.

* **16. Say My Name**
  * [16-no_link.sql](./16-no_link.sql): A MySQL script to list the `score` and `name` of all records in the table `second_table` in order of descending `score`, excluding rows without a `name` value.

* **17. Go to UTF8**
  * [100-move_to_utf8.sql](./100-move_to_utf8.sql): A MySQL script to convert the `hbtn_0c_0` database to UTF8.

* **18. Temperatures #0**
  * [101-avg_temperatures.sql](./101-avg_temperatures.sql): A MySQL script to display the average temperature (in Fahrenheit) by city in descending order.

* **19. Temperatures #1**
  * [102-top_city.sql](./102-top_city.sql): A MySQL script to display the three cities with the highest average temperature from July to August in descending order.

* **20. Temperature #2**
  * [103-max_state.sql](./103-max_state.sql): A MySQL script to display the maximum temperature of each state ordered by state name.

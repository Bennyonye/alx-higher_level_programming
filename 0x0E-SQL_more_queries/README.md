# 0x0E. SQL - More queries

This project focuses on practicing SQL queries related to permissions, joins, and constraints. It utilizes two databases: `hbtn_0d_tvshows` and `hbtn_0d_tvshows_rate`.

### Scripts and Usage:

* **Scripts:**
    * Each task corresponds to a separate `.sql` script located in the project directory.
* **Usage:**
    * Execute scripts for tasks 10-101 on the `hbtn_0d_tvshows` database:
        ```
        $ cat ./hbtn_0d_tvshows_sql/[task_number].sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
        ```
    * Execute scripts for tasks 102-103 on the `hbtn_0d_tvshows_rate` database:
        ```
        $ cat ./hbtn_0d_tvshows_rate_sql/[task_number].sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows_rate
        ```

### Tasks:

**Permissions and User Management:**

* **0. My Privileges:** Lists privileges for specified users.
* **1. Root User Creation:** Creates a root user (`user_0d_1`) with full privileges.
* **2. Read User Creation:** Creates a user (`user_0d_2`) with read-only access to `hbtn_0d_2`.

**Table Structures and Constraints:**

* **3. Always a Name:** Creates a table `force_name` with mandatory name column.
* **4. ID Can't be Null:** Creates a table `id_not_null` with a non-nullable default ID and name column.
* **5. Unique ID:** Creates a table `unique_id` with a unique and non-nullable default ID and name column.

**Database and Table Creation:**

* **6. States Table:** Creates a database `hbtn_0d_usa` with a table `states` for US states.
* **7. Cities Table:** Creates a table `cities` in `hbtn_0d_usa` with foreign key linking to `states`.

**Data Retrieval and Manipulation:**

* **8. Cities of California:** Lists cities in California from `hbtn_0d_usa` ordered by ID.
* **9. Cities by States:** Lists all cities in `hbtn_0d_usa` with corresponding state names, ordered by city ID.
* **10. Genre ID by Show:** Lists shows with genres from `hbtn_0d_tvshows` ordered by show title and genre ID.
* **11. Genre ID for all Shows:** Lists all shows from `hbtn_0d_tvshows` with genres (or NULL if none), ordered by title and genre ID.
* **12. No Genre:** Lists shows from `hbtn_0d_tvshows` without genres, ordered by title.
* **13. Number of Shows by Genre:** Lists genres and their associated show counts from `hbtn_0d_tvshows`, ordered by number of shows in descending order.
* **14. My Genres:** Lists genres linked to the show "Dexter" from `hbtn_0d_tvshows`, ordered by genre name.
* **15. Only Comedy:** Lists comedy shows from `hbtn_0d_tvshows`, ordered by title.
* **16. List Shows and Genres:** Lists shows and their associated genres from `hbtn_0d_tvshows`, ordered by show title and genre name.
* **17. Not My Genre:** Lists genres not linked to "Dexter" from `hbtn_0d_tvshows`, ordered by genre name.
* **18. No Comedy Tonight:** Lists shows without the "comedy" genre from `hbtn_0d_tvshows`, ordered by title.

@bennyonye

* **19. Rotten Tomatoes:** Lists shows from `hbtn_0d_tvshows_rate` by their rating, ordered highest to lowest.
* **20. Best Genre:** Lists genres from `hbtn_0d_tvshows_rate` by their average rating, ordered highest to lowest.

This rewrite condenses the information while retaining crucial details, making it easier to understand the project's scope and individual tasks.

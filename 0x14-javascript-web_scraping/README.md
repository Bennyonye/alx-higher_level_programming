# JavaScript Web Scraping Project

In this project, I delved into practicing file I/O with Node.js and utilized the NPM request framework to interact with both the [Star Wars API](https://swapi.co/) and [JSONPlaceholder API](https://jsonplaceholder.typicode.com). I also explored web scraping in JavaScript using the `request` and `fs` modules.

## Tasks Overview

### 1. Readme
* **File:** [0-readme.js](./0-readme.js)
* **Description:** A JavaScript script that reads and prints the contents of a file.
* **Usage:** Execute `./0-readme.js <file path>`.

### 2. Write me
* **File:** [1-writeme.js](./1-writeme.js)
* **Description:** JavaScript script for writing a string to a file.
* **Usage:** Execute `./1-writeme.js <file path> <string to write>`.

### 3. Status code
* **File:** [2-statuscode.js](./2-statuscode.js)
* **Description:** JavaScript script to display the status code of a `GET` request using the `request` framework.
* **Usage:** Execute `./2-statuscode.js <URL to GET>`.
* **Output:** `code: <status code>`.

### 4. Star Wars movie title
* **File:** [3-starwars_title.js](./3-starwars_title.js)
* **Description:** JavaScript script utilizing the Star Wars API to print the title of a Star Wars movie based on the provided episode number.
* **Usage:** Execute `./3-starwars_title.js <episode number>`.

### 5. Star Wars Wedge Antilles
* **File:** [4-starwars_count.js](./4-starwars_count.js)
* **Description:** JavaScript script utilizing the Star Wars API to print the number of movies featuring the character "Wedge Antilles".
* **Usage:** Execute `./4-starwars_count.js http://swapi.co/api/films/`.

### 6. Loripsum
* **File:** [5-request_store.js](./5-request_store.js)
* **Description:** JavaScript script to store the contents of a webpage in a file.
* **Usage:** Execute `./5-request_store.js <URL to get> <file path to store content in>`.

### 7. How many completed?
* **File:** [6-completed_tasks.js](./6-completed_tasks.js)
* **Description:** JavaScript script utilizing the JSONPlaceholder API to compute the number of tasks completed per user ID.
* **Usage:** Execute `./6-completed_tasks.js https://jsonplaceholder.typicode.com/todos`.

### 8. Who was playing in this movie?
* **File:** [100-starwars_characters.js](./100-starwars_characters.js)
* **Description:** JavaScript script using the Star Wars API to print all characters featured in a given movie.
* **Usage:** Execute `./100-starwars_characters.js <movie ID>`.

### 9. Right order
* **File:** [101-starwars_characters.js](./101-starwars_characters.js)
* **Description:** JavaScript script utilizing the Star Wars API to print all characters featured in a given movie in the same order as they are listed in the `characters` list of the `/films/` response.
* **Usage:** Execute `./101-starwars_characters.js <movie ID>`.

# JavaScript - Web jQuery

This project focused on learning how to manipulate the DOM using jQuery, a powerful JavaScript library. Before implementing jQuery in the hBnB project, we practiced various DOM manipulation tasks. Here's a breakdown of the tasks completed:

## Tasks:

### 0. No jQuery
- **[0-script.js](./0-script.js):** This script utilizes `document.querySelector` to update the text color of the HTML tag `HEADER` to red (`#ff0`).

### 1. With jQuery
- **[1-script.js](./1-script.js):** This script uses jQuery to update the text color of the HTML tag `HEADER` to red (`#ff0`).

### 2. Click and turn red
- **[2-script.js](./2-script.js):** Using jQuery, this script changes the text color of the HTML tag `HEADER` to red (`#ff0`) when the user clicks on the tag `DIV#red_header`.

### 3. Add `.red` class
- **[3-script.js](./3-script.js):** jQuery is employed to add the class `.red` to the HTML tag `HEADER` when the user clicks on the tag `DIV#red_header`.

### 4. Toggle classes
- **[4-script.js](./4-script.js):** This script toggles the class of the HTML tag `HEADER` between `.red` and `.green` when the user clicks on the tag `DIV#red_header`, utilizing jQuery.

### 5. List of elements
- **[5-script.js](./5-script.js):** Using jQuery, this script adds a `LI` element to a list (`UL.my_list`) when the user clicks on the tag `DIV#add_item`. The added element is `<li>Item</li>`.

### 6. Change the text
- **[6-script.js](./6-script.js):** jQuery is utilized to update the text of the HTML tag `HEADER` to "New Header!!!" when the user clicks on the tag `DIV#update_header`.

### 7. Star wars character
- **[7-script.js](./7-script.js):** This script uses jQuery to fetch the name of a Star Wars character from the Star Wars API (`https://swapi.co/api/people/5/?format=json`) and display it in the HTML tag `DIV#character`.

### 8. Star Wars movies
- **[8-script.js](./8-script.js):** jQuery is used to fetch and list all movie titles from the Star Wars API (`https://swapi.co/api/films/?format=json`). The titles are listed in the HTML tag `UL#list_movies`.

### 9. Say Hello!
- **[9-script.js](./9-script.js):** jQuery fetches and displays how to say "Hello" in French using the API `https://fourtonfish.com/hellosalut/?lang=fr`. The translation is displayed in the HTML tag `DIV#hello`.

### 10. No jQuery - document loaded
- **[100-script.js](./100-script.js):** Similar to Task 0, this script uses `document.querySelector` to update the text color of the HTML tag `HEADER` to red (`#ff0`). It works when imported in the `HEAD` tag.

### 11. List, add, remove
- **[101-script.js](./101-script.js):** jQuery is employed to add, remove, and clear `LI` elements from a list based on user click input. It adds a new element when the user clicks `DIV#add_item`, removes the last element when the user clicks `DIV#remove_item`, and clears all elements when the user clicks `DIV#clear_list`.

### 12. Say hello to everybody!
- **[102-script.js](./102-script.js):** This script fetches and displays how to say "Hello" in a given language using the API `https://www.fourtonfish.com/hellosalut/hello/`. It fetches the translation for the language entered in the HTML tag `INPUT#language_code` and displays it in the HTML tag `DIV#hello` when the user clicks on the HTML tag `INPUT#btn_translate`.

### 13. And press ENTER
- **[103-script.js](./103-script.js):** Similar to Task 12, this script fetches and displays how to say "Hello" in a given language using the API `https://www.fourtonfish.com/hellosalut/hello/`. The translation is fetched when either the user clicks on the HTML tag `INPUT#btn_translate` or presses `ENTER` when hovering over the tag `INPUT#language_code`.

These tasks helped us understand and practice jQuery's capabilities in DOM manipulation, making our web applications more dynamic and interactive.

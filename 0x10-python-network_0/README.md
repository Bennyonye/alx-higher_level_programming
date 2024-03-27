# Python Networking Project Overview

In this networking project, I utilized `curl` within Bash scripts to interact with HTTP endpoints, exploring various HTTP headers and request methods. Through this process, I gained insights into URL structures, domain names, HTTP header fields, status codes, and cookie usage.

## Tests :heavy_check_mark:

* [tests](./tests): Directory containing test files provided by ALX.

## Tasks :page_with_curl:

Please note that all `curl` commands in the Bash scripts were designed to interact with a server hosted on an ALX-provided container.

* **0. cURL Body Size**
  * [0-body_size.sh](./0-body_size.sh): Bash script to send a `GET` request to a specified URL and display the size of the response body in bytes.

* **1. cURL to the End**
  * [1-body.sh](./1-body.sh): Bash script to send a `GET` request to a specified URL and display the response body for a `200` status code.

* **2. cURL Method**
  * [2-delete.sh](./2-delete.sh): Bash script to send a `DELETE` request to a specified URL and display the response body.

* **3. cURL Only Methods**
  * [3-methods.sh](./3-methods.sh): Bash script to display all HTTP methods accepted by the server of a given URL.

* **4. cURL Headers**
  * [4-header.sh](./4-header.sh): Bash script to send a `GET` request to a specified URL with a custom header variable `X-School-User-Id=98` and display the response body.

* **5. cURL POST Parameters**
  * [5-post_params.sh](./5-post_params.sh): Bash script to send a `POST` request to a specified URL with predefined variables and display the response body.

* **6. Find a Peak**
  * [6-peak.py](./6-peak.py): [Technical interview preparation] - Python program to find a peak in an unsorted list of integers.
  * [6-peak.txt](./6-peak.txt): Text file containing the algorithm's complexity analysis.

* **7. Only Status Code**
  * [100-status_code.sh](./100-status_code.sh): Bash script to send a `GET` request to a specified URL and display only the status code of the response.

* **8. cURL a JSON File**
  * [101-post_json.sh](./101-post_json.sh): Bash script to send a JSON `POST` request with the contents of a provided file to a specified URL and display the response body.

* **9. Catch Me if You Can!**
  * [102-catch_me.sh](./102-catch_me.sh): Bash script to send a request to `0.0.0.0:5000/catch_me` triggering the server to respond with a message containing `You got me!` in the response body.

These tasks provided valuable insights into HTTP interactions and equipped me with practical skills for networking and web development.

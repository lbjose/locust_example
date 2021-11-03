# **locust_example**<br>
Locust is an easy to use, scriptable and scalable performance testing tool.<br>

To check more about the:<br>
[locust](http://docs.locust.io/en/stable/what-is-locust.html)<br>
[blog](http://oak.cs.ucla.edu/refs/locust/index.html)

Added example showcasing how to use locust to get the load stats for two semantic search models.

To start with, 
- Install locust, for details [follow](https://docs.locust.io/en/stable/installation.html)
- Python >= 3.6

For the example to work,<br> 
```
pip install -r requirements.txt
```


To run the script<br> 
```
locust
```

To run locust with another file<br>
```
locust -f file_name
# Example
locust -f locustfile.py
```

To run locust with another file specifying a particular tag<br>
```
locust -f file_name --tags tag_name
# Example
locust -f locustfile.py --tags sbert
```


Open http://localhost:8089/, to see the load stats in the browser. To have the results saved as csv you can checkout [here](http://docs.locust.io/en/stable/retrieving-stats.html)

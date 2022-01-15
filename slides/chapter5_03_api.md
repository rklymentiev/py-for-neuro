---
type: slides
---

# API requests

---

# What is API

<center><img src="https://res.cloudinary.com/practicaldev/image/fetch/s--g6Ggy_Sx--/c_imagga_scale,f_auto,fl_progressive,h_420,q_auto,w_1000/https://dev-to-uploads.s3.amazonaws.com/i/ogc6dv4qqshabcdetd65.png"></img></center>

Credits: [DEV community](https://dev.to/austinbrownopspark/an-overview-of-apis-and-rest-1093)

Notes: API stands for **Application Programming Interface**. To put in simple words, that's a set of protocols to enable the interaction between the client and the server (database).

Think about Twitter. If you want to get the data about your sent tweets or likes, there is no way to download nice a clean CSV file with your data. However, there is an [official API](https://developer.twitter.com/en/docs/twitter-api) that enables you to connect to Twitter's database and retrieve the data.

We, as clients, create a **request**, that has 4 main methods:

1. `GET` (the one we use most often)
2. `POST`
3. `PUT`
4. `DELETE`

Server sends us data back as a **response**, that is usually in a JSON or XML formats.

Further reading:

* [Blog Post: An Introduction to APIs & 5 APIs a Data Scientist must know!](https://www.analyticsvidhya.com/blog/2016/11/an-introduction-to-apis-application-programming-interfaces-5-apis-a-data-scientist-must-know/)

---

# Basic elements of an API

* **Access**: are you allowed to get access?
* **Request**: what do you want to get?
* **Response**: the resulting data

Notes: Not all APIs are publicly available. Some APIs require some sort of authentication. It can be a secret key that proves that you have an **access** to the server.

**Requests** are usually done by URL, where you can specify some additional **parameters**. For example, parameters could be the dates you want to get your tweets from.

And finally you get the resulting data as the **response**.

---

# Open APIs From Space

**Open Notify** is an open source project to provide a simple programming interface for some of NASA's awesome data.

[Open Notify website](http://open-notify.org/) || [ISS Current Location API](http://open-notify.org/Open-Notify-API/ISS-Location-Now/)


```python
import requests

URL = "http://api.open-notify.org/iss-now.json"
response = requests.get(URL)
print(response.status_code)
```
```out
200
```

Notes: There are several package to handle requests in Python, like `httplib`, `urllib2`, `requests`. Here we will focus only on the last one.

This is an exaple simple API to return the current location of the ISS (International Space Station). It returns the current latitude and longitude of the space station with a unix timestamp for the time the location was valid. This API takes no inputs. Accorfing to the documentation, API URL is: http://api.open-notify.org/iss-now.json.

After `GET`ting the response by that URL we can check its status to make sure everything is fine.

---

# Some of the status codes

| Code | Description |
|--:|:--|
| 200 (OK) | The request was fulfilled. |
| 204 (No response) | Server has received the request but there is no information to send back. |
| 301 (Moved Permanently) | The URL of the requested resource has been changed permanently. The new URL is given in the response. |
| 400 (Bad request) | The request had bad syntax or was inherently impossible to be satisfied. |
| 403 (Forbidden) | The request is for something forbidden. Authorization will not help. |
| 404 (Not found) | The server has not found anything matching the URI given. |
| 500 (Internal Error) | The server encountered an unexpected condition which prevented it from fulfilling the request. |

Notes: Some of the status codes are presented here. The main idea is:

* `2xx` codes indicate success;
* `3xx` codes indicate redirection;
* `4xx` codes indicate error on the client's side;
* `5xx` codes indicate error on the server's side.

Further reading:

* [List of HTTP response status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

---

# Response content

```python
print(response.content)
```
```out
b'{"iss_position": {"longitude": "15.0988", "latitude": "49.8144"}, \
"timestamp": 1616014375, "message": "success"}'
```

```python
print(response.json())
```
```out
{
    'iss_position': {
        'longitude': '15.0988',
        'latitude': '49.8144'
        },
    'timestamp': 1616014375,
    'message': 'success'
}
```

Notes: After we saw that status code was `200` (meaning that request was fulfilled) we can extract the resulting data. There is an attribute `.content` to extract the **raw** data as a binary string (note `b` letter in front of the string), which is not really useful in that case. However, we know that API returns data as JSON file (we know that from the documentation of the API and there is `.json` part in the API URL).

There is a method `.json()` to convert raw data into Python dictionary.

---

# Where is ISS?

<iframe src="iss.html" style="width:100%; height:100%;"></iframe>

Notes:

Full code for the plot:

```python
import requests
import plotly.graph_objects as go
from datetime import datetime

URL = "http://api.open-notify.org/iss-now.json"
response = requests.get(URL)
iss_data = response.json()
fig = go.Figure(
    data=go.Scattergeo(
        lon=[iss_data['iss_position']['longitude']],
        lat=[iss_data['iss_position']['latitude']],
        text=['ISS is over here!'],
        mode='markers',
        marker=dict(color='red')))
fig.update_layout(
    title = f'<b>The Location of ISS @{datetime.fromtimestamp(iss_data["timestamp"])}</b>',
    geo_scope='world')
fig.show()
```

---

# Additional parameters

```python
import requests

URL = "http://api.open-notify.org/iss-pass.json"

parameters = {
    "lat": 52.1205, # Magdeburg, DE
    "lon": 11.6276,
    "n": 3}

response = requests.get(URL, params=parameters)
print(response.status_code)
```
```out
200
```
```python
print(response.url)
```
```out
http://api.open-notify.org/iss-pass.json?lat=52.1205&lon=11.6276&n=3
```

Notes: The international space station (ISS) is an orbital outpost circling high above out heads. Sometimes it’s overhead, but when? It depends on your location. Given a location on Earth (latitude, longitude, and altitude) [International Space Station Pass Times API](http://open-notify.org/Open-Notify-API/ISS-Pass-Times/) will compute the next `n` number of times that the ISS will be overhead.

This API has a set of **parameters** that could be added to the URL to modify the output:

* `lat`: the latitude of the place to predict passes, **required**;
* `lon`: the longitude of the place to predict passes, **required**;
* `alt`: the altitude of the place to predict passes;
* `n`: the number of passes to return.

You can specify these parameters in a separate dictionary and pass it to the `params` argument in `requests.get()` function. The function will put this parameters in a URL after the `?` sign separated by `&`. Or you could manually add these values in the URL without the `params` argument.

---

#  Let's code!

# oplover-api
Unofficial Oploverz API's

# Get All Series
> API ini berfungsi untuk mengambil semua series anime
* URL: ```https://nuubi.herokuapp.com/api/oplover/get_series```
* Methods: ```GET```
> example for GET request: https://nuubi.herokuapp.com/api/oplover/get_series

# Search Anime
> API ini berfungsi untuk mencari series anime
* URL: ```https://nuubi.herokuapp.com/api/oplover/search```
* DATA: ```q=<query>```
* Methods: ```GET```
> example for GET request: https://nuubi.herokuapp.com/api/oplover/search?q=violet

# Get Episode Anime Series
> API ini berfungsi untuk mengambil url episode anime
* URL: ```https://nuubi.herokuapp.com/api/oplover/get_episode```
* DATA: ```url=<url_anime>```
* Methods: ```GET```
> example for GET request: https://nuubi.herokuapp.com/api/oplover/get_episode?url=https://www.oploverz.in/series/violet-evergarden/

# Get Download URL Anime
> API ini berfungsi untuk mengambil url download (lengkap) anime
* URL: ```https://nuubi.herokuapp.com/api/oplover/get_urldl```
* DATA: ```url=<url_episode>```
* Methods: ```GET```
> example for GET request: https://nuubi.herokuapp.com/api/oplover/get_urldl?url=https://www.oploverz.in/boku-no-hero-academia-01-subtitle-indonesia/


* Example <a href="https://github.com/KANG-NEWBIE/oplover-api/blob/master/oplover-dl.py">source code</a> 

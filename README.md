Scrapes Australan weather data from WillyWeather, and sends automated notifications to mobile/desktop.

## Set Up

1. Install dependencies from your terminal:
  `$ python -m pip install requests`
  `$ pip install selenium`
  `$ pip install beautifulsoup4`
2. Dowload a copy of `weathermsg_v2.py`. You'll find the four setup variables under a comment on line 7.
3. Assign the WillyWeather URL of your town/city (NOT your state) to `URL`. It should have a format similar to: https://www.willyweather.com.au/sa/adelaide/adelaide.html
4. Sign up for [Pushover](https://pushover.net/), and assign your API token and user key to `token` and `key` respectively
5. Assign your first name to `first_name`
6. Run the code locally to ensure all notifications are working as designed
7. Schedule the code as a [Cron Job](https://cron-job.org/) or on a free automation platform like [PythonAnywhere](https://www.pythonanywhere.com/)

_Note: pushover app has a one-time $5 USD setup fee after the free trial. I have no affiliation with them, but have paid for it, and found it to be useful for my own purposes._

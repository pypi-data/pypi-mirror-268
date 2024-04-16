from garbevents.custom_sensors_events import GetData
from garbevents.settings import Settings as ST


"gb -p 8889 -s test_custom_sensors_events.py"
ST.url = "https://sensors.wenwo.com"
ST.report_path = "report"
ST.all_events = ["$WebClick", "$pageview"]

addons = [GetData()]

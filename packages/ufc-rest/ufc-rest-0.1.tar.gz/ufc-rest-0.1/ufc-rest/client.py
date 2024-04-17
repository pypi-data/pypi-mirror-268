import requests
from models.event import Event

def main():
    url = "https://d29dxerjsp82wz.cloudfront.net/api/v3/event/live/1081.json"
    data = requests.get(url).json()
    event_obj = Event.from_json(data)
    print(event_obj.get_main_event())
    #print(event_obj)

if __name__ == "__main__":
    main()
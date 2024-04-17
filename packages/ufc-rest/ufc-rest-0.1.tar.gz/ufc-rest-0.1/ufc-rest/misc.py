import requests
import re
from datetime import datetime

def probe_url(url: str):
    response = requests.get(url)
    if response.status_code != 200:
        print(f'Failed to probe URL: {url}')
        return False
    return True

def compile_event_url(event_name: str, event_date: str = None):
    date = datetime.strptime(event_date, "%Y-%m-%dT%H:%MZ")
    fdate = date.strftime("%B-%d-%Y").lower()
    ppv_match = re.search(r'UFC (\d+): ', event_name)
    fn_match = re.search(r'UFC Fight Night: ', event_name)
    url = None
    if ppv_match:
        number = ppv_match.group(1)
        url = f'https://www.ufc.com/event/ufc-{number}'
    elif fn_match:
        url = f'https://www.ufc.com/event/ufc-fight-night-{fdate}'
    if url and probe_url(url):
        return url
    print(f'Failed to compile event URL for {event_name} (Many older events and TUF events are not supported)')
    raise ValueError('Invalid event name')

'''Extract the fmid (UFC API event ID) from the specified event URL at UFC.com'''
def extract_fmid(event_url: str):
    url_match = re.search(r'ufc.com/event/', event_url) 
    if not url_match:
        raise ValueError('Invalid UFC.com event URL')
    response = requests.get(event_url)
    response.raise_for_status()

    fmid_match = re.search(r'data-fmid="(\d+)"', response.text)
    if not fmid_match:
        raise ValueError('Failed to extract fmid from response')
    return fmid_match.group(1)

def test_compile_event_url():
    event_name = 'UFC 269: Oliveira vs Poirier'
    event_date = '2021-12-11T23:00Z'
    event_url = compile_event_url(event_name, event_date)
    assert event_url == 'https://www.ufc.com/event/ufc-269'
    print('PPV event test passed!\n')

    event_name = 'UFC Fight Night: Font vs Aldo'
    event_date = '2021-12-04T23:00Z'
    event_url = compile_event_url(event_name, event_date)
    assert event_url == 'https://www.ufc.com/event/ufc-fight-night-december-04-2021'
    print('Fight Night event test passed!')


if __name__ == "__main__":
    test_compile_event_url() 
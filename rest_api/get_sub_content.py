import requests as req
import json
from src.config import config as cfg


def get_content(scription_data):
    try:
        if scription_data:
            data = {
                "subscriptions": scription_data
            }
            data_json = json.dumps(data)
            headers = {'Content-type': 'application/json'}
            resp = req.post(cfg.get('api', 'GET_CONTENT'), verify=False, data=data_json, headers=headers)
            resp_dict = resp.json()
            return resp_dict
        else:
            return None

    except req.exceptions.HTTPError as httpErr:
        print("Http Error:", httpErr)
    except req.exceptions.ConnectionError as connErr:
        print("Error Connecting:", connErr)
    except req.exceptions.Timeout as timeOutErr:
        print("Timeout Error:", timeOutErr)
    except req.exceptions.RequestException as reqErr:
        print("Something Else:", reqErr)

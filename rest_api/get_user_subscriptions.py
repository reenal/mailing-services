from src.config import config as cfg
import requests


def get_user_subscriptions():
    try:

        final_result = []
        response = requests.get(cfg.get('api', 'GET_USER'), verify=False)
        response.raise_for_status()
        response_json = response.json()
        response_list = response_json['users']
        user_list = cfg.get('user', 'USER').split(',')
        for user_data in response_list:
            if user_data['username'] in user_list:
                result = [user_data['username'], user_data['email'], user_data['subscriptions']]
                final_result.append(result)
        return final_result

    except requests.exceptions.HTTPError as httpErr:
        print("Http Error:", httpErr)
    except requests.exceptions.ConnectionError as connErr:
        print("Error Connecting:", connErr)
    except requests.exceptions.Timeout as timeOutErr:
        print("Timeout Error:", timeOutErr)
    except requests.exceptions.RequestException as reqErr:
        print("Something Else:", reqErr)

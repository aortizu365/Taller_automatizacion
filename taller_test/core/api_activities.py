import requests

url = ""


def get_all_activities():
    endpoint = "/activities"
    peticion = requests.get(url + endpoint)
    return peticion


def get_activity(id):
    endpoint = "/activities/{}".format(str(id))
    peticion = requests.get(url + endpoint)
    return peticion


def create_activity(id, activity_name, date, status):
    endpoint = "/activities"
    headers = {"Content-Type": "application/json"}
    payload = {
        "ID": id,
        "Title": "{}".format(activity_name),
        "DueDate": "".format(date),
        "Completed": status
    }
    peticion = requests.post(url + endpoint, data=payload, headers=headers)
    return peticion


def edit_activity(id, activity_name, date, status):
    endpoint = "/activities"
    headers = {"Content-Type": "application/json"}
    payload = {
        "ID": id,
        "Title": "{}".format(activity_name),
        "DueDate": "".format(date),
        "Completed": status
    }
    peticion = requests.post(url + endpoint, data=payload, headers=headers)
    return peticion


def delete_activity(id):
    endpoint = "/activities/{}".format(str(id))
    peticion = requests.delete(url + endpoint)
    return peticion

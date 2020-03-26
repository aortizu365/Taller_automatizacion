import requests

url = ""


def get_all_authors():
    endpoint = "/authors"
    peticion = requests.get(url + endpoint)
    return peticion


def get_author(id):
    endpoint = "/authors/{}".format(str(id))
    peticion = requests.get(url + endpoint)
    return peticion


def get_libro_author(id):
    endpoint = "/authors/books/{}".format(str(id))
    peticion = requests.get(url + endpoint)
    return peticion

def create_author(id, author_name, date, status):
    endpoint = "/authors"
    headers = {"Content-Type": "application/json"}
    payload = {
        "ID": id,
        "Title": "{}".format(author_name),
        "DueDate": "".format(date),
        "Completed": status
    }
    peticion = requests.post(url + endpoint, data=payload, headers=headers)
    return peticion


def edit_author(id, author_name, date, status):
    endpoint = "/authors"
    headers = {"Content-Type": "application/json"}
    payload = {
        "ID": id,
        "Title": "{}".format(author_name),
        "DueDate": "".format(date),
        "Completed": status
    }
    peticion = requests.post(url + endpoint, data=payload, headers=headers)
    return peticion


def delete_author(id):
    endpoint = "/authors/{}".format(str(id))
    peticion = requests.delete(url + endpoint)
    return peticion

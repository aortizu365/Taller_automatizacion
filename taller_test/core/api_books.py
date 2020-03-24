import requests

url = ""


def get_all_books():
    endpoint = "/books"
    peticion = requests.get(url + endpoint)
    return peticion


def get_book(id):
    endpoint = "/books/{}".format(str(id))
    peticion = requests.get(url + endpoint)
    return peticion


def create_book(id, book_name, date, status):
    endpoint = "/books"
    headers = {"Content-Type": "application/json"}
    payload = {
        "ID": id,
        "Title": "{}".format(book_name),
        "DueDate": "".format(date),
        "Completed": status
    }
    peticion = requests.post(url + endpoint, data=payload, headers=headers)
    return peticion


def edit_book(id, book_name, date, status):
    endpoint = "/books"
    headers = {"Content-Type": "application/json"}
    payload = {
        "ID": id,
        "Title": "{}".format(book_name),
        "DueDate": "".format(date),
        "Completed": status
    }
    peticion = requests.post(url + endpoint, data=payload, headers=headers)
    return peticion


def delete_book(id):
    endpoint = "/books/{}".format(str(id))
    peticion = requests.delete(url + endpoint)
    return peticion

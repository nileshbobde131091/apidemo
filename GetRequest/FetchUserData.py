import json

import jsonpath
import requests


class FetchUserData:

    def test_get_list_users(self):
        url = "https://reqres.in/api/users?page=2"
        response = requests.get(url)
        json_response = json.load(response.text)
        pages = jsonpath.jsonpath(json_response,'total_pages')
        assert pages[0]==5


    def test_create_users(self):
        url = "https://reqres.in/api/user"
        f = open('E:\\Nilesh\\ApiDemoProject\\DataFiles\\jsonfile.json' , 'r')
        request_json = json.load(f.read())
        response = requests.post(url,request_json)
        json_response = json.load(response.text)
        id = jsonpath.jsonpath(json_response,'id')
        assert id[0]==313
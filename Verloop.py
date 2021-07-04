import requests
import xmltodict
import json
import pprint
import jsonpath
import sys
class GoodreadsAPIClient():
    @classmethod
    def get_book_details(cls,URL):
        DICT_USER = {}
        response = requests.get(URL)
        if response.status_code==200:
            pp = pprint.PrettyPrinter(indent=4)
            parsedata = json.dumps(xmltodict.parse(response.text))
            json_content = json.loads(parsedata)
            data = jsonpath.jsonpath(json_content, 'GoodreadsResponse.book')
            dict = data[0]
            try:
                #print(dict["title"])
                DICT_USER["title"]=dict["title"]
            except:
                print("No title")
            try:
                #print(dict["average_rating"])
                DICT_USER["average_rating"] = dict["average_rating"]
            except:
                print("No average_rating")
            try:
                #print(dict["ratings_count"])
                DICT_USER["ratings_count"] = dict["ratings_count"]
            except:
                print("No ratings_count")
            try:
                #print(dict["num_pages"])
                DICT_USER["num_pages"] = dict["num_pages"]
            except:
                print("No num_pages")
            try:
                #print(dict["image_url"])
                DICT_USER["image_url"] = dict["image_url"]
            except:
                print("No image_url")
            try:
                #print(dict["publication_year"])
                DICT_USER["publication_year"] = dict["publication_year"]
            except:
                print("No publication_year")
            try:
                try:
                    #print(dict["authors"]["author"]["name"])
                    DICT_USER["authors"] = dict["authors"]["author"]["name"]
                except:
                    value = 0
                    l = []
                    for i in range(len(dict["authors"]["author"])):
                        #print(dict["authors"]["author"][value]["name"])
                        #DICT_USER["authors"]=dict["authors"]["author"][value]["name"]
                        l.append(dict["authors"]["author"][value]["name"])
                        value += 1
                    str_value = ",".join(l)
                    DICT_USER["authors"]=str_value
            except:
                print("No authors")
        else:
            print(response.status_code)
        return DICT_USER

user_input = ["12067.Good_Omens","22034.The_Godfather","12177850-a-song-of-ice-and-fire","Invalid_URL"]
for index in range(len(user_input)):
    URL = "https://www.goodreads.com/book/show/"+user_input[index]+"?key=LiAf8CTzIGweMPZq8S30mg"
    print(GoodreadsAPIClient.get_book_details(URL))
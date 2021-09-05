import requests
import time
import notifypy

# making a request to the api and converting the response into json and storing it in
InspirationalQuotesDataJSON = requests.get(
    "https://type.fit/api/quotes").json()


# print(InspirationalQuotesDataJSON) # The data format is json and the structure is :-

# [
#     {
#         text: "motivational quote",
#         author: "author name"
#     },
#     {
#         text: "motivational quote",
#         author: "author name"
#     }
# ]


#! each quote here is, the each object inside the json response.
#! i am extracting the author and text name from it and notifying it

for eachQuoteObject in InspirationalQuotesDataJSON:

    # initializing the Notifypy class
    Notification = notifypy.Notify()

    # adding the title of the notification
    # ! make sure to give single quotes after f character because double quotes is used in eachquoteObject["text"]
    Notification.title = f'Author :- {eachQuoteObject["author"]}'

    Notification.message = f'Quote :- {eachQuoteObject["text"]}'

    # this function will send the notification
    Notification.send()

    # it will notify me in every 15 minutes that is 900 seconds
    time.sleep(900)

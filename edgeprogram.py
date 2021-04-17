import requests



def send_data_to_server(value):
    url = "http://localhost:8000"
    data = {
        "value": value
    }
    response = requests.post(url, data= data )
    print(response.text)
    return response.text

def send_buffered_data(value):
    new_list = []
    for val in value:
        response = send_data_to_server(val)
        if response == "ERROR":
            print("ERROR in edge progrem for buffer data: ", val)
            new_list.append(val)

    return new_list

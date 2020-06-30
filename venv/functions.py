import requests

def get_req(link):
    result = requests.get(link) #attempts to grab the website data
    if result.status_code == 200: #check if works
        print("SUCCESSFUL ACCESS")
    else:
        print("UNSUCESSFUL ACCESS")
    return result


def get_result(search):
    result = []
    for result in search:  # loop result list
        print('Title: %s' % result.h3.string)  # geting h3
        result.append(result.h3.string)

        print('Url: %s' % result.a.get('href'))  # geting a.href

        print('Description: %s' % result.find(class_='st').text)  # description
        print('\n###############\n')

    return result





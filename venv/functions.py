import requests

def get_req(link):
    result = requests.get(link) #attempts to grab the website data
    if result.status_code == 200: #check if works
        print("SUCCESSFUL ACCESS")
    else:
        print("UNSUCESSFUL ACCESS")
    return result


def get_result(search, titles, links, descriptions):

    for result in search:  # loop result list
        print('Title: %s' % result.h3.string)  # geting h3
        titles.append(str(result.h3.string))

        print('Url: %s' % result.a.get('href'))  # geting a.href
        links.append(str(result.a.get('href')))

        print('Description: %s' % result.find(class_='st').text)  # description
        descriptions.append(str(result.find(class_='st').text))
        print('-------------------------------------------------')


    return titles, links, descriptions





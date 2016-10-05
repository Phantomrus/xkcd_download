import requests



last_index = int(input("Enter last index of comics: "))

for index in range(last_index, 0, -1):
    page_url = 'http://xkcd.ru/' + str(index)
    page = requests.get(page_url)
    if page.status_code != 404:
        page_code = page.text

        find_image_url_string = page_code.find('img bo')
        find_image_url_start = page_code.find('http', find_image_url_string)
        find_image_url_end = page_code.find('\"', find_image_url_start)
        image_url = page_code[find_image_url_start:find_image_url_end]
        #print(image_url)
        image = requests.get(image_url)
        image_file_name = str(index) + '.png'
        with open(image_file_name, 'wb') as file:
            file.write(image.content)

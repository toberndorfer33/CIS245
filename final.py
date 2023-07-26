import json, requests

base_url = "https://openweathermap.org"
appid = "2e0c39973fd158ebd29ab29e901b0bc3"


def main():
    city = input(str("Enter the city or the ZIP you want to know the weather for: "))
    
    url = f'{base_url}?q={city}&units=imperial&APPID={appid}'
    print(url)
    print ()

    response = requests.get(url)
    print(response)
    
main()
    
cont = input(str("Do you want to search for another city? Y/N: "))


while cont == "Y" :
    main()

else:
    print("Goodbye")
    
    
    



# Current program allows the user to input a city or zip code and will return the json data for the given 
# city or zip. I am still struggling to get the python code to pull the json information out and assign 
# it to a variable. If the city or zip doesnt exist, the command prompts the user to try again. After the
# code pulls data from the weather site, the command asks the user if they want to look at data for a 
# different city or zip


# importing json and request moduels
import json, requests

#video showed the website as /2.5/weather. That url was not working so I had to use /forecast
base_url = "http://api.openweathermap.org/data/2.5/forecast"
appid = "2e0c39973fd158ebd29ab29e901b0bc3"

# defining the main function
def main():
    
    #getting the user input of city or zip to search
    city = input(str("Enter the city or the ZIP you want to know the weather for: "))
    
    # creates the url with the city or zip input by the user, the base url, my appid, and sets the 
    # units to imperial
    
    url = f'{base_url}?q={city}&units=imperial&APPID={appid}'
    
    # prints the url to ensure that the url was created correctly
    print(url)
    print ()

    # program attemps to request the information from the weather website in json
    try:
      response = requests.get(url)
      unformated_data = response.json()
      
      # as of right now, the program only works correctly if the whole json is printed
      print(unformated_data)
     
     
     #python commands to assign json information to python variable still not workng
  
      # temp = unformated_data["main"]["temp"]
      # print("The current temp is: {temp}.")
      # print(unformated_data["main"]["temp"])
   
   # if the city or zip is not found on the weather website, it notifies the user and prompts them to
   # enter another city or zip
   
    except:
      print("That city or zip is not valid try again.")
      main()
  
  
    # code asks the user if they want to search for another city or zip
    cont = str(input("Do you want to search another city? (Type 'yes' or 'no'): "))

    # if the user does want to search another city/zip 
    if cont == "yes":
        main()
        
    # if the user does not want to search another city/zip the program ends
    else:
        print("Goodbye!")

main()    


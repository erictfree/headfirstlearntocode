import requests, json, turtle

def track_craft(craft, lat, long):
    craft.hideturtle()
    craft.penup()
    craft.goto(long, lat)
    craft.pendown()
    craft.showturtle()

screen = turtle.Screen()
screen.setup(1000,500)
screen.bgpic('earth.gif')
screen.setworldcoordinates(-180, -90, 180, 90)

iss = turtle.Turtle()
turtle.register_shape("iss.gif")
iss.shape("iss.gif")

url = 'http://api.open-notify.org/iss-now.json'

response = requests.get(url)

if (response.status_code == 200):
    response_dictionary = json.loads(response.text)
    position = response_dictionary['iss_position']
    lat = float(position['latitude'])
    long = float(position['longitude'])
    track_craft(iss, lat, long)
else:
    print("Houston we have a problem:", response.status_code)

turtle.mainloop()


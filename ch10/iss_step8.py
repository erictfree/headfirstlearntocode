import requests, json, turtle

def setup(craft, window):
    window.setup(1000,500)
    window.bgpic('earth.gif')
    window.setworldcoordinates(-180, -90, 180, 90)
    turtle.register_shape("iss.gif")
    craft.shape("iss.gif")

def track_craft(craft):
    url = 'http://api.open-notify.org/iss-now.json'
    response = requests.get(url)
    if (response.status_code == 200):
        response_dictionary = json.loads(response.text)
        position = response_dictionary['iss_position']
        lat = float(position['latitude'])
        long = float(position['longitude'])
        craft.hideturtle()
        craft.penup()
        craft.goto(long, lat)
        craft.pendown()
        craft.showturtle()
    else:
        print("Houston we have a problem:", response.status_code)

def main():
    iss = turtle.Turtle()
    screen = turtle.Screen()
    setup(iss, screen)
    track_craft(iss)

if __name__ == "__main__":
    main()
    turtle.mainloop()

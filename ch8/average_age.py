users = {} 
users['Kim'] = {'email' : 'kim@oreilly.com','gender': 'f', 'age': 27, 'friends': ['John', 'Josh']}
users['John'] = {'email' : 'john@abc.com','gender': 'm', 'age': 24, 'friends': ['Kim', 'Josh']}
users['Josh'] = {'email' : 'josh@wickedlysmart.com','gender': 'm', 'age': 32, 'friends': ['Kim']}


def average_age(username):
    user = users[username]
    friends = user['friends']

    sum = 0

    for name in friends:
        friend = users[name]
        sum = sum + friend['age']

    average = sum/len(friends)
    print(username + "'s friends have an average age of", average)

average_age('Kim')
average_age('John')
average_age('Josh')

import openai as ai

ai.api_key = input(print("Insert your OpenAI API key"))

#Action, Adventure, Comedy, Drama, Horror, Mystery, and Romance
users = {1: [5,3,5,2,4,3,3], 2: [3,3,4,5,3,2,5], 3: [4,4,5,5,2,2,3]}

#add users to the dictionary
def add_user(user_id, ratings,users):

    users[user_id] = ratings

def menu():
    print()
    print("1. Add user")
    print("2. Delete user")
    print("3. Display users")
    print("4. Recommend 3 movies by your favourite genre")
    print("5. Exit")

def userExists(user_id, users):
    if user_id in users:
        return True
    else:
        return False

def highestGenre(user_id, users):
    highest = 0
    list = []
    for i in range(0, 7):
        if users[user_id][i] == highest:
            list.append(i)
        elif users[user_id][i] > highest:
            list = [i]
            highest = users[user_id][i]
    return list

def recomendation(list,genre):
    for i in range (0,len(list)):
        print(genre[list[i]] + " movies:")
        prompt = "Recommend 3 movies in the genre of"+ genre[list[i]]
        response = ai.Completion.create(engine="text-davinci-002",prompt= prompt,max_tokens=100,n=1,stop=None,temperature=0.5,)
        print(response.choices[0].text)
def main():
    user_id = 3 #Already 3 users in the dictionary
    ratings = [0, 0, 0, 0, 0, 0, 0]

    genre = ["Action", "Adventure", "Comedy", "Drama", "Horror", "Mystery", "Romance"]

    print(menu())
    choice = int(input("Enter your choice: "))
    while choice != 5:
        match choice:
            case 1:
                user_id += 1
                for i in range (0,7):
                    ratings[i] = int(input("Enter rating for genre "+ genre[i] + ":"))
                    while ratings[i] > 5 or ratings[i] < 1:
                        print("Invalid rating")
                        ratings[i] = int(input("Enter rating for genre "+ genre[i] + ":"))
                add_user(user_id,ratings,users)
                print(menu())
                choice = int(input("Enter your choice: "))
            case 2:
                print("Enter user id to delete: ")
                user_id = int(input())
                if userExists(user_id, users) == True:
                    users.pop(user_id)
                else:
                    print("User does not exist")
                print(menu())
                choice = int(input("Enter your choice: "))
            case 3:
                print("Users: ", users)
                print(menu())
                choice = int(input("Enter your choice: "))
            case 4:
                print("Enter user id: ")
                user_id = int(input())
                if userExists(user_id, users) == True:
                    list = highestGenre(user_id, users)
                    print(list)
                    recomendation(list,genre)
                else:
                    print("User does not exist")
                print(menu())
                choice = int(input("Enter your choice: "))
            case _:
                print("Invalid choice")
                print(menu())
                choice = int(input("Enter your choice: "))

main()

import sqlite3

# Connect to the database
while True:
    # Ask the user for the name of the database
    db_name = input("Enter the name of the database you want to connect to or 'q' to quit: ")
    if db_name == 'q':
        # Close the database connection
        conn.close()
        break
    try:
        # Connect to the database
        conn = sqlite3.connect(db_name+".db")
        cursor = conn.cursor()
        print("Connected to the database: ", db_name)
        break
    except sqlite3.Error as e:
        print("An error occurred:", e)
        continue
cursor = conn.cursor()

while True:
    # Ask the user for an option
    option = input("Enter an option (1 -4) or 'q' to quit:\n"
                   "1 = List all tournaments for a given game name\n" 
                   "2 =  Retrieve the average player salary for a given game name\n"
                   "3 = List all tournaments by location\n"
                   "4 = Get number of players by gender\n"
                   "\n")
    
    if option == 'q':
        break
    elif option not in ['1', '2', '3', '4']:
        print("Invalid option.")
        continue
    
    try:
        if option == '1':
            # Ask the user for a game name
            game_name = input("Enter the name of the game:\n"
                              "SuperSmashBros\n"
                              "Tekken 7\n"
                              "StreetFighter 6\n"
                              "LeagueOfLegends\n"
                              "CS:GO\n"
                              "Apex\n"
                              "\n")
            
            # Execute the first query to list all tournaments for the given game name
            cursor.execute('''
            SELECT Tournament.Date 
            FROM Tournament 
            JOIN Game ON Tournament.IdGame = Game.IdGame 
            WHERE Game.Name = ?''', (game_name,))
            tournaments = cursor.fetchall()
            if tournaments:
                print("Tournaments for game: ", game_name)
                for tournament in tournaments:
                    print(tournament)
            else:
                print("No tournaments found for game: ", game_name)
            
        elif option == '2':
            # Ask the user for a game name
            game_name = input("Enter the name of the game:\n"
                              "SuperSmashBros\n"
                              "Tekken 7\n"
                              "StreetFighter 6\n"
                              "LeagueOfLegends\n"
                              "CS:GO\n"
                              "Apex\n"
                              "\n")
            
            # Execute the second query to get the average salary of players for the given game name
            cursor.execute('''
            SELECT AVG(Employee_Data.Wage) 
            FROM Player 
            JOIN Game ON Player.IdGame = Game.IdGame 
            JOIN Employee_Data ON Player.IdEmployeeData = Employee_Data.IdEmployee 
            WHERE Game.Name = ?''', (game_name,))
            average_salary = cursor.fetchone()
            if average_salary[0]:
                print("Average salary of players for game: ", game_name, " is ", average_salary[0])
            else:
                print("No salary found for game: ", game_name)
            
        elif option == '3':
            # Execute the third query to list all tournaments by location
            cursor.execute('''
            SELECT Place.Name, Tournament.IdTournament, Tournament.Date, Tournament.Duration
            FROM Tournament
            JOIN Place ON Tournament.IdPlace = Place.IdPlace
            ''')
            tournaments_by_location = cursor.fetchall()
            if tournaments_by_location:
                print("Tournaments by location:")
                for tournament in tournaments_by_location:
                    print(tournament)
            else:
                print("No tournaments found.")
            
        elif option == '4':
            # Execute the fourth query to get the number of players by gender
            cursor.execute('''
            SELECT Employee_Data.Gender, COUNT(Player.IdPlayer) 
                        FROM Player 
            JOIN Employee_Data ON Player.IdEmployeeData = Employee_Data.IdEmployee 
            GROUP BY Employee_Data.Gender
            ''')
            players_by_gender = cursor.fetchall()
            if players_by_gender:
                print("Number of players by gender:")
                for player in players_by_gender:
                    print(player)
            else:
                print("No players found.")
    except sqlite3.Error as e:
        print("An error occurred:", e)

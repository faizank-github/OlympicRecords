olympic_records = {}

def record_medal_details():
    nation_name = input("Enter Country Name: ")
    event_name = input("Enter Sport Name: ")
    medal_count = int(input("Enter total medals won: "))

    if nation_name not in olympic_records:
        olympic_records[nation_name] = {"total_medals": 0}
    if event_name not in olympic_records[nation_name]:
        olympic_records[nation_name][event_name] = []

    for i in range(medal_count):
        print(f"Enter Details for medal {i + 1}")
        participant_name = input("Enter Athlete Name: ")
        win_year = int(input("Enter Year: "))
        medal_category = input("Enter Medal Won (Bronze/Silver/Gold): ")
        olympic_records[nation_name][event_name].append({'athlete': participant_name, 'medal' : medal_category, 'year': win_year})
        
        olympic_records[nation_name]["total_medals"] += 1

def show_event_details():
    nation_name = input("Enter Country Name: ")
    event_name = input("Enter Sport Name: ") 

    if nation_name in olympic_records and event_name in olympic_records[nation_name]:
        print(f"\nDetails for {event_name} in {nation_name}:")
        for medal_info in olympic_records[nation_name][event_name]:
            print(f"Athlete: {medal_info['athlete']}, Medal: {medal_info['medal']}, Year: {medal_info['year']}")
    else:
        print("No records found for the given country and sport.")

def show_all_records():
    for nation, events in olympic_records.items():
        print(f"\nCountry: {nation}")
        for event, medals in events.items():
            if event != "total_medals":
                print(f"  Sport: {event}")
                for medal_info in medals:
                    print(f"    Athlete: {medal_info['athlete']}, Medal: {medal_info['medal']}, Year: {medal_info['year']}")

def find_athlete_performance():
    participant_name = input("Enter Athlete Name to search: ")
    found = False

    for nation, events in olympic_records.items():
        for event, medals in events.items():
            if event != "total_medals":
                for medal_info in medals:
                    if medal_info['athlete'].lower() == participant_name.lower():
                        found = True
                        print(f"\nAthlete: {medal_info['athlete']}")
                        print(f"  Country: {nation}")
                        print(f"  Sport: {event}")
                        print(f"  Medal: {medal_info['medal']}")
                        print(f"  Year: {medal_info['year']}")

    if not found:
        print("No records found for the specified athlete.")

def show_olympic_summary():
    medal_tally = {"Gold": 0, "Silver": 0, "Bronze": 0}
    total_participants = 0
    total_medals = 0

    for nation, events in olympic_records.items():
        for event, medals in events.items():
            if event != "total_medals":
                total_participants += len(medals)
                for medal_info in medals:
                    medal_tally[medal_info['medal']] += 1
                    total_medals += 1

    if total_participants > 0:
        avg_medals_per_participant = total_medals / total_participants
    else:
        avg_medals_per_participant = 0

    print("\nStatistics:")
    print(f"Total Athletes: {total_participants}")
    print(f"Total Medals: {total_medals}")
    print(f"Average Medals per Athlete: {avg_medals_per_participant:.2f}")
    print(f"Medal Distribution: Gold: {medal_tally['Gold']}, Silver: {medal_tally['Silver']}, Bronze: {medal_tally['Bronze']}")

while True:
    print("\nOlympic Medal and Athlete Tracker\n")
    print("1. Record Medal Details")
    print("2. Show Event Details")
    print("3. Show All Records")
    print("4. Find Athlete Performance")
    print("5. Show Summary Statistics")
    print("6. Exit")
    option = input("Choose an option: ")

    if option == '1':
        record_medal_details()
    elif option == '2':
        show_event_details()
    elif option == '3':
        show_all_records()
    elif option == '4':
        find_athlete_performance()
    elif option == '5':
        show_olympic_summary()
    elif option == '6':
        break
    else:
        print("Invalid option, please try again.")

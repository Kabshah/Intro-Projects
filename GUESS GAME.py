state_capitals={"New Mexico": "Santa Fe", "Texas": "Austin", "Ohio":"Columbus", "Georgia": "Atlanta",'Utah': 'Salt Lake City',
'Vermont': 'Montpelier','Virginia': 'Richmond','Washington': 'Olympia','West Virginia': 'Charleston','Wisconsin': 'Madison',
'Wyoming':'Cheyenne','North Carolina': 'Raleigh','North Dakota': 'Bismarck','Ohio': 'Columbus','Oklahoma': 'Oklahoma City','Oregon': 'Salem',
'Pennsylvania': 'Harrisburg','Rhode Island': 'Providence','South Carolina': 'Columbia','South Dakota': 'Pierre','Tennessee':' Nashville',
'New York': 'Albany' ,'Illinois': 'Springfield','Indiana': 'Indianapolis','Iowa': 'Des Moines','Kansas': 'Topeka','Kentucky': 'Frankfort',
'Louisiana': 'Baton Rouge','Maine': 'Augusta','Maryland': 'Annapolis','Massachusetts':'Boston','Michigan': 'Lansing','Minnesota': 'St. Paul',
'Mississippi': 'Jackson','Missouri': 'Jefferson City','Montana': 'Helena','Nebraska': 'Lincoln','Nevada': 'Carson City',
'New Hampshire': 'Concord','New Jersey': 'Trenton','Hawaii': 'Honolulu','Idaho': 'Boise','Alabama': 'Montgomery','Alaska': 'Juneau',
'Arizona': 'Phoenix','Arkansas': 'Little Rock','California': 'Sacramento','Colorado': 'Denver','Connecticut': 'Hartford','Delaware': 'Dover',
'Florida': 'Tallahassee'}
print("\t\tGuess The Capitals Game")
correct = 0
incorrect = 0
for key, value in state_capitals.items():
    query = input("\nWhat is the capital of " + key.title() + "? (or 'Exit' to quit):").title().strip()
    if query == value:
        print("Your answer is correct")
        correct += 1
    elif query != value:
        print("Your answer is wrong","\nThe capital of", key.title(), "is" ,value.title())
        incorrect += 1
        break
if query == 'Exit':
    print("Thanks for playing!")

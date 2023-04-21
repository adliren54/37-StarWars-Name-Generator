print("STAR WARS NAME GENERATOR")

initial = input("Enter your first name, last name, Mum's maiden name and the city you were born in: ")

vorname = initial.split()[0].capitalize()
nachname = initial.split()[1].lower()
maidenName = initial.split()[2].capitalize()
gebursort = initial.split()[3].lower()

result = f"Your Star Wars name is {vorname[:3]}{nachname[:2]} {maidenName[:1]}{gebursort[:2:-1]}"

print(result)
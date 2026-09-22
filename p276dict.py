country_population = {
    "China": 143,
    "India": 136,
    "USA": 32,
    "UK": 21
}
print("enter print to see the country population")
print("enter add to add a new country and its population")
print("enter remove to remove a country and its population")
print("enter query to query the population of a country")
options = input("Enter your option: ")
if options == "print":
    print(country_population)
elif options == "add":
    country = input("Enter the country name: ")
    population = int(input("Enter the population in millions: "))
    country_population[country] = population
    print(f"{country} with population {population} million added.")
    print(country_population)
elif options == "remove":
    country = input("Enter the country name to remove: ")
    if country in country_population:
        del country_population[country]
        print(f"{country} removed from the dictionary.")
    else:
        print(f"{country} not found in the dictionary.")
    print(country_population)
elif options == "query":
    country = input("Enter the country name to query: ")
    if country in country_population:
        print(f"The population of {country} is {country_population[country]} million.")
    else:
        print(f"{country} not found in the dictionary.")
    print(country_population)
    
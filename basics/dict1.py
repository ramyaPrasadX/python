# creating a dictionary
population = {
    'china' : 143,
    'india' : 136,
    'usa' : 32,
    'pakistan' : 21
}

#define add function to add a new country to the dict
def add() :
    country = input("Enter country name to add:")
    # convert the input given by user to all lowercases
    country = country.lower()
    if country in population:
        print("Country already exists in our database.")
        return
    p = input(f"Enter the population for {country}")
    p = float(p)
    population[country] = p #adds new key value pair to dictionary
    print_all() # defined below

    # define remove function
def remove():
    country = input("Enter country to remove:")
    country = country.lower()
    if country not in population:
        print("Country doesn't exist in our database")
        return
    del population[country]
    print_all()

#define query function
def query():
    country = input("enter country name to query:")
    country = country.lower()
    if country not in population:
        print("Country doesn't exist in our database")
        return
    print(f"Population of {country} is: {population[country]} crores")

#deine the print all function
def print_all():
    for country, p in population.items():
        print(f"{country}==>{p}")
def main():
    op = input("enter operation (add, remove, query or print):")
    if op.lower()== 'add':
        add()
    elif op.lower()=='remove':
        remove()
    elif op.lower()== 'query':
        query()
    elif op.lower() == 'print':
        print_all()

if __name__ == '__main__':
    main()
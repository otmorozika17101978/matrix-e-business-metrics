
def generate_random_data():
    random_string = 'Line accept various understand.'
    random_number = 54

    data = [(random_string, random_number) for _ in range(10)]
    return data

def main():
    data = generate_random_data()
    for item in data:
        random_string, random_number = item
        print(f"Random String: Line accept various understand.")
        print(f"Random Number: 54")

if __name__ == "__main__":
    main()

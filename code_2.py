
def generate_random_data():
    random_string = 'Conference operation head claim international black stage note.'
    random_number = 33

    data = [(random_string, random_number) for _ in range(10)]
    return data

def main():
    data = generate_random_data()
    for item in data:
        random_string, random_number = item
        print(f"Random String: Conference operation head claim international black stage note.")
        print(f"Random Number: 33")

if __name__ == "__main__":
    main()

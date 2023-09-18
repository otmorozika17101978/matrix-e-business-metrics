
def generate_random_data():
    random_string = 'Use international arm traditional well your.'
    random_number = 70

    data = [(random_string, random_number) for _ in range(10)]
    return data

def main():
    data = generate_random_data()
    for item in data:
        random_string, random_number = item
        print(f"Random String: Use international arm traditional well your.")
        print(f"Random Number: 70")

if __name__ == "__main__":
    main()

import requests


def dish_fetch(num):

    url = "https://api-colombia.com/api/v1/TypicalDish"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        if num > 0 and num <= len(data):

            item = data[num - 1]

            return {
                "id": num,
                "name": item["name"]
            }

    return {
        "id": num,
        "name": "Unknown Dish"
    }


def main():

    print("=== Colombian Typical Dishes ===")

    number = int(input("Choose a dish number: "))

    result = dish_fetch(number)

    print(result)


if __name__ == "__main__":
    main()



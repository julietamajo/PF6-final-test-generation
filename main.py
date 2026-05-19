import requests


def dish_fetch(num):

    url = f"https://api-colombia.com/api/v1/TypicalDish/{num}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        return {
            "id": data["id"],
            "name": data["name"]
        }

    return {
        "id": num,
        "name": "Unknown Dish"
    }


def main():

    print("Hello learners!")
    print("=== Colombian Typical Dishes ===")

    while True:

        select_user = input(
            "\nIngrese el número del plato o escriba 'salir': "
        )

        if select_user.lower() == "salir":
            print("Programa finalizado.")
            break

        if not select_user.isdigit():
            print("Ingrese un número válido.")
            continue

        dish = dish_fetch(int(select_user))

        print(f"\nID del plato: {dish['id']}")
        print(f"Nombre del plato: {dish['name']}")


if __name__ == "__main__":
    main()

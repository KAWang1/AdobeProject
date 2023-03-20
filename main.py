from api_service import get_palette


if __name__ == '__main__':
    prompt = input("What would you like a color palette for?\n")
    number = input("How many colors would you like?\n")
    get_palette(prompt, number)

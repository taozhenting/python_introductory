filename_cats = "cats.txt"
filename_dogs = "dogs.txt"
try:
    with open(filename_cats) as file_cats:
        for line in file_cats:
            print(
                "您好，" +
                line.strip() +
                "猫咪!"
            )
except FileNotFoundError:
    pass

try:
    with open(filename_dogs) as file_dogs:
        for line in file_dogs:
            print(
                "您好，" +
                line.strip() +
                "小狗!"
            )
except FileNotFoundError:
    pass
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
    print("抱歉！" +
          filename_cats +
          "没找到！")

try:
    with open(filename_dogs) as file_dogs:
        for line in file_dogs:
            print(
                "您好，" +
                line.strip() +
                "小狗!"
            )
except FileNotFoundError:
    print("抱歉！" +
          filename_dogs +
          "没找到！")
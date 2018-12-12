class User():
    def __init__(self,first_name,last_name,*user_info):
        self.first_name = first_name
        self.last_name = last_name
        self.user_info = user_info
    def describe_user(self):
        print(
            "\n" +
            self.first_name +
            self.last_name +
            "用户信息摘要:"
        )
        for self.info in self.user_info:
            print(
                self.info
            )
    def greet_user(self):
        print(
            "您好, " +
            self.first_name +
            self.last_name +
            "!"
        )

tao = User('tao','zhenting','36','shanghai')
tao.describe_user()
tao.greet_user()

wei = User('wei','yun','32','shanghai')
wei.describe_user()
wei.greet_user()


class User():
    def __init__(self,first_name,last_name,*user_info):
        self.first_name = first_name
        self.last_name = last_name
        self.user_info = user_info
        self.login_attempts = 0
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
    #尝试登陆次数
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(User):
    def __init__(self,first_name,last_name,*user_info):
        super().__init__(first_name,last_name,*user_info)
        self.privileges = ['can add post','cat delete post','cat ban user']
    def show_privileges(self):
        print(
            "这是管理员\n权限有:"
        )
        for self.privilege in self.privileges:
            print(self.privilege)
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

tao = User('tao','zhenting','36','shanghai')
tao.increment_login_attempts()
print(tao.login_attempts)
tao.increment_login_attempts()
print(tao.login_attempts)
tao.increment_login_attempts()
print(tao.login_attempts)
tao.reset_login_attempts()
print(tao.login_attempts)
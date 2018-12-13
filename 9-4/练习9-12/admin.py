from user import User
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
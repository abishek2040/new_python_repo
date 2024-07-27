from User import User
from Privileges import Privileges, Admin

user1 = User("Abishek", "Phuyal")
user1.describe_user()


User2 = Admin("Abishek", "Phuyal")
User2.privileges.show_privileges()
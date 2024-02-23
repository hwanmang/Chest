
class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def display(self):
        print(f"회원 이름 : {self.name}")
        print(f"회원 아이디 : {self.username}")


class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author


member1 = Member("Tom", "tom111", "password111")
member2 = Member("Kim", "kim222", "password222")
member3 = Member("Lee", "lee333", "password333")

members = []
members.append(member1)
members.append(member2)
members.append(member3)


print("회원 목록:")
for member in members:
    print(member.name)

posts = []

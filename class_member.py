
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
for member in members:
    for i in range(3):  # 각 회원당 3개의 게시글 작성
        title = f"{member.name}의 게시글 {"개시글", i+1}"
        content = f"{member.name}의 게시글 내용 {"내용", i+1}"
        post = Post(title, content, member.username)
        posts.append(post)

# 특정 유저가 작성한 게시글 제목 출력
print("특정 유저가 작성한 게시글 제목:")
for post in posts:
    if post.author == "Kim":
        print(post.title)

# 특정 단어가 포함된 게시글 제목 출력
print("\n특정 단어가 포함된 게시글 제목:")
for post in posts:
    if '1' in post.content:
        print(post.title)


class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def display(self):
        print("회원 정보")
        print(f"회원 이름 : {self.name}")
        print(f"회원 아이디 : {self.username}")


class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author


members = []
member_list = [
    Member("김땡땡", "tom111", "password111"),
    Member("이머머", "kim222", "password222"),
    Member("박누구", "lee333", "password333")
]

for member in member_list:
    members.append(member)

print("회원 목록:")
for member in members:
    print(member.name)

print("\n")

posts = []
for member in members:
    for i in range(3):
        title = f"{member.name}의 {i+1}번째 게시글"
        content = f"안녕하세요. {member.name}입니다 {i+1}번째 게시글입니다.\n"
        post = Post(title, content, member)
        posts.append(post)
        # print(post)

print("김땡땡이 작성한 게시글 제목")
for post in posts:
    if '김땡땡' in post.author.name:
        print(post.title)

print("\n")

print("'1번째'이 들어간 게시글 제목")
for post in posts:
    if '1번째' in post.content:
        print(post.title)

print("\n")

for post in posts:
    print(post.title)
    print(post.content)

while True:
    new_member_ask = input("회원을 추가하시겠습니까? (y/n): ")
    if new_member_ask.lower() == "y":
        print("회원 등록하려면 입력해주세요")
        name = input("회원 이름을 입력해주세요: ")
        username = input("회원 아이디를 입력해주세요: ")
        password = input("비밀번호를 설정해주세요: ")

        new_member = Member(name, username, password)
        members.append(new_member)

        print("회원 등록 되었습니다.")
        new_member.display()
    elif new_member_ask.lower() == "n":
        print("게시글 추가를 종료합니다.")
        break
    else:
        print("유효한 입력이 아닙니다.")
        continue

while True:
    new_post_ask = input("게시글을 추가하시겠습니까? (y/n): ")
    if new_post_ask.lower() == "y":
        author = input("아이디를 입력하세요: ")
        title = input("게시글 제목을 입력하세요: ")
        content = input("게시글 내용을 입력하세요: ")

        new_post = Post(title, content, member)
        posts.append(new_post)

        print("추가된 게시글")
        print(f"게시글  제목: {new_post.title}")
        print(f"게시글 내용: {new_post.content}")
        print(f"작성자 아이디: {new_post.author.username}")
    elif new_post_ask.lower() == "n":
        print("게시글 추가를 종료합니다.")
        break
    else:
        print("유효한 입력이 아닙니다.")
        continue

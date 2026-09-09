from faker import Faker

fake = Faker()
word = fake.word()
answers = ""
count = 20

while True:
    succeed = True
    print()
    for w in word:
        if w in answers:
            print(w, end=" ")
        else:
            print("_", end=" ")
            succeed = False
    print()
    print()

    if succeed:
        print("게임 종료")
        break
    elif count == 0:
        print("게임 종료")
        print(f"정답: {word}")
        break

    answer = input("알파벳을 입력하세요: ")
    if answer not in answers:
        answers += answer

    print("=" * 30)
    if answer in word:
        print("포함되어 있습니다.")

    else:
        print("포함되어 있지 않습니다.")
        count -= 1
        print(f"남은 기회 : {count}")
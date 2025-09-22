boys = list(input().split())
girls = list(input().split())

boys.sort()
girls.sort()

if len(boys) == len(girls):
    print("Идеальные пары:")

    for i in range(len(boys)):
        print(f"{boys[i]} и {girls[i]}")
else:
    print("Внимание, кто-то может остаться без пары!")
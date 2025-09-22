import re

stream = list(input().split())

total_views = 0
unique_users = set()

pattern = r'^([^,]+),[^;]+;(\d+)$'

for record in stream:
    match = re.match(pattern, record)

    if match:
        user = match.group(1)
        views = int(match.group(2))
        total_views += views
        unique_users.add(user)

avg_views_per_user = total_views / len(unique_users)
print(f"Среднее количество просмотров на уникального пользователя: {avg_views_per_user}")



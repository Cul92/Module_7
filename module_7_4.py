team1 = ('Мастера кода')
team2 = ('Волшебники данных')
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'

print("В команде %s участников: %s !" % (team1, team1_num))

print("Итого сегодня в командах участников: %s и %s !" % (team1_num, team2_num))

print("Команда {} решила задач: {} !".format(team2, score_2))

print("{} решили задачи за {:.1f} с !".format(team2, team2_time))

print(f"Команды решили {score_1} и {score_2} задач.")

print(f"Результат битвы: {result}")

print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg:.1f} секунды на задачу!")

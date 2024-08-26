units = int(input())
hp = int(input())
spawn = int(input())

def min_rounds(soldiers, enemy_health, enemy_soldiers):
    rounds = 0
    while enemy_soldiers > 0 and enemy_health > 0:
        enemy_soldiers -= soldiers
        enemy_health -= soldiers
        rounds += 1
    if enemy_soldiers <= 0 and enemy_health <= 0:
        return rounds
    else:
        return -1

# Пример использования функции

print(min_rounds(units , hp, spawn))

id_, level = input().split()

class next_level:
    def __init__(self, id_ = 'codetree', level= 10):
        self.id_ = id_
        self.level = level

next_level_ori = next_level()
print(f'user {next_level_ori.id_} lv {next_level_ori.level}')

next_level_result = next_level(id_, level)
print(f'user {next_level_result.id_} lv {next_level_result.level}')
def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


def step2_umbrella():
    print('Хорошие пельмени - это очень вкусно!\n'
          'На самом деле рецепт простой: много мяса, мало теста')


def step2_no_umbrella():
    print('Ну и правильно. Дождь не на улице')


if __name__ == '__main__':
    step1()

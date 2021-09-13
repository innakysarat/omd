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
    print('\033[32mТогда утка с зонтиком просит пельменей\n'
          'Рецепт простой: много мяса, мало теста\033[0m')


def step2_no_umbrella():
    print('\033[31mВы уверены, что хотите лишить утку зонтика?\033[0m')
    option = ''
    options = {'да': False, 'нет': True}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    if options[option]:
        return step2_umbrella()
    print('\033[31mТогда утка без зонтика просит 2 сидра\033[0m')


if __name__ == '__main__':
    step1()

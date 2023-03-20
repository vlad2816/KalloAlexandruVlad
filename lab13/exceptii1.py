import logger


def circle_area(radius):
    '''Calculate circle area. Radius has to be positive int.

    Args: 
        - Radius (float) : Circle radius.

        Raises: 
        - ValueError: if radius is less than 0
    '''
    if radius < 0:
        raise ValueError('[Alarm] Radius need to be > than 0')

    return 3.14 * radius ** 2


# try:
#     number = float(input('Adauga un numar pentru raza cercului: '))
# except ValueError:
#     print('[Critical] Please input a float or an int.')

# else:
try:
    print(circle_area('sss'))
except (ValueError, TypeError) as err:
    logger.error(err)
except Exception:
    print('Hello Exception ')


print('End')

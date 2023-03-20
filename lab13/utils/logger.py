def error(msg):
    print(f'[Error] {msg}')


def warning(warning):
    print(f'[Warning] {warning}')


def info(info):
    print(f'[info] {info}')


def debug(debug):
    print(f'[debug] {debug}')


# Module guard, sa se execute doar in program nu si cand este importat.
if __name__ == '__main__':
    print('From module code')

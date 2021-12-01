

def calculate(input_file_name):
    with open(input_file_name, 'r', encoding='utf-8') as f:
        input_data = f.read().splitlines()

    report = [int(val) for val in input_data]

    increased = 0
    decreased = 0
    prev = report[0]

    for elem in report[1:]:
        if elem >= prev:
            increased += 1
        else:
            decreased += 1
        prev = elem

    return increased, decreased


if __name__=='__main__':
    input_file_name = 'input_data.txt'
    increased, decreased = calculate(input_file_name)
    print(f'{increased=} {decreased=}')

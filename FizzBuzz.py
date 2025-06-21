

def processLogs(logs,threshold):

    for i in logs:
        print(f'Value of i is:{i}')
        for item in i:
            print(f'the value of item is {item}')
            if item != ' ':
                result = search_if_value_exist(item,logs)
                print(f'Resultado de veces encontradas el valor de {item} es de: {result} veces')
                
        


def search_if_value_exist(value,logs):

    result = 0
    counter = 0
    previus_value = None

    for i in logs:

        print(f'Value of i into the funtion is:{i}')

        for item in i:

            print(f'The value of item into the funtion is {item}')

            current_value = item

            if previus_value == item:
                break
            else:
                if current_value == value:
                    result += 1
                    previus_value = item

            counter += 1

            if counter == 4:
                counter = 0
                previus_value = None
                break

    return result            

if __name__ == '__main__':
    array_logs = ["1 2 50", "1 7 70", "1 3 20", "2 2 17"]
    processLogs(array_logs,2)


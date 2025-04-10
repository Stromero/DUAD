from main_module_week_6_exercices import sum_numbers, reverse_string, num_of_uppercase, order_alf, retornar_lista_numeros_primos
import pytest

# *** 3 unit test for exercise #3 ***
def test_sum_number_correctly():
    #AAA
    #Arrange
    list_to_sum = [1,2,3,4,5,6,7,8,9,10]
    #Act
    result = sum_numbers(list_to_sum)
    #Assert
    assert result == 55

def test_sum_number_with_negative_values():
    #AAA
    #Arrange
    list_to_sum = [2,8,-4,25,-15,6,9,-3,4,5]
    #Act
    result = sum_numbers(list_to_sum)
    #Assert
    assert result == 37

def test_sum_number_with_argument_that_is_not_a_list():
    #AAA
    #Arrange
    list_to = 'Hello'
    #Act & Assert
    with pytest.raises(ValueError):
        sum_numbers(list_to)

# *** 3 unit test for exercise #4 ***
def test_reverse_string_correctly():
    #AAA
    #Arrange
    text_to_process = 'My name is Steven'
    #Act
    result = reverse_string(text_to_process)
    #Assert
    assert result == 'nevetS si eman yM'

def test_reverse_empty_value():
    #AAA
    # Arrange
    text_to_process = ''
    #Act
    result = reverse_string(text_to_process)
    #Assert
    assert result == ''    

def test_reverse_string_with_different_value():
    #AAA
    #Arrange
    text_to_process = 1854
    #Act & Assert
    with pytest.raises(ValueError):
        reverse_string(text_to_process)

# *** 3 unit test for exercise #5 ***
def test_count_of_uppercase_and_lowercase_correctly():
    #AAA
    #Arrange
    text_to_process = 'Steven Romero'
    #Act
    result = num_of_uppercase(text_to_process)
    #Assert
    assert result == (2,10)

def test_count_of_just_lowercase_letters_in_string():
    #AAA
    #Arrange
    text_to_process = 'my name is luka'
    #Act
    result = num_of_uppercase(text_to_process)
    #Assert
    assert result == (0,12)

def test_count_of_uppercase_and_lowercase_with_incorrect_input():
    #AAA
    #Arrange
    text_to_process = 1234
    #Act & Assert
    with pytest.raises(ValueError):
        num_of_uppercase(text_to_process)
    
# *** 3 unit test for exercise #6 ***

def test_order_alf_correctly():
    #AAA
    #Arrange
    text_to_process = 'python-variable-funcion-computadora-monitor'
    #Act
    result = order_alf(text_to_process)
    #Assert
    assert result == 'computadora-funcion-monitor-python-variable'

def test_order_alf_correctly_with_big_amount_of_words():
    #AAA
    #Arrange
    text_to_process = 'Steven-Carmen-Alex-Estefany-Jonathan-Priscilla-Michelle'
    #Act
    result = order_alf(text_to_process)
    #Assert
    assert result == 'Alex-Carmen-Estefany-Jonathan-Michelle-Priscilla-Steven'

def test_order_alf_with_number_value():
    #AAA
    #Arrange
    text_to_process = 1234
    #Act & Assert
    with pytest.raises(ValueError):
        order_alf(text_to_process)

# *** 3 unit test for exercise #7 ***

def test_list_of_prime_numbers_correctly():
    #AAA
    #Arrange
    list_to_process = [1,2,3,4,5,6,7,8,9,10]
    #Act
    result = retornar_lista_numeros_primos(list_to_process)
    #Assert
    assert result == [2,3,5,7]

def test_list_of_prime_numbers_with_big_amount_of_number():
    #AAA
    #Arrange
    list_to_process = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
    #Act
    result = retornar_lista_numeros_primos(list_to_process)
    #Assert
    assert result == [ 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

def test_list_of_prime_numbers_with_incorrect_input():
    #AAA
    #Arrange
    list_to_process = 'Hello Numbers'
    #Act & Assert
    with pytest.raises(ValueError):
        retornar_lista_numeros_primos(list_to_process)
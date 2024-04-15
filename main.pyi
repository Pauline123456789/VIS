def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Ошибка: деление на ноль"
    
def display_menu():
    print("4. Деление")

def main():
    while True:
        display_menu()
        choice = input("Введите номер операции (или 0 для выхода): ")
        if choice == '4':
            num1, num2 = map(float, input("Введите два числа через пробел (делимое и делитель): ").split())
            if num2 == 0:
                print("Ошибка: деление на ноль")
                continue
            print("Результат деления:", divide(num1, num2))
        else:
            print("Неверный ввод. Попробуйте снова.")



if __name__ == "__main__":
    main()
#Programa criado com auxílio do Iãh!
print("---------------------------------")
print("• Program for calculating grades")
print("Insert values between 0 and 100!")
print("---------------------------------")
user = str(input("Insert your name: "))
print(f"Hey, {user}. \nAt anytime insert 'end' to end the program!\n")

grade = []
values = 0.0

while True:
    values = input(f"Insert the {len (grade) + 1}° grade: ")
    try:
        if float(values) in range(101):
            grade.append(float(values)) # O comando 'append()' serve para empurrar o valor dentro dos () para dentor do vetor
        elif float(values) not in range(101):
            print('> '+'\033[31m'+'Insert values between 0 and 100!'+'\033[0;0m')
            values = 0
            continue
    except:
        if str(values).upper()  == "END": # O 'upper()' serve para converter o input do usuário em CAPS (e vice-versa)
            break
##====================xXXx====================##

average = sum(grade) / len(grade)
print(f"\nFinal media: {average:.2f}")
print("Entered values: ", grade)
input("")
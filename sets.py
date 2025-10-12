math_debtors = {"Петров", "Сидоров", "Иванов", "Комаров"}
rulang_debtors = {"Петров", "Сидоров", "Быков"}
cs_debtors = {"Петров", "Попов", "Быков"}

print(math_debtors & cs_debtors) # множество тех, у кого долги и по математике, и по информатике
print(math_debtors & rulang_debtors & cs_debtors) # множество тех, у кого долги по всем трем предметам
print(math_debtors ^ rulang_debtors ^ cs_debtors) # множество тех, у кого ровно один долг
print("Сидоров" in math_debtors or rulang_debtors) # есть ли Сидиров в должникам по математике или в должникам по русскому
Collection_Nums = []

for i in range(10):
    _varNum = int(input(f"Escreva o {i + 1}º número: "))
    Collection_Nums.append(_varNum)

for i in range(len(Collection_Nums)):
    if Collection_Nums[i] < 0:
        Collection_Nums[i] = 0

print("Sua lista de números com o negativo corrigido é: ")
print(Collection_Nums)

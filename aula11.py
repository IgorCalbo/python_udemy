# ordem de execução
# 1. (n + n)
# 2. **
# 3. * / // %
# 4. + -


conta_errada = 1 + 1 ** 5 + 5 #  7
conta_certa = (1 + 1) ** (5 + 5) # 1024
conta_certa2 = (1 + int(0.5 + 0.5)) ** (5 + 5) # 1024

print(conta_errada)
print(conta_certa)
print(conta_certa2)
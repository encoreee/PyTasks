k = ord('A')
a = []
nr = 26  # количество строк
nc = 26  # количество столбцов
for r in range(nr):
    a.append([])
    for c in range(nc):
        let = chr(k)
        a[r].append(let)  # добавляем очередной элемент в строку
        k += 1
        if r == c:
            let = chr(k)
            k = ord('A')
            break


print(a)

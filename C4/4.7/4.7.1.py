def count(array, element):
    count = 0
    for a in array:
        if a == element:
            count += 1
    return count

array = list(map(int, input().split()))
element = int(input())

print(count(array, element))
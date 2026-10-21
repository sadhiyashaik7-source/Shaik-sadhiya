def main():
    fruits = ['apple', 'banana', 'cherry']
    print("Original list:", fruits)

    fruits.append('orange')
    print("After append:", fruits)

    fruits.insert(1, 'mango')
    print("After insert aat index 1:", fruits)

    fruits.remove('banana')
    print("After removing 'banana:", fruits)

    fruits.pop()
    print("After popping last element:", fruits)

    fruits.sort()
    print("After sort:", fruits)

    fruits.reverse()
    print("After reverse:", fruits)
    print("Index of 'mango':", fruits.index('mango'))
    print("Count of 'apple':", fruits.count('apple'))

if __name__ == "__main__":
    main()
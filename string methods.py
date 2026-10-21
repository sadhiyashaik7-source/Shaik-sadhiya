def main():
    text = "Hello World"
    print("Original text:", text)
    print("Lowercase:", text)
    print("Uppercase:", text)
    print("Replace 'Wrold' with 'Python':", text.replace('World', 'python'))
    print("Find 'World';", text.find('World'))
    print("Split;", text.split())
    print("Starts with 'H'?", text.startswith('H'))
    print("Ends with 'd'?", text.endswith('d'))

if __name__ == "__main__":
    main()
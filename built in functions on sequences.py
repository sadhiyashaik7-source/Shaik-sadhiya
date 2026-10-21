def main():
    names = ['Alice', 'Bob', 'Charlie']
    scores = [85,90,78]

    print("Using enumerator:")
    for i, name in enumerate(names):
        print(f"{i}: {names}")

    print("\nUsing zip:")
    for name, score in zip(names, scores):
        print(f"{names} scored {score}")

    print("\n Reversed names:", list(reversed(names)))
    print("Sorted scores:", sorted(scores))
            
main()
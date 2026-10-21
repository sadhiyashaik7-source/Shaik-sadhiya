def main():
    seq = [10,20,30,40,50]
    print("Original sequence:", seq)
    print("First element:", seq[0])
    print("Last element:", seq[-1])
    print("Sliced (1:4):", seq[1:4])
    print("Is 30 in sequence?", len(seq))
    print("Length of sequence:", len(seq))
    print("Max value:", max(seq))
    print("Min value:", min(seq))

if __name__ == "__main__":
    main()
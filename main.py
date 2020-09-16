from OddOrEven.prover import Parser, ProveEven, ProveOdd

if __name__ == "__main__":
    p = Parser()
    p.set_function("f(x)=x^3-x*3")  # This part is a little finicky, you have to specify -x rather than -3x,
    # and multiply x after you assign negative. This is probably because of how the parsing is set up.
    # Also doesn't support composite functions (Unless you substitute variables for 1 and calculate it yourself)

    p.parse()

    e = ProveEven(p.parsed_function)  # Prove it is even
    o = ProveOdd(p.parsed_function)  # Prove it is odd
    isEven, e1, e2 = e.prove()
    isOdd, o1, o2 = o.prove()
    print("All variables have been substituted for 1")
    print(f"Is it even: {isEven}\nEven value 1: {e1}\nEven value 2: {e2}\n\nIs it odd: {isOdd}\nOdd value 1: {o1}\nOdd value2: {o2}\n\nIs it neither: {isEven == isOdd}")  # Let the user know :)

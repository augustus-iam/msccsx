def main():
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    str_in = input("Enter message, like HELLO(exit to quit): ")
    if str_in == "exit":
        print("Bye.")
        return
    n = len(str_in)
    str_out = ""

    for i in range(n):
        c = str_in[i]
        loc = alpha.find(c)
        print(i, c, loc, )
        newloc = loc + 3
        str_out += alpha[newloc]
        print(newloc, str_out)
    print("Obfuscated version:", str_out)
    main()


if __name__ == '__main__':
    main()

def main():
    def judge(s):
        for o in O:
            # o‚Ís‚ÉŠmŽÀ‚ÉŠÜ‚Ü‚ê‚Ä‚¢‚Ü‚·
            if o not in s:
                return False
        for x in X:
            # x‚Ís‚ÉŠmŽÀ‚ÉŠÜ‚Ü‚ê‚Ä‚¢‚Ü‚¹‚ñ
            if x in s:
                return False
        return True

    S = input()
    O = []
    X = []

    for i, char in enumerate(S):
        if char == "o":
            O.append(str(i))
        elif char == "x":
            X.append(str(i))

    ans = 0

    for i in range(10000):
        s = str(i).zfill(4)
        if judge(s):
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()

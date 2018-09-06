class RandomStuff:
    def toLowerCase(self, str):
        toLowerCaseFunc = lambda x: chr(ord(x) + ord('a') - ord('A')) if ord('A') < ord(x) < ord('Z') else x
        return ''.join(list(map(toLowerCaseFunc, str)))

if __name__ == "__main__":
    rs = RandomStuff()
    print(rs.toLowerCase("TianTainNOodle"))

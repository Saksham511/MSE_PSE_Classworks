class FileRead:

    def readwhole(self):
        with open("demo_file.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                print(line[0:-1])
        f.close()

    def countchar(self):
        with open("demo_file.txt","r",encoding="utf-8") as f:
            count = 0
            for line in f:
                for ch in line:
                    if ch=="*":
                        count += 1
        return count

def main():
    obj1 = FileRead()
    obj1.readwhole()
    c=obj1.countchar()
    print("The number of * character is",c)

if __name__=="__main__":
    main()
for _ in range(int(input())):

        string = input()

        vowels, length = 0, len(string)

        for i in range(length):

            vowels+=(length-i)*(i+1) if string[i].lower() in 'aeiou' else 0

        print(vowels)

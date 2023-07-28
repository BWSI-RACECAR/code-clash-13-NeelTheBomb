class Solution:
    def stonks(self, prices):
            #type prices: list of int
            #return type: int
            least = 0
            least1 = 0
            save = 0
            save1=0
            resultlist = []
            #TODO: Write code below to returnn an int with the solution to the prompt.
            count = 0
            for i in range(len(prices)):
                for b in range(len(prices)):
                    for c in range(len(prices)):
                        least = 0
                        save = b-i
                        save1 = c-b
                        resultlist.append(save+save1)
            greatest = 0
            print(resultlist)
            for i in range(len(resultlist)):
                if resultlist[i] > greatest:
                    print(resultlist[i])
                    greatest = resultlist[i]
            print(greatest)
            return greatest
                    

            pass

def main():
    array = input().split(" ")
    for x in range (0, len(array)):
        array[x] = int(array[x])

    tc1 = Solution()
    ans = tc1.stonks(array)
    print(ans)

if __name__ == "__main__":
    main()

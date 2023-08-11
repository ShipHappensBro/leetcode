class Solution_1:
    def reverseWords(self, s: str) -> str:
        s=s.strip()
        new_list=[]
        i=0
        new_list=s.split(' ')
        a=new_list.count('')
        while i<a:
            new_list.remove("")
            i+=1
        new_list.reverse()
        return " ".join(new_list)
run_1=Solution_1()
print(run_1.reverseWords("    a good          example   "))
# Время выполнения 83 мс, потребление памяти 16.5 мб


class Solution_main:
    def reverseWords(self, s: str) -> str:
        print(type(s.split()))
        return " ".join(reversed(s.split()))
run=Solution_main()
print(run.reverseWords("    a good          example   "))
# Время выполнения 32 мс, потребление памяти 16.3 мб
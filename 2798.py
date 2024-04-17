class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        counter = 0
        for i in range(len(hours)):
            if hours[i] >= target:
                counter +=1
        return counter

def main():
    solution = Solution()
    hours = [0,1,2,3,4]
    target = 2
    print(solution.numberOfEmployeesWhoMetTarget(hours,target))


main()
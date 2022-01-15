def Rotatearr(nums, k, n):
    count = 0
    i = 0
    val = nums[0]
    rep = 0
    while (count<len(nums)):
        position = (i+k)%n
        temp = nums[position]
        nums[position] = val
        i = position

        if (position == rep):
            rep = (i+k)%n
            val = nums[rep]
            i = rep
            count = count+1
            continue

        val = temp
        count+=1
    return nums




if __name__ == '__main__':
    nums = [1,2,3,4,5]
    print(Rotatearr(nums,1,len(nums)))


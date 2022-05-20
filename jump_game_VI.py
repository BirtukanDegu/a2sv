max_index = 0
        for n in range(1, len(nums)):
            start = max((n - k) , 0)
            if max_index < start:
                max_index = start
                for i in range(start + 1, n):
                    if nums[i] >= nums[max_index]:
                        max_index = i
            nums[n] = nums[n] + nums[max_index]
            if nums[n] >= nums[max_index]:
                max_index = n
        return nums[-1]


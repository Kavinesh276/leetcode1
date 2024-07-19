def two_sum(nums, target):
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i
    return None  
nums_input = input("Enter the list of numbers separated by spaces: ")

if isinstance(nums_input, str):
    nums = list(map(int, nums_input.split())) 
else:
    print("Error: Input is not a string.")
    nums = []

target_input = input("Enter the target number: ")

if isinstance(target_input, str):
    try:
        target = int(target_input)
    except ValueError:
        print("Error: Target input is not a valid integer.")
        target = None
else:
    print("Error: Target input is not a string.")
    target = None

if nums and target is not None:
    result = two_sum(nums, target)

    if result:
        print("The indices of the two numbers that add up to {} are: {}".format(target, result))
    else:
        print("No solution found.")
else:
    print("Invalid input.")

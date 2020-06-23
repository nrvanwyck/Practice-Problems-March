def partitionArray(k, numbers):
    if len(numbers) % k != 0:
        return "No"
    count_dict = {number: numbers.count(number) for number in set(numbers)}
    if max(count_dict.values()) > (len(numbers) / k):
        return "No"
    return "Yes"

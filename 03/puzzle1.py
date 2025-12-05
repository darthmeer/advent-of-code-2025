"""

The batteries are each labeled with their joltage rating, a value from 1 to 9.

Each line in input is a bank of batteries. 

Within each bank, you need to turn on exactly two batteries; the joltage that the bank produces is equal to the number formed by the digits on the batteries you've turned on.

If you have a bank 12345 and you turn on batteries 2 and 4, the bank would produce 24 jolts. (You cannot rearrange batteries.)

Find the largest possible joltage each bank can produce.

The total output joltage is the sum of the maximum joltage from each bank.

"""

def main():

    total_joltage = 0

    with open("input") as f:
        for line in f:
            # get all batteries with their positions
            batteries = [(int(battery), i) for i, battery in enumerate(line.strip())]
            
            # sort by battery value (descending), then by position (ascending)
            batteries.sort(key=lambda x: (-x[0], x[1]))
            
            # find the two highest batteries that maintain order
            first = batteries[0]
            second = None
            for battery in batteries[1:]:
                if battery[1] > first[1]:
                    second = battery
                    break
            
            # if no second found, try finding first before second
            if second is None:
                for battery in batteries[1:]:
                    if battery[1] < first[1]:
                        second = first
                        first = battery
                        break
            
            # get joltage maintaining position order
            if first[1] < second[1]:
                bank_joltage = first[0] * 10 + second[0]
            else:
                bank_joltage = second[0] * 10 + first[0]

            print(f"bank line: '{line.strip()}' bank joltage: {bank_joltage}")
            total_joltage += bank_joltage

    print(f"total joltage = {total_joltage}")

if __name__ == "__main__":
    main()

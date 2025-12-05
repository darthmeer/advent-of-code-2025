"""
Input has a list fo product ID ranges in a single line.

The ranges are separated by commas (,); each range gives its first ID and last ID separated by a dash (-).

Invalid IDs are any ID which are made only of some sequence of digits repeated twice. So, 55 (5 twice), 6464 (64 twice), and 123123 (123 twice) would all be invalid IDs.

Find all of the invalid IDs that appear in the given ranges.

Add up all invalid IDs found in the ranges and output that sum.
"""

def main():

    invalid_id_sum = 0

    with open("input") as f:
        line = f.readline().strip()
        ranges = line.split(",")

        for r in ranges:
            start_r, end_r = r.split("-")

            for id in range(int(start_r), int(end_r) + 1):
                id_str = str(id)
                length = len(id_str)

                if length % 2 == 0:
                    half = length // 2
                    if id_str[:half] == id_str[half:]:
                        invalid_id_sum += id

    print(f"sum of invalid IDs = {invalid_id_sum}")

if __name__ == "__main__":
    main()

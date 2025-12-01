"""
Dial starts at 50.

The safe has a dial with numbers 0 through 99 in order. 

The input file contains a sequence of rotations, one per line, which tell you how to open the safe.

A rotation starts with an L or R which indicates whether the rotation should be to the left (toward lower numbers) or to the right (toward higher numbers). Then, the rotation has a distance value which indicates how many clicks the dial should be rotated in that direction.

Because the dial is a circle, turning the dial left from 0 makes it point at 99. Turning the dial right from 99 makes it point at 0.

What is the number of times the dial is left pointing at 0 after any rotation in the sequence.
"""

def main():
    position = 50
    zero_count = 0

    with open("input") as f:
        for line in f:
            direction = line[0]
            distance = int(line[1:])

            if direction == 'L':
                position = (position - distance) % 100
            elif direction == 'R':
                position = (position + distance) % 100

            if position == 0:
                zero_count += 1

    print(f"pointed at 0 = {zero_count}")

if __name__ == "__main__":
    main()

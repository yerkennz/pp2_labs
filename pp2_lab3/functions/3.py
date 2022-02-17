def solve(numheads, numlegs):
    print("Number of rabbits", (numlegs-2*numheads)//2)
    print("Number of chickens", numheads - (numlegs-2*numheads)//2)

print("Enter number  of heads and legs:")
numh, numl = int(input()), int(input())
solve(numh, numl)
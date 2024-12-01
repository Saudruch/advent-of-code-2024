input = open("/home/user/Documents/Python/advent-of-code-2024/day1/input.txt", "r")
left_column = []
right_column = []
distance = []

for line in input:
    left_column.append(int(line.split()[0]))
    right_column.append(int(line.split()[1]))

left_column.sort()
right_column.sort()

for i in range(len(left_column)):
    distance.append(abs((right_column[i]-left_column[i])))

total_distance = sum(distance)
print(f"Total distance is {total_distance}")

left_column_set = set(left_column)
similarity_score = 0

for number in left_column_set:
    count = right_column.count(number)
    similarity_score +=  number * count

print(f"Similarity score is {similarity_score}")
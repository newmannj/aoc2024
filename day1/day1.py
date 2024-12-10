left = []
right = []

with open("lists.txt", "r") as file:
    for line in file:
        split = line.split()
        left.append(int(split[0]))
        right.append(int(split[1]))

left.sort()
right.sort()

# Part 1: Get the distances
i = 0
distances = []
while(i < len(left) and i < len(right)):
    left_location = left[i]
    right_location = right[i]
    distance = abs(left_location - right_location)
    distances.append(distance)
    i += 1

print(sum(distances))
# Part 2: Get the similarity score
scores = {}
total_similarity_score = 0
right_i = 0
for left_location in left:
    if left_location in scores:
        total_similarity_score += scores[left_location]
    else:
        similarity_score = 0
        while(right_i < len(right)):
            right_location = right[right_i]
            # If the right side is greater than the left, we know we have a similarity score of 0
            if right_location > left_location:
                break
            elif right_location == left_location:
                similarity_score += left_location
                right_i += 1
            elif right_location < left_location:
                right_i += 1
                continue
            else:
                break    
        scores[left_location] = similarity_score
        total_similarity_score += similarity_score

print(total_similarity_score)

import random

def main(fruits):
    
    # Cumulative probability
    cumulative_prob = generate_cumulative_probability(fruits)
    print(cumulative_prob)

    # Generate random variable
    rand_val = generate_rand(cumulative_prob)
    print(rand_val)

    # Find the first smallest element to the generated value
    index = find_first_smallest(cumulative_prob, rand_val, 0, len(cumulative_prob)-1, 0)
    print(cumulative_prob[index])

    # return the element at the index
    return fruits[index][0]


def generate_cumulative_probability(fruits):
    cumulative = [0]
    for x in range(0, len(fruits)):
        val = cumulative[x] + fruits[x][1]
        cumulative.append(val)
    return cumulative

def generate_rand(cumulative):
    rand_val = random.randint(0, cumulative[-1])
    return rand_val

def find_first_smallest(cumulative_prob, rand_val, start, end, result):
    if start > end:
        return result
    mid = start + (end - start) // 2
    if rand_val < cumulative_prob[mid]:
        return find_first_smallest(cumulative_prob, rand_val, 0, mid - 1, result)
    elif rand_val > cumulative_prob[mid]:
        result = mid
        return find_first_smallest(cumulative_prob, rand_val, mid+1, end, result)
    else:
        result = mid
        return result

if __name__ == '__main__':
    fruits = [("Apple", 10), ("Orange", 7), ("Pear", 12), ("Guava", 13)]
    x = main(fruits)
    print(x)
def reverse(data):
    for index in range(len(data)-1, -1, -1):
            yield data[index]

if __name__ == "__main__":
    ret = reverse([x for x in range(10)])
    print([x for x in ret])

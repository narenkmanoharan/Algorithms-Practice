def dnf(A, index):
    small, equal, pivot, large = 0, 0, A[index], len(A) - 1
    while equal <= large:
        if A[equal] < pivot:
            A[small], A[equal] = A[equal], A[small]
            small += 1
            equal += 1
        elif A[equal] == pivot:
            equal += 1
        elif A[equal] > pivot:
            A[equal], A[large] = A[large], A[equal]
            large -= 1
    return A

if __name__ == '__main__':
    print(dnf([0,5,8,3,3], 3))
    print(dnf([0,5,8,23,23,2,2,3,5,1,7,3,3], 7))

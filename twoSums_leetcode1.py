def twoSums(nums: List[int], target: int) -> List[int]:

    # in python {key: value} pairs are stored as dictionary/hash table
    # (a hash function is applied to the key for easy access).
    # type({'k': 'v'}) will give 'dict'
    # type(dict(k: 'v')) will give 'dict'
    #
    # both ways can be used to create hash table
    # people = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
    # people['Age'] will give '7'
    # people['id'] = '01a' will add the new key, value pair


    # ENUMERATE
    # arr = ['abdi', 'shah', 'henry', 'adith']
    # for index, value in arr:
    #     print index, ': ', value, '\n'
    #
    # ######  OUTPUT
    # ######  0: abdi
    # ######  1: shah
    # ######  2: henry
    # ######  3: adith

    dictionary = {}
    for ind, num in enumerate(nums):
        compliment = target - num
        if(compliment in dictionary):
            return ind, dictionary[compliment]
        dictionary[num] = ind

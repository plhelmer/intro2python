def name_generator(person1 : str, person2: str):
    ###PUT YOUR CODE BELOW THIS LINE VVVVVVVV
    vowel = ['a', 'A', 'e', 'E', 'e', 'o', 'O', 'u', 'U', 'y', 'Y']
    marker1 = []
    for n in range (len(person1)-1):
        if person1[n-1] == 's' and person1[n] == 'h' and person1[n-2] in vowel:
            marker1 += [n]
        elif person1[n-1] in vowel and person1[n] not in vowel and person1[n-1] != 's' and person1[n] != 'h':
            marker1 += [n-1]
    marker1 = [i for i in marker1 if i != 0]
    sybF1 = person1[0:marker1[0]+1]
    sybL1 = person1[marker1[-1] + 1:len(person1)]

    marker2 = []
    for m in range (len(person2)-1):
        if person2[m-1] == 's' and person2[m] == 'h' and person2[m-2] in vowel:
            marker2 += [m]
        elif person2[m-1] in vowel and person2[m] not in vowel and person2[m-1] != 's' and person2[m] != 'h':
            marker2 += [m-1]
    marker2 = [i for i in marker2 if i != 0]
    sybF2 = person2[0:marker2[0]+1]
    sybL2 = person2[marker2[-1]+1:len(person2)]

    if sybF1 + sybL2 == person1 or sybF1 + sybL2 == person2:
        couple_name = [sybF1 + sybF2]
    else: couple_name = [sybF1 + sybL2]
    print(couple_name)
    ###PUT YOUR CODE ABOVE THIS LINE ^^^^^^^^
    return couple_name
name_generator(person1='Alice',person2='Sharon')
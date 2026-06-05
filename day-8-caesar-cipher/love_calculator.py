def calculate_love_score(name1, name2):
    s1 = 0
    s2 = 0
    names = name1 + name2
    for a in names:
        match(a):
            case 'T': s1+=1
            case 't': s1+=1
            case 'R': s1+=1
            case 'r': s1+=1
            case 'U': s1+=1
            case 'u': s1+=1
            case 'E': s1+=1
            case 'e': s1+=1
            
    for a in names:
        match(a):
            case 'L': s2+=1
            case 'l': s2+=1
            case 'O': s2+=1
            case 'o': s2+=1
            case 'V': s2+=1
            case 'v': s2+=1
            case 'E': s2+=1
            case 'e': s2+=1
            
    print(str(s1)+str(s2))

calculate_love_score( "Angela Yu", "Jack Bauer")
#python L1_Challenge4_Task1and2.py

#TASK 1 - CodeWars
"""The Office I - Outed"""

def outed(meet, boss):
    total_score = 0
    for k, v in meet.items():
        if k == boss:
            total_score += v*2
        else:
            total_score += v
    overall_happiness = total_score / len(meet)
    if overall_happiness <= 5:
        return 'Get Out Now!'
    else:
        return 'Nice Work Champ!'

#print (outed({'tim':0, 'jim':2, 'randy':0, 'sandy':7, 'andy':0, 'katie':5, 'laura':1, 'saajid':2, 'alex':3, 'john':2, 'mr':0}, 'laura'))
#print (outed({'tim':1, 'jim':3, 'randy':9, 'sandy':6, 'andy':7, 'katie':6, 'laura':9, 'saajid':9, 'alex':9, 'john':9, 'mr':8}, 'katie'))
#print (outed({'tim':2, 'jim':4, 'randy':0, 'sandy':5, 'andy':8, 'katie':6, 'laura':2, 'saajid':2, 'alex':3, 'john':2, 'mr':8}, 'john'))


"""The Office II - Boredom Score"""

scores = {"accounts": 1, "finance": 2, "canteen": 10, "regulation": 3, "trading": 6, "change": 6, "IS": 8, "retail": 5, "cleaning": 4, "pissing about": 25}
## k, v in staff
## l, b in scores
def boredom(staff):
    score = 0
    for k, v in staff.items():
        for l, b in scores.items():
            if v == l:
                score += b
    if score <=80:
        return "kill me now"
    elif 80 < score < 100:
        return "i can handle this"
    elif score >= 100:
        return "party time!!"

#print (boredom({"tim": "change", "jim": "accounts",
      #"randy": "canteen", "sandy": "change", "andy": #"change", "katie": "IS",
      #"laura": "change", "saajid": "IS", "alex": #"trading", "john": "accounts",
      #"mr": "finance" }))
#print (boredom({ "tim": "IS", "jim": "finance",
      #"randy": "pissing about", "sandy": "cleaning", #"andy": "cleaning",
      #"katie": "cleaning", "laura": "pissing about", #"saajid": "regulation",
      #"alex": "regulation", "john": "accounts", "mr": #"canteen" }))
#print (boredom({ "tim": "accounts", "jim": "accounts",
      #"randy": "pissing about", "sandy": "finance", #"andy": "change",
      #"katie": "IS", "laura": "IS", "saajid": "canteen", #"alex": "pissing about",
      #"john": "retail", "mr": "pissing about" }))




#TASK 2 - Leetcode(optional)

"""Challenge 1: Top K Frequent Words"""
def topKFrequent(words, k):
    word_counter = {}
    for word in words:
        if word not in word_counter:
            word_counter[word] = 1
        else:
            word_counter[word] += 1

    dict_ordered_value = sorted(word_counter.items(), key=lambda items: (-items[1], items[0]))
    return dict_ordered_value[:k]

#print(topKFrequent(["the","day","is","sunny","the","the","the","sunny","is","is"], 2))


"""Challenge 2: Decode the Message"""
def decodeMessage(key, message):
    def list_keys():
        stripped_keys = list(key.replace(" ", ""))
        list_keys = []
        for char in stripped_keys:
            if char not in list_keys:
                list_keys.append(char)
        list_keys = list_keys[:26]
        return list_keys
    list_keys = list_keys()

    def list_letters():
        import string
        list_letters = list(string.ascii_lowercase)
        return list_letters
    list_letters = list_letters()

    code_dict = dict(zip(list_keys, list_letters))

    for k, v in code_dict.items():
        message = message.replace(k, v)

    return ("Code Keys: {} \nCode Values: {} \nCode Dictionary: {} \nDecoded Message: {}".format(list_keys, list_letters, code_dict, message))



#print(decodeMessage("the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv"))
                                                                   #this is v sezret


"""Challenge 3: Roman to Integer"""
symbol = ["I", "V", "X", "L", "C", "D", "M"]
value = [1, 5, 10, 50, 100, 500, 1000]
roman_dict = dict(zip(symbol, value))

def romanToInt(s):
    s = s.replace("IV", "IIII")
    s = s.replace("IX", "VIIII")
    s = s.replace("XL", "XXXX")
    s = s.replace("XC", "LXXXX")
    s = s.replace("CD", "CCCC")
    s = s.replace("CM", "DCCCC")
    s = list(s)

    integer_s = [roman_dict[k] for k in s if k in roman_dict]

    def add_values():
        total = 0
        for i in integer_s:
            total += i
        return total
    return (add_values())

#print(romanToInt("III")) --> 3
#print(romanToInt("LVIII")) --> 58
#print(romanToInt("MCMXCIV")) --> 1994

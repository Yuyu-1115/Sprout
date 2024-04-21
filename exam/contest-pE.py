n = int(input())
choice = dict()

for i in range(n):
    rule = input()
    if "<" in rule:
        rule = rule.split(sep = "<")
        if rule[0] not in choice:
            choice[rule[0]] = [rule[1]]
        else:
            choice[rule[0]].append(rule[1])
    else:
        rule = rule.split(sep = ">")
        if rule[1] not in choice:
            choice[rule[1]] = [rule[0]]
        else:
            choice[rule[1]].append(rule[0])

m = int(input())

for i in range(m):
    combo = input().split(sep = ",")
    if len(combo) == 1:
        punch = combo[0]
        if punch in choice:
            output = str(len(choice[punch])) + ":"
            print(output + ",".join(sorted(choice[punch])))
        else:
            print(-1)
    else:
        for punch in combo:
            if punch not in choice:
                combo.remove(punch)
        if len(combo) == 0:
            print(-1)
            continue
        output_list = sorted(choice[combo[0]])
        for punch in combo:
            for one in output_list:
                if not one in choice[punch]:
                    output_list.remove(one)

        output = str(len(output_list)) + ":"
        print(output + ",".join(sorted(output_list)))


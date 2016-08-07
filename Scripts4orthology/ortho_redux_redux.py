
import sys
from collections import Counter

f = open(sys.argv[1], "r")
groups = sys.argv[2:]

one_to_one = []
ortho_plus_paralog = []
one_to_one_notallspecies = []
ortho_plus_paralog_notallspecies = []
group_single = {}
group_paralog = {}

for group in groups:
    group_single[group] = []
    group_paralog[group] = []


for line in f:
    is_one_to_one = True
    is_ortho_plus_paralog = True
    for group in groups:
        if group not in line:
            is_one_to_one = False
            is_ortho_plus_paralog = False
            break

        if line.count(group) > 1:
            is_one_to_one = False

    if is_one_to_one:
        one_to_one.append(line)
    elif is_ortho_plus_paralog:
        ortho_plus_paralog.append(line)
    else:
        valid_group = True
        cur_group = None
        group_count = 0
        for group in groups:
            line_count = line.count(group)
            if line_count == 0:
                continue

            if cur_group is not None:
                valid_group = False
                break

            cur_group = group
            group_count = line_count


        if valid_group and cur_group is not None:
            if line.count(cur_group) == 1:
                group_single[cur_group].append(line)
            else:
                group_paralog[cur_group].append(line)
        else:
            other_one_to_one = True
            for group in groups:
                if line.count(group) > 1:
                    other_one_to_one = False
                    break

            if other_one_to_one:
                one_to_one_notallspecies.append(line)
            else:
                ortho_plus_paralog_notallspecies.append(line)



one_to_one_out = open("one_to_one.txt", "w")
ortho_plus_paralog_out = open("ortho_plus_paralog.txt", "w")
one_to_one_notallspecies_out = open("one_to_one_notallspecies.txt", "w")
ortho_plus_paralog_notallspecies_out = open("ortho_plus_paralog_notallspecies.txt", "w")
single_copy_out = open("single_copy.txt", "w")
paralog_out = open("paralogs.txt", "w")


for line in one_to_one:
    one_to_one_out.write(line)

for line in one_to_one_notallspecies:
    one_to_one_notallspecies_out.write(line)

for line in ortho_plus_paralog:
    ortho_plus_paralog_out.write(line)

for line in ortho_plus_paralog_notallspecies:
    ortho_plus_paralog_notallspecies_out.write(line)




for key in group_single:
    single_copy_out.write("\n{} single copy\n\n".format(key))
    for line in group_single[key]:
        single_copy_out.write(line)

for key in group_paralog:
    paralog_out.write("\n{} paralog\n\n".format(key))
    for line in group_paralog[key]:
        paralog_out.write(line)


paralog_out.close()
single_copy_out.close()
one_to_one_out.close()
one_to_one_notallspecies_out.close()
ortho_plus_paralog_out.close()
ortho_plus_paralog_notallspecies_out.close()
#
# for key in group_paralog:
#     print("\n{} paralog\n".format(key))
#     for line in group_paralog[key]:
#         print(line.rstrip())

# print("One to One\n\n")
# for line in one_to_one:
#     print(line)
# for line in ortho_plus_paralog:
#     print(line)

# print("One to One\n\n")
# for line in one_to_one_notallspecies:
#     print(line)
# for line in ortho_plus_paralog_notallspecies:
#     print(line)

# print(Counter(map(lambda w: "/".join([group for group in groups if group in w]),
#                   f)))

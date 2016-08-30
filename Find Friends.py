def check_connection(robots, name1, name2):
    x = 0
    i = 0
    robot1 = set()
    robot2 = set()
    temp_robots = []
    names = [[name1], [name2]]
    for q in range(0, len(names)):
        for a in range(0, len(robots)):
            temp_robots.append(robots[a])
        while x < len(temp_robots) and i < (2*len(robots)):
            for a in range(0,len(temp_robots)):
                j = temp_robots[a].split('-')
                if j[0] in names[q] or j[1] in names[q]:
                    names[q].append(j[0])
                    names[q].append(j[1])
                    temp_robots[a] = '-'
                    x = temp_robots.count('-')
            i += 1
        if q == 0:
            for r1 in range(0, len(names[q])):
                robot1.add(names[q][r1])
        else:
            for r1 in range(0, len(names[q])):
                robot2.add(names[q][r1])
    if robot1 & robot2:
        return True
    else:
        return False

# print(check_connection(("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
#      "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
#     "scout2", "scout3"))

# print(check_connection(("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
#      "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
#     "dr101", "sscout"))

# print(check_connection(
#         ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
#          "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
#         "super", "scout2"))

print(check_connection(
    ("nikola-robin","batman-nwing","mr99-batman","mr99-robin","dr101-out00","out00-nwing",)
                       ,"dr101","mr99"))

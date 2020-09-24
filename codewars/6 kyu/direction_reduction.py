opposite = {'NORTH': 'SOUTH', 'EAST': 'WEST', 'SOUTH': 'NORTH', 'WEST': 'EAST'}

def dirReduc(plan):
    new_plan = []
    for i in plan:
        if new_plan and new_plan[-1] == opposite[i]:
            new_plan.pop()
            print (new_plan)
        else:
            new_plan.append(i)
            print (new_plan)
    return new_plan

print (dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))

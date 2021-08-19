lst = ["naseef", "gregary", "safaf", 2, 4, 7, 323]
val = 4
pos = lst.index(val)+1
if(val in lst):
    print("value", val, "found at", pos, "th position")
else:
    print(val, "not found")

lst = ["naseef", "gregary", "safaf", "niya", "shad", "kak", "ab", "jaykara"]
ctr = 0
for name in lst:
    if (len(name) > 5):
        ctr += 1
if(ctr > 0):
    print("%d persons name are having more than 5 characters in name" % ctr)
else:
    print("The name length of all persons are less than 5.")

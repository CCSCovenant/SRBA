
def get_relic_effects(RIDs):
    counter = {}

    for RID in RIDs:
        if RID in counter:
            counter[RID] = counter[RID] + 1
        else:
            counter[RID] = 1

    for RID in counter:
        if counter[RID] >= 2:
            # TODO 应用两件套效果
            pass
        if counter[RID] >= 4:
            # TODO 应用四件套效果
            pass

    pass
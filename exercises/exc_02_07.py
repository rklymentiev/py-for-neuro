ids = [
    'id1', 'id2', 'id3', 'id4', 'id5',
    'id6', 'id7', 'id8', 'id9', 'id10'
    ]
groups = [
    'ContrOl_1', 'ContrOl_1', 'TreatMent_2', 'ContrOl_1', 'TreatMent_2',
    'TreatMent_2', 'TreatMent_2', 'TreatMent_2', 'ContrOl_1', 'ContrOl_1'
    ]

groups_cleaned = list(map(___, groups))

ids_ctl = ___             # initialize empty list with control group IDs
ids_trt = ___             # initialize empty list with treatment group IDs
for i in ___:             # iterate over indeces of the list
    if ___ == 'control':  # if the i-th elemnt in a cleaned groups list is control
        ids_ctl.___       # then add i-th ID to the control group
    else:
        ids_trt.___       # otherwise add i-th ID to the treatment group

print(f"Control Group: {ids_ctl}")
print(f"Treatment Group: {ids_trt}")

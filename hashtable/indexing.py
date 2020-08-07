# you have a bunch of records
# return all IOS students

records = [
    ('Scott', 'IOS'),
    ('Nick', 'IOS'),
    ('Ryan', 'DS'),
    ('Chris', 'DS'),
    ('Damon', 'WEB'),
    ('Michael', 'WEB')
    ]

#let's make an index for instant access by some attribute or other
## some attribute we search by often

#key: attribute - track 
#value: list of names

def build_index(records):
    indexed_records = {}

    for index, record in enumerate(records): #tupel of index and item
        track = record[1]
        name = record[0]

        if track in indexed_records:
            indexed_records[track].append(name)
        else:
            indexed_records[track] = [name]
    return indexed_records

indexed_records = build_index(records)
print(indexed_records['IOS'])


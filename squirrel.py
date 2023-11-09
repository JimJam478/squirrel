import json

def load_json():
    f = open('journal.json')
    journal = json.load(f)
    journal_list = list(journal)
    f.close()
    return journal_list


    
import json
import math

def load_json():
    f = open('journal.json')
    journal = json.load(f)
    journal_list = list(journal)
    f.close()
    return journal_list

def compute_phi(file,event):
    n_11,n_00,n_10,n_01 = 0  
    n_1p,n_0p,n_p1,n_p0 = 0 
    for i in file:
        if event in i['events'] and i['squirrel']:
            n_11 += 1
        if event not in i['events'] and not i['squirrel']:
            n_00 += 1
        if event in i['events'] and not i['squirrel']:
            n_10 += 1
        if event not in i['events'] and i['squirrel']:
            n_01 += 1
        if event in i['events']:
            n_1p += 1
        if event not in i['events']:
            n_0p += 1
        if i['squirrel']:
            n_p1 += 1
        if not i['squirrel']:
            n_p0 += 1
    phi = (n_11 * n_00 - n_10 * n_01) / math.sqrt((n_1p * n_0p * n_p1 * n_p0))
    return phi

def compute_correlations(file):
    data = load_json()
    correlation_dict = {}
    for i in data:
        for event in i['events']:
            phi = compute_phi(data,event)
            correlation_dict[event] = phi
    return correlation_dict



    
    
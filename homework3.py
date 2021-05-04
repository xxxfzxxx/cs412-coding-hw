
def get_db(file):
    def split(line):
        return [char for char in line]
    f = open(file, 'r')
    f_line = f.readlines()
    db = []
    for i in f_line:
        line_arr = split(i)
        start = line_arr.index('<') + 1
        end = line_arr.index('>')
        line_arr = line_arr[start: end]
        line = ''.join(line_arr)
        print(line)
        db.append(line)
    return db

def is_frequent(patt, db, minsup):
    cnt = 0
    for line in db:
        if patt in line:
            cnt += 1
    if cnt < minsup:
        return False
    else:
        return True

def generate_next(patt, db):
    next_patt = []
    for line in db:
        start_pos = [n for n in range(len(line)) if line.find(patt, n) == n]
        end_pos = []
        for i in start_pos:
            i += len(patt)+1
            end_pos.append(i)
        if len(start_pos) != 0:
            for i in range(len(start_pos)):
                next_patt.append(line[start_pos[i]:end_pos[i]])
    for item in next_patt:
        if len(item) == len(patt):
            next_patt.remove(item)
    next_patt = list(set(next_patt))
     
    return next_patt
def get_patt_cnt(patt, db):
    cnt = 0
    for line in db:
        if patt in line:
            cnt+=1
    return cnt

def get_sequences(file, minsup):
    db = get_db(file)
    F1 = {}
    freq_item_list = []
    for line in db:
        for i in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
            F1[i] = 0
    for line in db:
        for i in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
            if i in line:
                F1[i] = F1[i]+1
    
    for a in F1:
        if is_frequent(a, db, minsup):
            freq_item_list.append(a)
            next_patts1 = generate_next(a, db)
            for b in next_patts1:
                if is_frequent(b, db, minsup):
                    freq_item_list.append(b)
                    next_patts2 = generate_next(b, db)
                    for c in next_patts2:
                        if is_frequent(c, db, minsup):
                            freq_item_list.append(c)
                            next_patts3 = generate_next(c, db)
                            for d in next_patts3:
                                if is_frequent(d, db, minsup):
                                    freq_item_list.append(d)
                                    next_patts4 = generate_next(d, db)
                                    for e in next_patts4:
                                        if is_frequent(e, db, minsup):
                                            freq_item_list.append(e)
                                            next_patts5 = generate_next(e, db)
                                            for f in next_patts5:
                                                if is_frequent(f, db, minsup):
                                                    freq_item_list.append(f)
                                                    next_patts6 = generate_next(f, db)
                                                    for g in next_patts6:
                                                        if is_frequent(g, db, minsup):
                                                            freq_item_list.append(g)
                                                            next_patts7 = generate_next(g, db)
                                                            for h in next_patts7:
                                                                if is_frequent(h, db, minsup):
                                                                    freq_item_list.append(h)
                                                                    next_patts8 = generate_next(h,db)
                                                                    for i in next_patts8:
                                                                        if is_frequent(i, db, minsup):
                                                                            freq_item_list.append(i)
                                                                            next_patts9 = generate_next(i,db)
                                                                            for j in next_patts9:
                                                                                if is_frequent(j, db, minsup):
                                                                                    freq_item_list.append(j)
                                                                                    next_patts10 = generate_next(j,db)
                                                                                    for k in next_patts10:
                                                                                        if is_frequent(k, db, minsup):
                                                                                            freq_item_list.append(k)
                                                                                            next_patts11 = generate_next(k,db)
                                                                                            for l in next_patts11:
                                                                                                if is_frequent(l, db, minsup):
                                                                                                    freq_item_list.append(l)
                                                                                                    next_patts12 = generate_next(l,db)
                                                                                                    for m in next_patts12:
                                                                                                        if is_frequent(m, db, minsup):
                                                                                                            freq_item_list.append(m)
                                                                                                            next_patts13 = generate_next(m,db)
                                    
    result = {}
    for item in freq_item_list:
        result[item] = get_patt_cnt(item, db)
    print(result)
    return result
get_sequences('validation.txt', 2)



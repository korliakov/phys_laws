def get_laws():
    laws = []
    with open("./data/laws.csv", "r", encoding="utf-8") as f:
        cnt = 1
        for line in f.readlines()[1:]:
            law, definition, formula, area, source = line.split(";")
            laws.append([cnt, law, definition, formula, area])
            cnt += 1
    return laws


def get_stats():
    db_terms = 0
    user_terms = 0
    areas = []
    area_freq = {}
    total_words = 0

    with open("./data/laws.csv", "r", encoding="utf-8") as f:
        for line in f.readlines()[1:]:
            law, definition, formula, area, source = line.split(";")
            areas.append(area)
            total_words += len(definition.split())
            if "user" in source:
                user_terms += 1
            elif "db" in source:
                db_terms += 1

    for ar in set(areas):
        area_freq[ar] = areas.count(ar)

    stats = {
        "terms_all": db_terms + user_terms,
        "terms_own": db_terms,
        "terms_added": user_terms,
        "area_freq": area_freq,
        "words_avg": round(total_words / (db_terms + user_terms), 1) if (db_terms + user_terms) > 0 else 0,
    }
    return stats
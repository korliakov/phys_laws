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


def write_law(new_law, new_definition, new_formula, new_area):
    new_law_line = f"{new_law};{new_definition};\[{new_formula}\];{new_area};user"
    with open("./data/laws.csv", "r", encoding="utf-8") as f:
        existing_laws = [l.strip("\n") for l in f.readlines()]
        title = existing_laws[0]
        old_laws = existing_laws[1:]
    laws_sorted = old_laws + [new_law_line]
    laws_sorted.sort()
    new_laws = [title] + laws_sorted
    with open("./data/laws.csv", "w", encoding="utf-8") as f:
        f.write("\n".join(new_laws))


def write_error(new_law, new_description, user_mail):
    new_law_line = f"{new_law};{new_description};{user_mail}"
    with open("./data/errors.csv", "r", encoding="utf-8") as f:
        existing_laws = [l.strip("\n") for l in f.readlines()]
        title = existing_laws[0]
        old_laws = existing_laws[1:]
    laws_sorted = old_laws + [new_law_line]
    laws_sorted.sort()
    new_laws = [title] + laws_sorted
    with open("./data/errors.csv", "w", encoding="utf-8") as f:
        f.write("\n".join(new_laws))
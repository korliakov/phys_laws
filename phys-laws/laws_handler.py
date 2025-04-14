def get_laws():
    laws = []
    with open("./data/laws.csv", "r", encoding="utf-8") as f:
        cnt = 1
        for line in f.readlines()[1:]:
            law, definition, formula, area, source = line.split(";")
            laws.append([cnt, law, definition, formula, area])
            # laws.append([cnt, law, definition, area])

            cnt += 1
        # print(law, definition, formula, area, source)
    return laws
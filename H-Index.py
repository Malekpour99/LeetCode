def hIndex(citations: list[int]) -> int:
    h_index = 0
    h_map = {}
    for i in range(len(citations)):
        if citations[i] not in h_map:
            h_map[citations[i]] = 0
            for j in range(len(citations)):
                if citations[j] >= citations[i]:
                    h_map[citations[i]] += 1

    for key, value in h_map.items():
        if key > h_index:
            if value >= key:
                h_index = key
            elif min(key, value) > h_index:
                h_index = min(key, value)

    return h_index


def hIndex(citations: list[int]) -> int:
        n = len(citations)
        citations.sort()

        for i,v in enumerate(citations):
            if n - i <= v:
                return n - i
        return 0

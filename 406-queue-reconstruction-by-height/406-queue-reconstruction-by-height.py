class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        ln = len(people)
        if ln == 0:
            return []

        people = sorted(people, key = lambda x: (-x[0], x[1]))

        final = []
        for pep in people:
            final.insert(pep[1], pep)

        return final
        
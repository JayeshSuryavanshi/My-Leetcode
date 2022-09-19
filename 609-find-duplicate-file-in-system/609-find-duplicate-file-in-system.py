class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
            _dict = collections.defaultdict(list)
            for line in paths:
                data = line.split()
                root = data[0]
                for file in data[1:]:
                    name, _, content = file.partition('(')
                    _dict[content[:-1]].append(root + '/' + name)

            return [x for x in _dict.values() if len(x) > 1]
        
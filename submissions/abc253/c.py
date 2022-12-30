from bisect import insort, bisect_left, bisect_right

__file = open(0)  # 入力の受け取りが重いので、高速なreadlineを使います
readline = __file.readline  # 400ms程度速くなります

class OrderedMultiList:
    class FenwickTree:
        def __init__(self, array):
            n = len(array)
            self.__container = [0] + array[:]
            self.__size = len(self.__container)
            self.__depth = n.bit_length()
            for i in range(n):
                j = i | (i + 1)
                if j < n:
                    self.__container[j + 1] += self.__container[i + 1]

        def add(self, i, x):
            i += 1
            while i < self.__size:
                self.__container[i] += x
                i += i & (-i)

        def sum(self, r):
            s = 0
            while r > 0:
                s += self.__container[r]
                r -= r & (-r)
            return s

        def upper_bound(self, s):
            w, r = 0, 0
            for i in reversed(range(self.__depth)):
                k = r + (1 << i)
                if k < self.__size and w + self.__container[k] <= s:
                    w += self.__container[k]
                    r += 1 << i
            return r

    __load = 1000

    def __init__(self):
        self.__lists = []
        self.__maxes = []
        self.__sizes_list = []
        self.__sizes_ft = self.FenwickTree([])
        self.__len = 0
        self.__block_count = 0

    def add(self, x):
        if self.__len > 0:
            li = bisect_left(self.__maxes, x)
            if li == len(self.__maxes):
                li -= 1
                self.__maxes[-1] = x
            _list = self.__lists[li]
            insort(_list, x)
            self.__sizes_list[li] += 1
            self.__sizes_ft.add(li, 1)
            if len(_list) >= 2 * self.__load:
                self.__split(li)
        else:
            self.__maxes.append(x)
            self.__lists.append([x])
            self.__sizes_list.append(1)
            self.__build_ft()
            self.__block_count += 1
        self.__len += 1

    def discard(self, x):
        if self.__len == 0:
            return False
        li = bisect_left(self.__maxes, x)
        if li == self.__block_count:
            return False
        __list = self.__lists[li]
        lli = bisect_left(__list, x)
        y = __list[lli]
        if x != y:
            return False
        del __list[lli]
        if not __list:
            del self.__lists[li]
            del self.__maxes[li]
            del self.__sizes_list[li]
            self.__block_count -= 1
            self.__len -= 1
            self.__build_ft()
            return True
        if x == self.__maxes[li]:
            self.__maxes[li] = __list[-1]
        self.__len -= 1
        self.__sizes_ft.add(li, -1)
        self.__sizes_list[li] -= 1
        if self.__block_count >= 2 and 2 * self.__sizes_list[li] <= self.__load:
            self.__marge(li)
        return True

    def contains(self, x):
        if self.__len == 0:
            return False
        li = bisect_left(self.__maxes, x)
        if li == self.__block_count:
            return False
        _list = self.__lists[li]
        lli = bisect_left(_list, x)
        y = _list[lli]
        return x == y

    def index(self, x):
        if self.__len == 0:
            return None
        li = bisect_left(self.__maxes, x)
        if li == self.__block_count:
            return None
        _list = self.__lists[li]
        lli = bisect_left(_list, x)
        y = _list[lli]
        if x != y:
            return None
        ft = self.__sizes_ft
        return ft.sum(li) + lli

    def index_right(self, x):
        if self.__len == 0:
            return None
        li = bisect_right(self.__maxes, x)
        if li == self.__block_count:
            y = self.__lists[-1][-1]
            return self.__pos(li - 1, self.__sizes_list[-1] - 1) if y == x else None
        _list = self.__lists[li]
        lli = bisect_right(_list, x) - 1
        if lli == -1:
            if li == 0:
                return None
            y = self.__lists[li - 1][-1]
            return self.__pos(li - 1, self.__sizes_list[li - 1] - 1) if y == x else None
        y = _list[lli]
        if x != y:
            return None
        return self.__pos(li, lli)

    def bisect_left(self, x):
        li = bisect_left(self.__maxes, x)
        if li == self.__block_count:
            return self.__pos(self.__block_count, 0)
        lli = bisect_left(self.__lists[li], x)
        return self.__pos(li, lli)

    def bisect_right(self, x):
        li = bisect_right(self.__maxes, x)
        if li == self.__block_count:
            return self.__pos(self.__block_count, 0)
        lli = bisect_right(self.__lists[li], x)
        return self.__pos(li, lli)

    def count(self, x):
        return self.bisect_right(x) - self.bisect_left(x)

    def le(self, x):
        if self.__len == 0:
            return None
        li = bisect_left(self.__maxes, x)
        if li == self.__block_count:
            return self.__lists[li - 1][-1]
        _list = self.__lists[li]
        lli = bisect_right(_list, x)
        if lli == 0:
            if li == 0:
                return None
            return self.__lists[li - 1][-1]
        return self.__lists[li][lli - 1]

    def lt(self, x):
        if self.__len == 0:
            return None
        li = bisect_left(self.__maxes, x)
        if li == self.__block_count:
            return self.__lists[li - 1][-1]
        _list = self.__lists[li]
        lli = bisect_left(_list, x)
        if lli == 0:
            if li == 0:
                return None
            return self.__lists[li - 1][-1]
        return self.__lists[li][lli - 1]

    def ge(self, x):
        if self.__len == 0:
            return None
        li = bisect_left(self.__maxes, x)
        if li == self.__block_count:
            y = self.__lists[-1][-1]
            return y if y == x else None
        _list = self.__lists[li]
        lli = bisect_left(_list, x)
        return self.__lists[li][lli]

    def gt(self, x):
        if self.__len == 0:
            return None
        li = bisect_right(self.__maxes, x)
        if li == self.__block_count:
            return None
        _list = self.__lists[li]
        lli = bisect_right(_list, x)
        return self.__lists[li][lli]

    @property
    def max(self):
        return self[self.__len - 1]

    @property
    def min(self):
        return self[0]

    def __build_ft(self):
        self.__sizes_ft = self.FenwickTree(self.__sizes_list)

    def __pos(self, li, lli):
        return self.__sizes_ft.sum(li) + lli

    def __split(self, li):
        _list = self.__lists[li]
        sz = self.__sizes_list[li]
        self.__maxes.insert(li + 1, _list[-1])
        self.__lists.insert(li + 1, _list[self.__load:])

        del _list[self.__load:]
        self.__maxes[li] = _list[-1]

        self.__sizes_list[li] = self.__load
        self.__sizes_list.insert(li + 1, sz - self.__load)
        self.__build_ft()
        self.__block_count += 1

    def __marge(self, li):
        if li == 0:
            self.__lists[0].extend(self.__lists[1])
            self.__sizes_list[0] += self.__sizes_list[1]
            self.__maxes[0] = self.__maxes[1]
            del self.__lists[1]
            del self.__maxes[1]
            del self.__sizes_list[1]
            self.__block_count -= 1
            if self.__sizes_list[0] >= 2 * self.__load:
                return self.__split(0)
        else:
            self.__lists[li - 1].extend(self.__lists[li])
            self.__sizes_list[li - 1] += self.__sizes_list[li]
            self.__maxes[li - 1] = self.__maxes[li]
            del self.__lists[li]
            del self.__maxes[li]
            del self.__sizes_list[li]
            self.__block_count -= 1
            if self.__sizes_list[li - 1] >= 2 * self.__load:
                return self.__split(li - 1)
        self.__build_ft()

    def __len__(self):
        return self.__len

    def __contains__(self, x):
        return self.contains(x)

    def __getitem__(self, i):
        if i < 0:
            i += self.__len
        ft = self.__sizes_ft
        li = ft.upper_bound(i)
        lli = i - ft.sum(li)
        return self.__lists[li][lli]

    def get_all_values(self):
        ret = []
        for _list in self.__lists:
            ret.extend(_list)
        return ret


def main():
    Q = int(input())
    S = OrderedMultiList()
    for _ in range(Q):
        query = list(map(int, input().split()))
        q = query[0]
        if q == 1:
            x = query[1]
            S.add(x)
        elif q == 2:
            x, c = query[1:]
            time = min(c,S.count(x))
            for _ in range(time):
                S.discard(x)
        else:  # q == 3
            print(S.max - S.min)


if __name__ == '__main__':
    main()

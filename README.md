# advent-of-code-2015

Decent solutions overall. Some very nice -- others could be improved (in terms of both elegance and performance).

If you don't see a part2, there either wasn't one (like on day 25), or the answer was deduced or part1 was used with modified input.

You'll also notice that I often don't actually memoize my dfs functions, I just use a closure dict of args to prevent recursing into a search space that's already been traversed elsewhere in the recursion tree.


def arrayRankTransform(self, arr: list[int]) -> list[int]:
      hash = {}
      seen = sorted(set(arr))
      for indx, val in enumerate(seen, 1):
          hash[val] = indx
      return [hash[num] for num in arr]
class Solution:
    def compress(self, chars: List[str]) -> int:
        c = 1
        prev = ""
        prev_index = 0   # start writing at 0

        for i in range(len(chars)):
            if i == 0:
                c = 1
                prev = chars[i]
            elif chars[i] == prev:
                c += 1
            else:
                # write previous char
                chars[prev_index] = prev
                prev_index += 1

                # write count if > 1
                if c > 1:
                    for digit in str(c):
                        chars[prev_index] = digit
                        prev_index += 1

                # reset for new char
                prev = chars[i]
                c = 1

        # handle last group after loop ends
        chars[prev_index] = prev
        prev_index += 1
        if c > 1:
            for digit in str(c):
                chars[prev_index] = digit
                prev_index += 1

        # trim array in-place
        chars[:] = chars[:prev_index]
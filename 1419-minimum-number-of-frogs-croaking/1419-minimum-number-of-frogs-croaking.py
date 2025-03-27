class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        croak = "croak"
        frog_count = 0
        max_frogs = 0
        
        # Array to track the count of each character in the sequence
        char_count = [0] * 5
        
        for ch in croakOfFrogs:
            if ch not in croak:
                return -1
            
            index = croak.index(ch)
            char_count[index] += 1
            
            # Check that the previous character has enough counts before progressing
            if index > 0 and char_count[index - 1] < char_count[index]:
                return -1
            
            # If we encounter 'c', a new frog starts croaking
            if ch == 'c':
                frog_count += 1
                max_frogs = max(max_frogs, frog_count)
            
            # If we encounter 'k', one frog completes the croak
            elif ch == 'k':
                frog_count -= 1
        
        # Check if all counts are balanced at the end
        if frog_count == 0 and all(count == char_count[4] for count in char_count):
            return max_frogs
        else:
            return -1

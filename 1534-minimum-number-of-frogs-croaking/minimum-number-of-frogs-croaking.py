class Solution:
    def find_frogs(self, croakOfFrogs, index, croak, count, frog_count, max_frogs):
        if index == len(croakOfFrogs):
            # Check if all characters are balanced at the end
            if all(count[i] == 0 for i in range(4)):
                return max_frogs
            else:
                return -1
        
        ch = croakOfFrogs[index]
        
        # Get the index of the current character in "croak"
        pos = croak.find(ch)
        
        if pos == 0:  # Start of a new croak ("c")
            count[pos] += 1
            frog_count += 1
            max_frogs = max(max_frogs, frog_count)
        
        elif 0 < pos <= 4:  # Next valid character in the croak sequence
            if count[pos - 1] == 0:
                return -1  # Invalid sequence if the previous character is not available
            count[pos - 1] -= 1
            count[pos] += 1
            
            # If the frog finishes croaking ("k")
            if pos == 4:
                frog_count -= 1
                count[pos] -= 1
        
        else:
            return -1  # Invalid character
        
        # Recursive call for the next character
        return self.find_frogs(croakOfFrogs, index + 1, croak, count, frog_count, max_frogs)
    
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        croak = "croak"
        
        # Length must be divisible by 5 for valid sequences
        if len(croakOfFrogs) % 5 != 0:
            return -1
        
        # Array to track the count of "c", "r", "o", "a" (skip "k" as it resets)
        count = [0] * 5
        
        return self.find_frogs(croakOfFrogs, 0, croak, count, 0, 0)

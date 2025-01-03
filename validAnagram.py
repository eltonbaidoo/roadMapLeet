def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        '''
        m = len(s) - 1
        for ch in s:
            if ch != t[m]:
                return False
            m -= 1
        return True
        '''
        if len(s) != len(t):
            return False
        sSorted = ''.join(sorted(s))
        tSorted = ''.join(sorted(t))

        return sSorted == tSorted
        
        


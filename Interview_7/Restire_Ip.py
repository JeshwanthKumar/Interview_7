class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        n = len(s)
        #edge condition     
        self.result=[]
        self.backtrack(n,s,0,[])
        return self.result


    def backtrack(self,n,s,pivot,substrings):
        #base condition
        if pivot==n and len(substrings)==4:
            temp = ".".join(substrings)
            self.result.append(temp)
            return

        if len(substrings)>4:
            return
        #logic
        for i in range(pivot,len(s)):
            substr = s[pivot:i+1]
            if self.isValidIP(substr):
                #action
                substrings.append(substr)

                #recurse
                self.backtrack(n,s,i+1,substrings)

                #backtrack
                substrings.pop()



    def isValidIP(self,s):
        ip = int(s)

        #check nums like 023 - which is not valid
        if len(s)!=len(str(ip)):
            return False

        if ip<0 or ip>255:
            return False
        return True
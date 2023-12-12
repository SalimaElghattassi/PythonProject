class myString:
    def _init_(self,s):
        self.s = s
    def append(self,x):
        self.s = self.s + x
        return self.s

    def pop(self,i):
        s1 = self.s[0:i]
        s2 = self.s[i+1:len(self.s)]
        return s1+s2
    def modifier(self,i):
        pass
        
# Tester la classe       
S = myString("hello world")
print(S.pop(1)) # affiche 'hllo'
print(S.append(" world !")) # affiche 'hello world !'
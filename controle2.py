
from math import *
class Cercle:
    def init(self,a,b,r):
        self.a = a
        self.b = b
        self.r = r
    
    def perimetre(self):
        return 2*pi*self.r
       
        
    def surface(self):
        return pi*self.r**2

    def formEquation(self,x,y):      
        return (x-self.a)*2 + (y-self.b)**2 -self.r*2
    def test_appartenance(self,x,y):
        if(self.formEquation(x,y)==0):
            print("le point : (",x,y,") appartient au cercle C")
        else:
            print("le point : (",x,y,") n'appartient pas au cercle C")
            
        
 
C = Cercle(1,2,1)

print("le périmètre du cercle C est  : ", C.perimetre())
print("le surface du cercle C est  : ", C.surface())
C.test_appartenance(1,1)




class CompteBancaire:
    def __init__(self, number, nomPrenom, solde):
        self.numb = number
        self.np = nomPrenom
        self.sld = solde

    def versement(self, montant):
        self.sld = self.sld + montant

    def retrait(self, argent):
        if self.sld < argent:
            print("Impossible d'effectuer cette opération")
        else:
            self.sld = self.sld - argent

    def afficher(self):
        print("Numéro de compte:", self.numb) 
        print("Nom et prénom:", self.np)
        print("Solde:", self.sld)

moncompte = CompteBancaire(123, "Ahmed Alaoui", 10000)
moncompte.afficher()
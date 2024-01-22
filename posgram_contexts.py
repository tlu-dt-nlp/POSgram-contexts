import json
import stanza

class PosgramContexts:
    def __init__(self, text, nlength=4):
        self.nlp=stanza.Pipeline(lang="et", processors="tokenize,pos")
        self.nlength=nlength
        self.dok=self.nlp(text)
        sonaliigijadad=["^"+"".join([sona.xpos for sona in lause.words if sona.xpos])+"$" for lause in self.dok.sentences]
        self.hoidla={}
        nr=0
        for rida in sonaliigijadad:
          nr+=1
          if nr % 10000 == 0: print(nr)
          r=rida.strip().replace("Z", "") #kirjavahemärgid välja
          ngramid=[r[koht: koht+self.nlength] for koht in range(len(r)-self.nlength+1)]
          for ngram in ngramid:
            if ngram in self.hoidla: self.hoidla[ngram]+=1
            else: self.hoidla[ngram]=1

    def precontexts(self, filename=""):
        c=self.contexts(self.hoidla, "pre")
        if filename:
            f2=open(filename, "w", encoding="utf-8") 
            json.dump(c, fp=f2)
            f2.close()
        return c

    def postcontexts(self, filename=""):
        c=self.contexts(self.hoidla, "post")
        if filename:
            f2=open(filename, "w", encoding="utf-8") 
            json.dump(c, fp=f2)
            f2.close()
        return c

    def contexts(self, hoidla, ctype):
        eelmine=""
        kogused={}
        koikkogused={}
        plokkkokku=0
        for voti in sorted(hoidla.keys(), key=lambda v: v[:-1] if ctype=="post" else v[1:]):
           if ctype=="post":
              ngram=voti[:-1]
              context=voti[-1]
           else:
              ngram=voti[1:]
              context=voti[0]
           if eelmine and ngram!=eelmine:
              self.percentages(kogused)
              koikkogused[eelmine]=kogused
              kogused={}
           kogused[context]=[hoidla[voti]]
           eelmine=ngram
        koikkogused[eelmine]=kogused
        self.percentages(kogused)
        return koikkogused

    def percentages(self, kogused):
        plokkkokku=sum([v[0] for v in kogused.values()])
        for kontekst in kogused.keys():
           kogused[kontekst].append(kogused[kontekst][0]*100/plokkkokku)       


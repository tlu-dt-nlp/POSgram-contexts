from posgram_contexts import PosgramContexts

p = PosgramContexts("""Juku tuli kooli. Juku tuli kooli ruttu. Unine Juku tuli kooli.""")
print(p.precontexts())
print(p.postcontexts())

#Input from file. 
#The example text file contains the L1 reference subcorpus of the Estonian Interlanguage Corpus.
#This subcorpus consists of opinion articles published on the websites of Postimees and Õhtuleht in 2014.
#See https://elle.tlu.ee/tools/.
p = PosgramContexts(open("EIC_L1_reference.txt", "r", encoding="utf-8").read())
p.precontexts("EIC_L1_pre.json")
p.postcontexts("EIC_L1_post.json")

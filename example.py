from posgram_contexts import PosgramContexts

p=PosgramContexts("""Juku tuli kooli. Juku tuli kooli ruttu. Unine Juku tuli kooli.""")
print(p.precontexts())        
p.precontexts("juku_pre.json")
p.postcontexts("juku_post.json")

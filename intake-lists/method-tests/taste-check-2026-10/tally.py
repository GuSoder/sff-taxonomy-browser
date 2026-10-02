import json,hashlib,os,re,collections
from ext import o,rd
M={ # title:(group,imprint)
'the devils':('Hachette','Gollancz'),'king sorrow':('HarperCollins','Morrow'),'grave empire':('Hachette','Orbit'),'steel gods':('Hachette','Orbit'),'the infinite state':('Hachette','Gollancz'),
'the raven scholar':('Hachette','Orbit'),'the everlasting':('Macmillan','Tor'),'a drop of corruption':('PRH','Del Rey'),'the tainted cup':('PRH','Del Rey'),'the keeper of magical things':('PRH','Del Rey'),
'a sorceress comes to call':('Macmillan','Tor'),'silver':('Macmillan','Tor'),'the incandescent':('Macmillan','Tordotcom'),'the river has roots':('Macmillan','Tordotcom'),
'the girl with a thousand faces':('HarperCollins','Harper Voyager'),'the butcher of the forest':('Macmillan','Tordotcom'),'the tusks of extinction':('Macmillan','Tordotcom'),
'service model':('Macmillan','Tordotcom'),'shroud':('Macmillan','Tor/Tordotcom'),'alien clay':('Hachette','Orbit US / Tor UK (split)'),'automatic noodle':('Macmillan','Tordotcom'),'platform decay':('Macmillan','Tordotcom'),
'overgrowth':('Macmillan','Tor Nightfire'),'the red winter':('Macmillan','Tor'),'wooing the witch queen':('Macmillan','Tordotcom'),'asunder':('Macmillan','Tordotcom'),'harmattan season':('Macmillan','Tordotcom'),
'brighter than scale, swifter than flight':('Macmillan','Tordotcom'),'rakesfall':('Macmillan','Tordotcom/Solaris'),'anji kills a king':('Macmillan','Tordotcom'),'the enchanted greenhouse':('Macmillan','Tor'),
'murder by memory':('Macmillan','Tordotcom'),'the practice, the horizon, and the chain':('Macmillan','Tordotcom'),"let's go to the zoo":('Macmillan','Tordotcom'),'bury our bones in the midnight soil':('Macmillan','Tor'),'victorious':('Macmillan','Tor'),
'witchcraft for wayward girls':('PRH','Berkley'),'the staircase in the woods':('PRH','Del Rey'),"agnes aubert\u2019s mystical cat shelter":('PRH','Del Rey (US)/Orbit (UK)'),'the unlikely escape of uriah heep':('Hachette','Orbit'),
'slow gods':('Hachette','Orbit'),'the bright sword':('PRH','Viking'),'greenteeth':('Hachette','Orbit'),'the starving saints':('HarperCollins','Harper Voyager'),'the book that held her heart':('HarperCollins','Harper Voyager'),
'daughter of crows':('HarperCollins','Harper Voyager'),'empire of the dawn':('HarperCollins','Harper Voyager'),'the fury of the gods':('Hachette','Orbit'),'the company of the wolf':('HarperCollins','Harper Voyager'),
'a letter to the luminous deep':('Hachette','Orbit'),'the last contract of isako':('Hachette','Orbit'),'someone you can build a nest in':('PRH','DAW'),'wearing the lion':('PRH','DAW'),'death of the author':('HarperCollins','Harper Voyager/Morrow'),
'all that we see or seem':('S&S','Saga'),'play nice':('PRH','Berkley'),'project hail mary':('PRH','Ballantine/Del Rey'),'where the axe is buried':('Other/unclear','FSG/Mantle'),'the dark mirror':('Other','Bloomsbury')}
ol=json.load(open('ol.json'));
blog=collections.defaultdict(int)
for r in ol:
    if r['title'] in M:blog[r['title']]+=r['blog']
# fix: blog counts via full text
txt={}
for k in('blog','yt'):
    for u,t,d in o[k]:
        if k=='yt' and 'watch?v=' not in u:continue
        tx=rd(u)
        if len(tx)>=1500:txt[(k,u)]=tx.lower()
cnt={k:{t:0 for t in M} for k in('blog','yt')}
for (k,u),tx in txt.items():
    for t in M:
        if len(t)<7 and t=='silver':
            if 'silver' in tx and 'kingfisher' in tx and re.search(r'\bsilver\b',tx):cnt[k][t]+=1
        elif t.replace('\u2019',"'") in tx.replace('\u2019',"'"):cnt[k][t]+=1
for k in('blog','yt'):
    print(k,sum(1 for x in txt if x[0]==k),'sources')
    byg=collections.Counter();byi=collections.Counter();bk=collections.Counter()
    for t,(g,i) in M.items():
        n=cnt[k][t]
        if n:byg[g]+=n;byi[i]+=n;bk[g]+=1
    print(' source-mentions by group',byg.most_common());print(' distinct books',bk.most_common());print(' imprint',byi.most_common(12))
tot=collections.Counter()
for t,(g,i) in M.items():
    tot[(g)]+=cnt['blog'][t]+cnt['yt'][t]
print(tot.most_common())
print(sorted(((cnt['yt'][t],cnt['blog'][t],t) for t in M),reverse=True)[:15])

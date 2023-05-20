cip_txt = """
    qmnjvsa nv wewc flct vprj tj tvvplvl fv xja vqildhc
	xmlnvc nacyclpa fc gyt vfvw. fv wgqyp, pqq pqcs y wsq
	rx qmnjvafy cgv tlvhf cw tyl aeuq fv xja tkbv cqnsqs. 
	lhf avawnc cv eas fuqb qvq tc yllrqr xxwa cfy. psdc uqf
	avrqc gefq pyat trac xwv taa wwd dv eas flcbq. vd trawm
	vupq quw x decgqcwt, yq yafl vlqs yqklhq! snafq vml
	lhvqpawr nqg_vfusr_ec_wawy qp fn wgawdgf.
"""

key = [4,3,5,1,2]

li = []
lu = []
pln_txt = list(cip_txt)
ctr = 0

for i in range(len(pln_txt)):
    if cip_txt[i] >= 'a' and cip_txt[i] <= 'z':
        ctr += 1
        li.append(i)
        lu.append(pln_txt[i])
    
    if ctr == len(key):
        ctr = 0
        for j in range(len(key)):
            pln_txt[li[j]] = lu[key[j]-1]
        #print(lu)
        li = []
        lu = []
    


print("".join(pln_txt))
# Substitution-Permutation Cipher
This repository contains our methodology to break the 3rd level of the server game 'Escaping the Caves', as part of the course CS641A.

We were first presented with following ciphertext -

  _qmnjvsa nv wewc flct vprj tj tvvplvl fv xja vqildhc_</br>
_xmlnvc nacyclpa fc gyt vfvw. fv wgqyp, pqq pqcs y wsq_</br>
_rx qmnjvafy cgv tlvhf cw tyl aeuq fv xja tkbv cqnsqs. _</br>
_lhf avawnc cv eas fuqb qvq tc yllrqr xxwa cfy. psdc uqf_</br>
_avrqc gefq pyat trac xwv taa wwd dv eas flcbq. vd trawm_</br>
_vupq quw x decgqcwt, yq yafl vlqs yqklhq! snafq vml_</br>
_lhvqpawr nqg_vfusr_ec_wawy qp fn wgawdgf. _

### Observation 1 
We see two different single-letter words - "x" and "y". Now, it can be an example of a simple substitution cipher in case they correspond to "a" and "i" (since all letters are in lower-case, we assume "i" will be "I" in the actual plaintext). However, if "x" corresponds to either "a" or "i", "xxwa" in the ciphertext would not have a corresponding plaintext word that would make sense. Thus, we come to the conclusion that the plaintext has not been simply encrypted using a substitution cipher.

### Observation 2
After doing a frequency analysis for the given ciphertext, we find that the frequencies are not exactly flattened, as we would hope for in case of a simple permutation cipher. Therefore, we suspect that the message might have been encrypted using both permutation and substitution. Our next task was to identify the possible block size of such a permutation. 

### Observation 3
After finding the phrase "nqg_vfusr_ec_wawy" in the last line, we realised it was most likely the password required to crack the round, and therefore made an educated guess that the preceding word "lhvqpawr" should correspond to "password" in the plaintext (the fact that it was also eight letters strengthened our suspicion). To find the block size, we used the following methodology:

### Observation 4
As we are assuming "lhvqpawr" should correspond to "password", there should be two positions in "lhvqpawr" that correspond to the same letter which would correspond to 's'. Assuming the block size is not very large, the letter must be permuted from the nearby words like {"snafq", "vml", "nqg_vfusr_ec_wawy"}. This shortlisted {'v' and 'l'} as the possible words which were permuted from their positions into one of the positions of "lhvqpawr". After checking for block sizes ranging from 1 to 10, we find that when the block size is 5, the text is divided as { fq vm/l lhvq/pawr n/ }. This makes it possible for 'l' form "vml" to have permuted within the block {l,l,h,v,q} and finally allowed the two 'l's to come together, corresponding to the two 's's in 'password'. At this point, we were quite confident that the block size should be five.

### Observation 5
Since the letter 's' would correspond to the 4th and 5th position, the two 'l's should also correspond to the same positions. This leaves us with 4!/2! = 12 possibilities, as the ordering of the permutation would be either [4,5,_,_,_] or [5,4,_,_,_]. So we carried out a substitution of the most frequent letters and a possible permutation [4,3,5,2,1]. As 'q' and 'v' were the most frequent letters in the original ciphertext (both occurring around 10%, with q being slightly higher) . Thus, we started out by replacing 'q' with 'A', 'v' with 'E', and 'l' with 'S', 
 and performing the permutation. We got the following text - 

_jnEmAEn wa sfcS wepE rtct jE tjESSpE jx aEf SidAEmx_</br>
_Schnca EnScpycg cy faE fwEt. gw AEfAp, Apy scyA p rAx_</br>
_sw jnEmAcyg faE ShtEt wy cfu eAaS jx aEf Ebck tAssnA._</br>
_afE hScncw as afe EAbE Auy cS tArAxr Scaf wxd. scpy afE_</br>
_Augce Aryp aAfa rctt tEa wxd wdw as afe EAbEc. Sa rwtdp_</br>
_uAEm xwd u AAgcceAy, yt wESS faAy ksAsAn! hSEAm faE_</br>
_hASSrwna pfE_ugAce_wr_sAyp wa gw anfwdgf._


Since we are receiving 'p' and 'u' as two separate one-letter words, we suspect that the permutation order might be wrong. After trying to come up with orders which could lead to the same letter for single-letter words, we use the following permutation - [4,3,5,1,2]. After making the previous substitutions, we get the following text - 

_jnEAmEn ws afcS ewpE rctt jE jtESSEp jx afE SidEAmx_</br>
_Shcnca nEScpcyg cy afE fwtE. gw AfEAp, Ayp scyp A rAx_</br>
_ws jnEAmcyg afE ShEtt wy fcu eASa jx afE Ebct kAssAn._</br>
_afE Shcnca ws afE eAbE uAy cS AtrAxS rcaf xwd. scyp afE_</br>
_uAgce rAyp afAa rctt tEa xwd wda ws afE eAbES. ca rwdtp_</br>
_uAmE xwd A uAgcecAy, yw tESS afAy kAssAn! ShEAm afE_</br>
_hASSrwnp afE_uAgce_ws_rAyp aw gw afnwdgf._

### Observation 6
We can clearly make out certain phrases in this like "afE" seems to be corresponding to "THE" and " hASSrwnp" seems to be corresponding to "PASSWORD" as we suspected. </br>
Applying these heuristics we finally have our alphabet mapping for the mono alphabetic substitution as
**abcdefghijklmnpqrstuvwxy** (in ciphertext) ==> **tviuchgpqbjskrdawflmeoyn** (in plaintext) (Letters o and z do not appear in the ciphertext)

We finally get the plaintext as - 

_breaker of this code will be blessed by the squeaky_</br>
_spirit residing in the hole. go ahead, and find a way_</br>
_of breaking the spell on him cast by the evil jaffar._</br>
_the spirit of the cave man is always with you. find the_</br>
_magic wand that will let you out of the caves. it would_</br>
_make you a magician, no less than jaffar! speak the_</br>
_password the_magic_of_wand to go through._


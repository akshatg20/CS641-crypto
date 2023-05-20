#include<iostream>
#include<vector>
#include<string>
using namespace std;

int main(int argc, char const *argv[])
{
    string s = "qmnjvsa nv wewc flct vprj tj tvvplvl fv xja vqildhc xmlnvc nacyclpa fc gyt vfvw. fv wgqyp, pqq pqcs y wsq rx qmnjvafy cgv tlvhf cw tyl aeuq fv xja tkbv cqnsqs.  lhf avawnc cv eas fuqb qvq tc yllrqr xxwa cfy. psdc uqf avrqc gefq pyat trac xwv taa wwd dv eas flcbq. vd trawm vupq quw x decgqcwt, yq yafl vlqs yqklhq! snafq vml lhvqpawr nqg_vfusr_ec_wawy qp fn wgawdgf.";
    vector<int> v(26,0);
    for(int i=0; i<s.length(); i++){
        if((s[i] >= 'a') && (s[i] <= 'z'))
            v[s[i] - 'a']++;
        else if((s[i] >= 'A') && (s[i] <= 'Z'))
            v[s[i] - 'A']++;
    }
    char c = 'a';
    float su = 0;
    for(int i=0; i<26; i++)
        su += v[i];
    for(int i=0; i<26; i++)
        cout << char(c + i) << ": " << v[i] << '\t' << float(v[i]/su)*100.0 << '\n';
    return 0;
}
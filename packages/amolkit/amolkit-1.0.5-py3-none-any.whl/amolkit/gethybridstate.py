import collections
from operator import itemgetter
from collections import OrderedDict
from ffparam import sourcepath
from ffparam.ffpcore.misc import flatten

def localranking(ama):
    rule={"H":1,"O":2,"N":3,"C":4}
    rnk=rule.get(ama)
    if rnk is None: rnk=5
    return(rnk)

def name2num(cnvlist,mapedatoms):
    inumaic=[]
    if type(cnvlist)==list:
        for ijc in cnvlist:
            inumaic.append(mapedatoms['mapnames'][ijc][0])
    return (inumaic)

def get_symmetry_type(core,value,mapedatoms,ringeles):

    def sortatoms(val):
        htyp=[];xyztyp=[]
        nums=list(map(lambda v:v[0],val))
        cntitm=[[item,count] for item, count in collections.Counter(nums).items()]
        cntitm=sorted(cntitm, key=itemgetter(1),reverse=True)
        cntitm=sorted(cntitm, key=lambda ix: localranking(ix[0][0]))
        for v in val:
            if v[0] == cntitm[0][0]:
               htyp.append(v)
            else:
               xyztyp.append(v)
        return (htyp,xyztyp)
    print (value)
    htyp,xyztyp=sortatoms(value)
    print (htyp)
    print (xyztyp)

    #ringcheck=list(set([mapedatoms['mapnames'][core][0]-1]).intersection(ringeles))
    ringcheck=list(set([mapedatoms[core]-1]).intersection(ringeles))
    print (ringeles)
    print (ringcheck)

    if ringcheck:
       if len(value) > 4:
           symmetry_type = "unknown"
       else:
           hxyznum=name2num([*htyp,*xyztyp],mapedatoms)
           pyhxyznum=list(map(lambda x:x-1, hxyznum))
           valueringcheck=list(set(pyhxyznum).intersection(ringeles))
           if len(hxyznum)-len(valueringcheck)==2: symmetry_type="ring_sp3"
           if len(hxyznum)-len(valueringcheck)==1: symmetry_type="ring_sp2"
           if len(hxyznum)-len(valueringcheck)==0: symmetry_type="ring_sp"
    else:
       if len(value) > 4:
          symmetry_type = "unknown"
       elif len(value) == 4:
          if (len(htyp) == 3): symmetry_type = "methyl_sp3"
          if (len(htyp) == 2): symmetry_type = "methylene_sp3"
          if (len(htyp) == 1): symmetry_type = "methine_sp3"
       elif len(value) == 3:
          if (len(htyp) == 3): symmetry_type = "amino" if core[0] == "N" else "methyl_sp3"   # <============
          if (len(htyp) == 2): symmetry_type = "amino" if core[0] == "N" else "methylene_sp2"
          if (len(htyp) == 1): symmetry_type = "imino" if core[0] == "N" else "methine_sp2"
       elif len(value) == 2:
          symmetry_type = "sp"
       elif len(value) == 1:
          symmetry_type = "end"
       else:
          symmetry_type = "unknown"
    return symmetry_type, [*htyp,*xyztyp] #,ringcheck


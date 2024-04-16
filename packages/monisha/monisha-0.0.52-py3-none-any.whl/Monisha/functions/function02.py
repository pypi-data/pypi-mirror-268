from ..scripts.es import Humon
from ..scripts.en import Scripted
#=============================================================================

def Dbytes(sizes, second=Scripted.DATA01):
    if not sizes or (sizes == Scripted.DATA02):
        return Scripted.DATA09
    nomos = 0
    POWEO = 2**10
    POWER = Humon.DATA01
    while sizes > POWEO:
        sizes /= POWEO
        nomos += 1
    ouing = str(round(sizes, 2)) + Scripted.DATA02 + POWER[nomos] + second
    return ouing

#=============================================================================

def Hbytes(sizes, second=Scripted.DATA01):
    if not sizes or (sizes == Scripted.DATA02):
        return Scripted.DATA08
    nomos = 0
    POWEO = 2**10
    POWER = Humon.DATA02
    while sizes > POWEO:
        sizes /= POWEO
        nomos += 1
    ouing = str(round(sizes, 2)) + Scripted.DATA02 + POWER[nomos] + second
    return ouing

#=============================================================================

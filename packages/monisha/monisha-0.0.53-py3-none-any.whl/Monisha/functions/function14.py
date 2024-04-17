import os, time
from ..scripts.es import Folder
from ..scripts.en import Scripted
#============================================================================

async def CDirectory(dname=Folder.DATA07):
    direos = str(dname)
    osemse = os.getcwd()
    moonse = os.path.join(osemse, direos, Scripted.DATA01)
    moonse if os.path.isdir(moonse) else os.makedirs(moonse)
    return moonse

#============================================================================

async def UDirectory(dname=Folder.DATA07):
    direos = str(dname)
    osemse = os.getcwd()
    timeso = str(round(time.time()))
    moonse = os.path.join(osemse, direos, timeso, Scripted.DATA01)
    moonse if os.path.isdir(moonse) else os.makedirs(moonse)
    return moonse

#============================================================================

async def BDirectory(uid, dname=Folder.DATA07):
    usered = str(uid)
    direos = str(dname)
    osemse = os.getcwd()
    timeso = str(round(time.time()))
    moonse = os.path.join(osemse, direos, usered, timeso, Scripted.DATA01)
    moonse if os.path.isdir(moonse) else os.makedirs(moonse)
    return moonse

#============================================================================

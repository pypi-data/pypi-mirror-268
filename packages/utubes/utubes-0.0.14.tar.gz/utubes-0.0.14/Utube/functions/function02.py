from ..scripts.es import Smbo
from pyrogram.types import MessageEntity
#=============================================================================================

class RMessages:
    def __init__(self, **kwargs):
        self.flielink = kwargs.get("flielink", None)
        self.filename = kwargs.get("filename", None)
        self.username = kwargs.get("username", None)
        self.password = kwargs.get("password", None)

#=============================================================================================

async def flinked(update: MessageEntity, incoming):
    try:
        for entity in update.entities:
            if entity.type == "text_link":
                uox = entity.incoming
            elif entity.type == "url":
                oxe = entity.offset
                omo = entity.length
                uox = incoming[oxe : oxe + omo]
            else:
                uox = incoming
        else:
            uox = incoming
    except Exception:
        uox = None

    return uox

#=============================================================================================

class ExtractoR:

    async def ext01(update, incoming):
        poxwers = incoming.split(Smbo.DATA04)
        if len(poxwers) == 2 and Smbo.DATA04 in incoming:
             Username = None
             Password = None
             Flielink = poxwers[0] # INCOMING URL
             Filename = poxwers[1] # INCOMING FILENAME
        elif len(poxwers) == 3 and Smbo.DATA04 in incoming:
             Filename = None
             Flielink = poxwers[0] # INCOMING URL
             Username = poxwers[1] # INCOMING USERNAME
             Password = poxwers[2] # INCOMING PASSWORD
        elif len(poxwers) == 4 and Smbo.DATA04 in incoming:
             Flielink = poxwers[0] # INCOMING URL
             Filename = poxwers[1] # INCOMING FILENAME
             Username = poxwers[2] # INCOMING USERNAME
             Password = poxwers[3] # INCOMING PASSWORD
        else:
             Filename = None # INCOMING FILENAME
             Username = None # INCOMING USERNAME
             Password = None # INCOMING PASSWORD
             Flielink = await flinked(update, incoming)

        moon01 = Flielink.strip() if Flielink != None else None
        moon02 = Filename.strip() if Filename != None else None
        moon03 = Username.strip() if Username != None else None
        moon04 = Password.strip() if Password != None else None
        return RMessages(flielink=moon01, filename=moon02, username=moon03, password=moon04)

#=============================================================================================

    async def ext02(update, filename, incoming):
        poxwers = incoming.split(Smbo.DATA04)
        if len(poxwers) == 2 and Smbo.DATA04 in incoming:
             Username = None
             Password = None
             Flielink = poxwers[0] # INCOMING URL
             Filename = poxwers[1] # INCOMING FILENAME
        elif len(poxwers) == 3 and Smbo.DATA04 in incoming:
             Filename = None
             Flielink = poxwers[0] # INCOMING URL
             Username = poxwers[1] # INCOMING USERNAME
             Password = poxwers[2] # INCOMING PASSWORD
        elif len(poxwers) == 4 and Smbo.DATA04 in incoming:
             Flielink = poxwers[0] # INCOMING URL
             Filename = poxwers[1] # INCOMING FILENAME
             Username = poxwers[2] # INCOMING USERNAME
             Password = poxwers[3] # INCOMING PASSWORD
        else:
             Filename = None # INCOMING FILENAME
             Username = None # INCOMING USERNAME
             Password = None # INCOMING PASSWORD
             Flielink = await flinked(update, incoming)

        moon01 = Flielink.strip() if Flielink != None else None
        moon03 = Username.strip() if Username != None else None
        moon04 = Password.strip() if Password != None else None
        moon02 = Filename.strip() if Filename != None else filename
        return RMessages(flielink=moon01, filename=moon02, username=moon03, password=moon04)

#=============================================================================================

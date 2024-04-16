import asyncio
from ..scripts.eo import Okeys
from yt_dlp import YoutubeDL, DownloadError
#======================================================================================================

class Utube:

    def __init__(self):
        self.fnames = None
        self.result = None
        self.errors = None
        self.status = True
        self.downdl = OKeys.DATA01
        self.runnes = asyncio.get_event_loop()

#======================================================================================================

    def download(self, link, command, progress):
        with YoutubeDL(command) as ydl:
            try:
                filelink = [link]
                ydl.add_progress_hook(progress)
                ydl.download(filelink)
            except DownloadError as erros:
                self.errors = erros
                self.status = False
            except Exception as erros:
                self.errors = erros
                self.status = False

            return self.status

#======================================================================================================
    
    async def metadata(self, link, command):
        with YoutubeDL(command) as ydl:
            self.result = ydl.extract_info(link, download=False)
            return self.result

#======================================================================================================

    async def extinfos(self, link, command):
        with YoutubeDL(command) as ydl:
            try:
                self.result = ydl.extract_info(link, download=False)
            except Exception as erros:
                self.errors = erros

            return self.result

#======================================================================================================

    async def filename(self, link, command):
        with YoutubeDL(command) as ydl:
            try:
                masteredata = await self.metadata(link, command)
                self.fnames = ydl.prepare_filename(masteredata, outtmpl=self.downdl)
            except Exception:
                self.fnames = None

            return self.fnames

#======================================================================================================

    async def start(self, link, command, progress):
        mainou = await self.runnes.run_in_executor(None, self.download, link, command, progress)
        return mainou

#======================================================================================================

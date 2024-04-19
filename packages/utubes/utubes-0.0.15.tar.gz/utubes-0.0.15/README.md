<p align="center">
 📦 <a href="https://pypi.org/project/utubes" style="text-decoration:none;">YOUTUBE EXTENSIONS</a>
</p>


## USAGE
```python
async def main():
    # EXAMPLE USAGE OF METHODS
    filelink = "YOUR_VIDEO_LINK"
    progress = None # YOUR PROGRESS HOOK FUNCTION
    commands = {"quiet": True, "no_warnings": True}

    # CALL METHODS USING AWAIT
    metadata_result = await UDownloader.metadata(filelink, commands)
    extinfos_result = await UDownloader.extracts(filelink, commands)
    filename_result = await UDownloader.filename(filelink, commands)
    download_result = await UDownloader.download(filelink, commands, progress)
    print(metadata_result.result) # metadata_result.errors
    print(extinfos_result.result) # extinfos_result.errors
    print(filename_result.result) # filename_result.errors
    print(download_result.status) # download_result.errors
    # DO SOMETHING WITH THE RESULTS

asyncio.run(main())
```

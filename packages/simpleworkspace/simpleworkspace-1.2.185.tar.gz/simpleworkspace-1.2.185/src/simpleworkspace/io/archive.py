import os as _os


class GZIP:
    @staticmethod
    def Compress(inputPath: str, outputPath: str = None):
        """Compresses one file to a GZIP archive

        :param inputPath: filepath to compress
        :param outputPath: desired full output path, by default adds format suffix to inputpath
        :return: the path to the compressed archive
        """
        import gzip

        if outputPath is None:
            outputPath = inputPath + ".gz"
        with open(inputPath, mode="rb") as f_in:
            with gzip.open(outputPath, mode="wb") as f_out:
                f_out.writelines(f_in)
        return outputPath

    @staticmethod
    def Extract(inputPath: str, outputPath: str = None):
        """Extracts one file to a GZIP archive

        :param inputPath: filepath to extract
        :param outputPath: desired full output path, by default removes format suffix from inputpath
        :return: the path to the extracted content
        """
        import gzip

        if outputPath is None:
            outputPath = inputPath.removesuffix(".gz")
        with gzip.open(inputPath, mode="rb") as f_in:
            with open(outputPath, mode="wb") as f_out:
                f_out.writelines(f_in)
        return outputPath


class TAR:
    @staticmethod
    def Compress(inputPath: str, outputPath: str = None, pipe_gz=True, ignoreErrors=False):
        """Compresses file or folder to TAR or Tar+GZIP archive

        :param inputPath: file or folder path to compress
        :param outputPath: desired full output path, by default adds format suffix to inputpath
        :param pipe_gz: If enabled, appends GZIP compression on top of the TAR archive which by itself is uncompressed.
        :param ignoreErrors: continue compressing next entry when encountering errors
        :return: the path to the compressed archive
        """
        import tarfile

        archiveType = ".tar.gz" if pipe_gz else ".tar"
        mode = "w:gz" if pipe_gz else "w"

        if outputPath is None:
            outputPath = inputPath + archiveType

        with tarfile.open(outputPath, mode=mode) as tar:
            try:
                if _os.path.isfile(inputPath):
                    tar.add(inputPath, arcname=_os.path.basename(inputPath))
                elif _os.path.isdir(inputPath):
                    for root, dirs, files in _os.walk(inputPath):
                        for file in files:
                            currentFilePath = _os.path.join(root, file)
                            tar.add(currentFilePath, arcname=_os.path.relpath(currentFilePath, inputPath))
            except Exception as ex:
                if not ignoreErrors:
                    raise ex
        return outputPath

    @staticmethod
    def Extract(inputPath: str, outputPath: str = None):
        """Extracts TAR or TAR+GZIP archive

        :param inputPath: filepath to extract
        :param outputPath: desired full output path, by default removes format suffix from inputpath
        :return: the path to the extracted content
        """
        import tarfile

        def GetType(archivePath: str):
            validExt = (".tar", ".tar.gz", ".tgz")
            for ext in validExt:
                if archivePath.endswith(ext):
                    return ext
            raise NameError(f"File extension is not recognized, expected {validExt}")

        archiveType = GetType(inputPath)

        if outputPath is None:
            outputPath = inputPath.removesuffix(archiveType)

        mode = "r" if archiveType == ".tar" else "r:gz"
        with tarfile.open(inputPath, mode=mode) as tar:
            tar.extractall(outputPath)
        return outputPath

    @classmethod
    def _GetArchiveExtension(cls, archivePath: str):
        validExt = (".tar", ".tar.gz", ".tgz")
        for ext in validExt:
            if archivePath.endswith(ext):
                return ext
        raise NameError(f"File extension is not recognized, expected {validExt}")


class ZIP:
    @staticmethod
    def Compress(inputPath: str, outputPath: str = None, compressionLevel: int = None, ignoreErrors=False):
        """Compresses file or folder to zip archive

        :param inputPath: file or folder path to compress
        :param outputPath: desired full output path, by default adds format suffix to inputpath
        :param compressionLevel: 0-9, where 0 uses no compression(only stores files), and 9 has max compression. \
                                 When None is supplied use default in zlib(usually 6)
        :param ignoreErrors: continue compressing next entry when encountering errors
        :return: the path to the compressed archive
        """
        import zipfile

        if outputPath is None:
            outputPath = inputPath + ".zip"
        compressionType = zipfile.ZIP_DEFLATED
        if (compressionLevel is not None) and (compressionLevel < 1):
            compressionType = zipfile.ZIP_STORED  # use no compression
            compressionLevel = None
        with zipfile.ZipFile(outputPath, mode="w", compression=compressionType, compresslevel=compressionLevel) as zipf:
            try:
                if _os.path.isfile(inputPath):
                    zipf.write(inputPath, arcname=_os.path.basename(inputPath))
                elif _os.path.isdir(inputPath):
                    for root, dirs, files in _os.walk(inputPath):
                        for file in files:
                            currentFilePath = _os.path.join(root, file)
                            zipf.write(currentFilePath, arcname=_os.path.relpath(currentFilePath, inputPath))
            except Exception as ex:
                if not ignoreErrors:
                    raise ex
        return outputPath

    @staticmethod
    def Extract(inputPath: str, outputPath: str = None):
        """Extracts ZIP archive

        :param inputPath: filepath to extract
        :param outputPath: desired full output path, by default removes format suffix from inputpath
        :return: the path to the extracted content
        """
        import zipfile

        if outputPath is None:
            outputPath = inputPath.removesuffix(".zip")
        with zipfile.ZipFile(inputPath, mode="r") as zipf:
            zipf.extractall(outputPath)
        return outputPath


class SevenZip:
    @staticmethod
    def Compress(inputPath: str, outputPath: str = None, useCompression=True, password: str = None, ignoreErrors=False):
        """Compresses file or folder to zip archive

        :param inputPath: file or folder path to compress
        :param outputPath: desired full output path, by default adds format suffix to inputpath
        :param useCompression: If false, use copy mode to store files without compression
        :param password: When password is supplied, encrypts the archive
        :param ignoreErrors: continue compressing next entry when encountering errors
        :return: the path to the compressed archive
        """
        import py7zr  # pip install py7zr

        if outputPath is None:
            outputPath = inputPath + ".7z"

        filters = None if useCompression else [{"id": py7zr.FILTER_COPY}]
        if(filters is not None) and (password is not None):
            #special scenario / issue for this lib: 
            #   When a custom filter is specified, it completely overrides all default filters, we therefore have to
            #   manually specify for example that we want encryption filter when filters are overriden and a password is set  
            filters.append({"id": py7zr.FILTER_CRYPTO_AES256_SHA256})
    
        useHeaderEncryption = password is not None
        with py7zr.SevenZipFile(outputPath, mode="w", filters=filters, password=password, header_encryption=useHeaderEncryption) as zipf:
            try:
                if _os.path.isfile(inputPath):
                    zipf.write(inputPath, arcname=_os.path.basename(inputPath))
                elif _os.path.isdir(inputPath):
                    for root, dirs, files in _os.walk(inputPath):
                        for file in files:
                            currentFilePath = _os.path.join(root, file)
                            zipf.write(currentFilePath, arcname=_os.path.relpath(currentFilePath, inputPath))
            except Exception as ex:
                if not ignoreErrors:
                    raise ex
        return outputPath

    @staticmethod
    def Extract(inputPath: str, outputPath: str = None, password: str = None):
        """Extracts ZIP archive

        :param inputPath: filepath to extract
        :param outputPath: desired full output path, by default removes format suffix from inputpath
        :return: the path to the extracted content
        """
        import py7zr  # pip install py7zr

        if outputPath is None:
            outputPath = inputPath.removesuffix(".7z")

        with py7zr.SevenZipFile(inputPath, mode="r", password=password) as archive:
            archive.extractall(outputPath)
        return outputPath

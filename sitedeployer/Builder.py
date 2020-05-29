import logging

logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
formatter = logging.Formatter("[deployer] - %(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
handler.setLevel(logging.DEBUG)
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

from sitedeployer._Sitetask.Sitetask import *



class Builder(
    Sitetask
):
    @classmethod
    def from_PATHFILE_deploypy(cls,
        PATHFILE_deploypy:Path=None
    ):
        result = cls(
            PATHFILE_deploypy=PATHFILE_deploypy
        )
        return result

    def __init__(self,
        PATHFILE_deploypy:Path=None
    ):
        Sitetask.__init__(self,
            PATHFILE_deploypy=PATHFILE_deploypy
        )

    def pythonanywhere_username(self) -> str:
        return 'ynsbuilder'

    def Build(self) -> None:
        self.log_environment()

        logger.info('Build and Upload projects...')

        for projekt in self.projekts_all():
            projekt.upload_on_pypi()

        logger.info('Builded and Uploaded projects!')

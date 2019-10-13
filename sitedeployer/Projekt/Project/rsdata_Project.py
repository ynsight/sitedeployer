from pathlib import Path
from typing import List

from sitedeployer.Projekt.Project._Project.Project import Project


class rsdata_Project(
    Project
):
    def NAME(self) -> str:
        return 'rsdata'
    
    def pythonanywhere_username(self) -> str:
        return 'getrsdata'

    def github_url_type(self) -> str:
        return 'ssh'

    def version_list(self) -> List[int]:
        return [2019, 2, 0]

    def is_uninstall_as_package_supported(self) -> bool:
        return False

    def package_executables(self) -> List[str]:
        return []


    def PATHDIRS_packages_to_upload_to_testpypi(self) -> List[Path]:
        return [

        ]
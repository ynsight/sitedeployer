from pathlib import Path
from typing import Type, List

from sitedeployer.projects.core.Projektproject import Projektproject, logger

class Ln_Projektproject(
    Projektproject
):
    def NAME(self) -> str:
        return 'Ln'
    
    def pythonanywhere_username(self) -> str:
        return 'getln'

    def github_url_type(self) -> str:
        return 'ssh'

    def dependencies_lib_temp_Types(self) -> List[Type[Projektproject]]:
        from sitedeployer.projects.builtin.projekt.base_Projektproject import base_Projektproject
        from sitedeployer.projects.builtin.projekt.projekt_Projektproject import projekt_Projektproject
        from sitedeployer.projects.builtin.projekt.myrta_Projektproject import myrta_Projektproject
        return [
            base_Projektproject,
            projekt_Projektproject,
            myrta_Projektproject
        ]

    def dependencies_lib_deployer_Types(self) -> List[Type[Projektproject]]:
        from sitedeployer.projects.builtin.projekt.base_Projektproject import base_Projektproject
        from sitedeployer.projects.builtin.projekt.projekt_Projektproject import projekt_Projektproject
        from sitedeployer.projects.builtin.projekt.myrta_Projektproject import myrta_Projektproject

        from sitedeployer.projects.builtin.projekt.una_Projektproject import una_Projektproject
        from sitedeployer.projects.builtin.projekt.rs_Projektproject import rs_Projektproject
        from sitedeployer.projects.builtin.projekt.fw_Projektproject import fw_Projektproject
        from sitedeployer.projects.builtin.projekt.sola_Projektproject import sola_Projektproject
        return [
            base_Projektproject,
            projekt_Projektproject,
            myrta_Projektproject,

            una_Projektproject,
            # rs_Projektproject,
            fw_Projektproject,
            # sola_Projektproject,
            # Ln_Projektproject
        ]

    def dependencies_lib_site_Types(self) -> List[Type[Projektproject]]:
        from sitedeployer.projects.builtin.projekt.base_Projektproject import base_Projektproject
        from sitedeployer.projects.builtin.projekt.projekt_Projektproject import projekt_Projektproject
        from sitedeployer.projects.builtin.projekt.myrta_Projektproject import myrta_Projektproject

        from sitedeployer.projects.builtin.projekt.una_Projektproject import una_Projektproject
        from sitedeployer.projects.builtin.projekt.rs_Projektproject import rs_Projektproject
        from sitedeployer.projects.builtin.projekt.fw_Projektproject import fw_Projektproject
        from sitedeployer.projects.builtin.projekt.sola_Projektproject import sola_Projektproject
        return [
            base_Projektproject,
            projekt_Projektproject,
            myrta_Projektproject,

            una_Projektproject,
            # rs_Projektproject,
            fw_Projektproject,
            # sola_Projektproject,
            # Ln_Projektproject
        ]

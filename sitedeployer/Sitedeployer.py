import logging

from sitedeployer.Projekt._Projekt.Projekt import Projekt

logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
formatter = logging.Formatter("[deployer] - %(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
handler.setLevel(logging.DEBUG)
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

from typing import List
import shutil
from pathlib import Path

from sitedeployer.utils import log_environment

class Sitedeployer:
    def __init__(self,
        PATHFILE_deploypy:Path=None,
        target_project:Projekt=None
    ):
        self._PATHFILE_deploypy = PATHFILE_deploypy
        self._target_project = target_project

    # projekt:
    def target_project(self) -> Projekt:
        return self._target_project

    # pythonanywhere:
    def pythonanywhere_username(self) -> str:
        return self.target_project().pythonanywhere_username()

    def URL_pythonanywhere_site(self) -> str:
        return self.pythonanywhere_username() + '.pythonanywhere.com'

    # github:
    def github_username(self) -> str:
        return 'ynsight'

    def python_version_list(self) -> List[int]:
        return [3, 6]

    def python_version_dot_str(self) -> str:
        return '.'.join(self.python_version_list())

    def FILENAME_python(self) -> str:
        return 'python%python_version_dot_str%'\
            .replace('%python_version_dot_str%', self.python_version_dot_str())

    def DIRNAME_venv(self) -> str:
        return 'python%python_version_dot_str%venv'\
            .replace('%python_version_dot_str%', self.python_version_dot_str())

    def DIRNAME_python(self) -> str:
        return 'python%python_version_dot_str%'\
            .replace('%python_version_dot_str%', self.python_version_dot_str())

    def PATHDIR_venvsitepackages(self) -> Path:
        return Path(
            '/home/%pythonanywhere_username%/.virtualenvs/%DIRNAME_venv%/lib/%DIRNAME_python%/site-packages'
                .replace('%pythonanywhere_username%', self.pythonanywhere_username())
                .replace('%DIRNAME_venv%', self.DIRNAME_venv())
                .replace('%DIRNAME_python%', self.DIRNAME_python())
        )

    def PATHDIR_venvbin(self) -> Path:
        return Path(
            '/home/%pythonanywhere_username%/.virtualenvs/%DIRNAME_venv%/bin'
                .replace('%pythonanywhere_username%', self.pythonanywhere_username())
                .replace('%DIRNAME_venv%', self.DIRNAME_venv())
        )

    # PATHS:
    def PATHDIR_home_pythonanywhereusername(self) -> Path:
        return self.PATHDIR_root().parent

    def PATHDIR_root(self) -> Path:
        return self._PATHFILE_deploypy.parent.parent

    def PATHDIR_root_sitedeployer(self) -> Path:
        return self.PATHDIR_root_sitedeployer_sitedeployerpackage().parent

    def PATHDIR_root_sitedeployer_sitedeployerpackage(self) -> Path:
        return self.PATHFILE_root_sitedeployer_sitedeployerpackage_deploypy().parent

    def PATHFILE_root_sitedeployer_sitedeployerpackage_deploypy(self) -> Path:
        return self._PATHFILE_deploypy

    def PATHFILE_wsgipy(self) -> Path:
        return Path(
                '/var/www/%pythonanywhere_username%_pythonanywhere_com_wsgi.py'
                    .replace('%pythonanywhere_username%', self.pythonanywhere_username())
            )

    def PATHFILE_root_sitedeployer_sitedeployerpackage_updatepy(self) -> Path:
        return self.PATHDIR_root_sitedeployer_sitedeployerpackage() / 'update.py'

    def PATHFILE_home_pythonanywhereusername_updatepy(self) -> Path:
        return self.PATHDIR_home_pythonanywhereusername() / 'update.py'


    def Execute(self) -> None:
        dependencies_projects = []
        for project_Type in self.target_project().dependencies_Types():
            if isinstance(self.target_project(), project_Type):
                dependency_project = self.target_project()
            else:
                dependency_project = project_Type()
            dependencies_projects.append(dependency_project)

            dependency_project.attach_to_sitedeployer(
                sitedeployer=self
            )

        self.target_project().attach_to_sitedeployer(
            sitedeployer=self
        )

        log_environment(logger=logger)

        logger.info(
'''# projekt:
target_project: '%target_project%'
dependencies_projects: '%dependencies_projects%'

# pythonanywhere:
pythonanywhere_username: '%pythonanywhere_username%'
URL_pythonanywhere_site: '%URL_pythonanywhere_site%'

# github:
github_username: '%github_username%'

# paths:
PATHDIR_home_pythonanywhereusername: '%PATHDIR_home_pythonanywhereusername%'
PATHDIR_root: '%PATHDIR_root%'
PATHDIR_root_sitedeployer: '%PATHDIR_root_sitedeployer%'
PATHDIR_root_sitedeployer_sitedeployerpackage: '%PATHDIR_root_sitedeployer_sitedeployerpackage%'
PATHFILE_root_sitedeployer_sitedeployerpackage_deploypy: '%PATHFILE_root_sitedeployer_sitedeployerpackage_deploypy%'
PATHFILE_wsgipy: '%PATHFILE_wsgipy%'
PATHFILE_root_sitedeployer_sitedeployerpackage_updatepy: '%PATHFILE_root_sitedeployer_sitedeployerpackage_updatepy%'
PATHFILE_home_pythonanywhereusername_updatepy: '%PATHFILE_home_pythonanywhereusername_updatepy%'
'''
            .replace('%target_project%', str(self.target_project()))
            .replace('%dependencies_projects%', str(dependencies_projects))
            \
            .replace('%pythonanywhere_username%', self.pythonanywhere_username())
            .replace('%URL_pythonanywhere_site%', self.URL_pythonanywhere_site())
            \
            .replace('%github_username%', self.github_username())
            \
            .replace('%PATHDIR_home_pythonanywhereusername%', str(self.PATHDIR_home_pythonanywhereusername()))
            .replace('%PATHDIR_root%', str(self.PATHDIR_root()))
            .replace('%PATHDIR_root_sitedeployer%', str(self.PATHDIR_root_sitedeployer()))
            .replace('%PATHDIR_root_sitedeployer_sitedeployerpackage%', str(self.PATHDIR_root_sitedeployer_sitedeployerpackage()))
            .replace('%PATHFILE_root_sitedeployer_sitedeployerpackage_deploypy%', str(self.PATHFILE_root_sitedeployer_sitedeployerpackage_deploypy()))
            .replace('%PATHFILE_wsgipy%', str(self.PATHFILE_wsgipy()))
            .replace('%PATHFILE_root_sitedeployer_sitedeployerpackage_updatepy%', str(self.PATHFILE_root_sitedeployer_sitedeployerpackage_updatepy()))
            .replace('%PATHFILE_home_pythonanywhereusername_updatepy%', str(self.PATHFILE_home_pythonanywhereusername_updatepy()))
        )

        for dependency_project in dependencies_projects:
            dependency_project.install_as_package()

        self.target_project().install_as_target()

        # wsgi.py:
        logger.info('Process wsgi.py...')
        logger.info(
'''PATHFILE_wsgipy=%PATHFILE_wsgipy%'''
            .replace('%PATHFILE_wsgipy%', str(self.PATHFILE_wsgipy()))
        )

        logger.info('Write wsgi.py file...')
        wsgipy_template = \
'''import sys, os
from pathlib import Path

%project_entry%

from %projektsitepub_package%.flask_app import app as application
'''

        wsgipy_fc = wsgipy_template\
            .replace('%project_entry%', self.target_project().wsgipy_entry())\
            .replace('%projektsitepub_package%', self.target_project().projektsitepub_package())

        self.PATHFILE_wsgipy().write_text(
            wsgipy_fc
        )

        logger.info('WSGIPY_FILE_BEGIN' + wsgipy_fc + 'WSGIPY_FILE_END')
        logger.info('Write wsgi.py file!')
        logger.info('Process wsgi.py!')

        # update.py:
        logger.info('Write update.py file...')
        logger.info(
'''update.py paths:
PATHFILE_root_sitedeployer_sitedeployerpackage_updatepy=%PATHFILE_root_sitedeployer_sitedeployerpackage_updatepy%
PATHFILE_home_pythonanywhereusername_updatepy=%PATHFILE_home_pythonanywhereusername_updatepy%'''
            .replace('%PATHFILE_root_sitedeployer_sitedeployerpackage_updatepy%', str(self.PATHFILE_root_sitedeployer_sitedeployerpackage_updatepy()))
            .replace('%PATHFILE_home_pythonanywhereusername_updatepy%', str(self.PATHFILE_home_pythonanywhereusername_updatepy()))
        )

        shutil.copyfile(
            self.PATHFILE_root_sitedeployer_sitedeployerpackage_updatepy(),
            self.PATHFILE_home_pythonanywhereusername_updatepy()
        )
        logger.info('Write update.py file!')

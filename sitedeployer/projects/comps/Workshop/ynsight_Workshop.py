from sitedeployer.projects.comps.Workshop._Workshop.Workshop import Workshop


class ynsight_Workshop(
    Workshop
):
    def NAME(self) -> str:
        return 'ynsight'

    def pythonanywhere_username(self) -> str:
        return 'ynsight'

    def github_url_type(self) -> str:
        return 'ssh'

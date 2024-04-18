from everai.app.context import Context
from everai.secret import Secret, SecretManager
from everai.volume import Volume, VolumeManager


class AppRuntime:
    secrets: dict[str, Secret]
    volumes: dict[str, Volume]
    volume_manager: VolumeManager
    secret_manager: SecretManager
    is_prepare_mode: bool

    def __init__(self):
        pass

    def context(self) -> Context:
        return Context(
            secrets=self.secrets,
            volumes=self.volumes,
            volume_manager=self.volume_manager,
            is_prepare_mode=self.is_prepare_mode,
        )

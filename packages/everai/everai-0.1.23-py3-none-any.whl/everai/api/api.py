import functools
import typing

from everai.token_manager import TokenManager
from generated.schedulers import (
    ApiClient as SchedulersClient,
    V1App,
    AppServiceCreateBody,
    V1AppServiceSetupImageBody,
    Appsv1SetupImage,
    V1BasicAuth,
    V1ValueFromSecret,
    AppServiceSetupVolumesBody,
    AppServiceApi,
    V1SetupVolume,
    AppServiceSetupSecretsBody,
    AppServiceSetupResourcesBody,
    V1ResourceClaim,
    AppServiceSetupAutoScalingPolicyBody,
    V1AutoscalingPolicy,
    V1BuiltInPolicy,
)

from generated.volumes import (
    ApiClient as VolumesClient,
    Configuration,
    V1Volume,
    V1File,
    VolumeServiceSignUploadBody,
    VolumeServiceCommitFileBody,
    V1Revision,
    VolumeServiceCommitRevisionBody,
    VolumeServiceInitializeMultipartUploadBody,
    VolumeServiceCompleteMultipartUploadBody,
    V1Part,
    VolumeServiceSignMultipartUploadBody,
    V1HeaderValue,
    V1SignUploadResponse,
    V1UploadAction,
    VolumeServiceCommitFileBodyFile,
    VolumeServiceApi,
    VolumeServiceCreateBody
)

from generated.secrets import (
    ApiClient as SecretsClient,
    V1Secret,
    SecretServiceApi,
    SecretServiceCreateBody,
)

from everai.constants import EVERAI_ENDPOINT


class ValueFromSecret:
    secret_name: str
    key: str

    def __init__(self, secret_name: str, key: str):
        self.secret_name = secret_name
        self.key = key


def check_token(func):
    @functools.wraps(func)
    def wrapper(s, *args, **kwargs):
        if s.token is None:
            raise ValueError("token not ready, please login first")
        return func(s, *args, **kwargs)

    return wrapper


class API:
    token: typing.Optional[str]
    volumes_client: VolumesClient
    schedulers_client: SchedulersClient
    secrets_client: SecretsClient

    app_service_api: AppServiceApi
    secret_service_api: SecretServiceApi
    volume_service_api: VolumeServiceApi

    def __init__(self, endpoint: str = None):
        endpoint = endpoint or EVERAI_ENDPOINT
        self.token = TokenManager().get_token()

        self.volumes_client = VolumesClient(
            header_name='Authorization',
            header_value=f'Bearer {self.token}',
            configuration=Configuration(
                host=endpoint,
            ),
        )
        self.volume_service_api = VolumeServiceApi(self.volumes_client)
        
        self.schedulers_client = SchedulersClient(
            header_name='Authorization',
            header_value=f'Bearer {self.token}',
            configuration=Configuration(
                host=endpoint,
            ),
        )
        self.app_service_api = AppServiceApi(self.schedulers_client)
        
        self.secrets_client = SecretsClient(
            header_name='Authorization',
            header_value=f'Bearer {self.token}',
            configuration=Configuration(
                host=endpoint,
            ),
        )
        self.secret_service_api = SecretServiceApi(self.secrets_client)

    def login(self, token: str) -> None:
        # do some check
        TokenManager().set_token(token)

    def create_volume(self, name: str, labels: dict[str, str] = None) -> V1Volume:
        body = VolumeServiceCreateBody()
        body.labels = labels
        v1_volume = self.volume_service_api.create_volume(name, body)
        return v1_volume

    def list_volume_files(self, name: str) -> list[V1File]:
        list_file_resp = self.volume_service_api.list_files(volume_name=name)

        return list_file_resp.files

    # noinspection PyMethodMayBeStatic
    def headers(self, headers: typing.Optional[dict[str, V1HeaderValue]]) -> [dict[str, list[str]]]:
        return {key: value.value for key, value in headers.items()}

    def sign_download(self, name: str, file_path: str) -> tuple[str, str, dict[str, list[str]]]:
        resp = self.volume_service_api.sign_download(volume_name=name, path=file_path)
        assert resp.method is not None
        assert resp.url is not None
        return resp.method, resp.url, self.headers(resp.headers)

    def sign_upload(self, name: str, revision_name: str, file_path: str, file_size: int,
                    file_sha256: str) -> (bool, str, str, dict[str, list[str]]):
        """
        :return:
            bool    True means need upload, False means already uploaded
            str     http method
            str     url
            dict    headers
        """
        body = VolumeServiceSignUploadBody().from_dict({'file': {'size': str(file_size), 'sha256': file_sha256}})
        resp = self.volume_service_api.sign_upload(volume_name=name, revision_name=revision_name,
                                                                 file_path=file_path, body=body)
        return (resp.action == V1UploadAction.UPLOAD, resp.response.method, resp.response.url,
                self.headers(resp.response.headers))

    def create_revision(self, name: str) -> V1Revision:
        return self.volume_service_api.create_revision(volume_name=name)

    def volume_cancel_revision(self, name: str, revision_name: str) -> None:
        self.volume_service_api.cancel_revision(volume_name=name, revision_name=revision_name)

    def commit_revision(self, name: str, revision_name: str, files: list[V1File]) -> None:
        self.volume_service_api.commit_revision(
            volume_name=name,
            revision_name=revision_name,
            body=VolumeServiceCommitRevisionBody(files=files),
        )

    def init_multipart_upload(self, name: str, revision_name: str, file_path: str, file_size: int,
                              file_sha256: str) -> tuple[bool, str]:
        """
        :return:
            bool True means need upload, False means already uploaded
            str Upload ID
        """
        resp = self.volume_service_api.initialize_multipart_upload(
            volume_name=name,
            revision_name=revision_name,
            file_path=file_path,
            body=VolumeServiceInitializeMultipartUploadBody().from_dict(
                {'file': {'size': str(file_size), 'sha256': file_sha256}})
        )

        return resp.action == V1UploadAction.UPLOAD, resp.upload_id

    def cancel_multipart_upload(self, name: str, revision_name: str, upload_id: str) -> None:
        self.volume_service_api.cancel_multipart_upload(
            volume_name=name,
            revision_name=revision_name,
            upload_id=upload_id)

    def complete_multipart_upload(self, name: str, revision_name: str, upload_id: str, parts: list[V1Part],
                                  mime_type: str = None) -> None:
        self.volume_service_api.complete_multipart_upload(
            name,
            revision_name,
            upload_id,
            VolumeServiceCompleteMultipartUploadBody(parts=parts, mime_type=mime_type),
        )

    def list_multipart_upload_parts(self, name: str, revision_name: str, upload_id: str) -> list[V1Part]:
        resp = self.volume_service_api.list_parts(name, revision_name, upload_id)
        return resp.parts

    def sign_multipart_upload(self, name: str, revision_name: str, upload_id: str,
                              part_number: int) -> tuple[str, str, dict[str, list[str]]]:
        resp = self.volume_service_api.sign_multipart_upload(
            name,
            revision_name,
            upload_id,
            VolumeServiceSignMultipartUploadBody(part_number=part_number),
        )
        headers = {key: value.value for (key, value) in resp.headers.items()}
        return resp.method, resp.url, headers

    def commit_file(self, name: str, revision_name: str, file: V1File) -> None:
        self.volume_service_api.commit_file(
            volume_name=name,
            revision_name=revision_name,
            file_path=file.path,
            body=VolumeServiceCommitFileBody(file=VolumeServiceCommitFileBodyFile(
                size=file.size,
                sha256=file.sha256,
                created_at=file.created_at,
                modified_at=file.modified_at,
            ))
        )
        return

    def get_volume(self, name: str) -> V1Volume:
        return self.volume_service_api.get_volume(name)

    def delete_volume(self, name: str) -> None:
        self.volume_service_api.delete_volume(name)

    def list_volumes(self) -> list[V1Volume]:
        resp = self.volume_service_api.list_volume()
        return resp.volumes or []

    def create_secret(self, secret: V1Secret) -> V1Secret:
        resp = self.secret_service_api.create_secret(secret.name, body=SecretServiceCreateBody(
            data=secret.data,
            labels=secret.labels,
        ))
        return resp

    def list_secrets(self) -> list[V1Secret]:
        resp = self.secret_service_api.list_secret()
        return resp.secrets or []

    def get_secret(self, name: str) -> V1Secret:
        resp = self.secret_service_api.get_secret(name)
        return resp

    def delete_secret(self, name: str) -> None:
        self.secret_service_api.delete_secret(name)

    def deploy_app(self, name: str) -> None:
        self.app_service_api.deploy_app(name)

    def get_app(self, name: str) -> V1App:
        return self.app_service_api.get_app(name)

    def delete_app(self, name: str) -> None:
        self.app_service_api.delete_app(name)

    def pause_app(self, name: str) -> None:
        self.app_service_api.pause_app(app_name=name)

    @check_token
    def create_app(self, name: str, route_name: typing.Optional[str] = None) -> V1App:
        return AppServiceApi(self.schedulers_client).create_app(
            app_name=name,
            body=AppServiceCreateBody(
                route_path=route_name or name,
            ),
        )

    def setup_image(self, app_name: str, repository: str, tag: str = None, digest: str = None,
                    username: ValueFromSecret = None, password: ValueFromSecret = None):
        auth: typing.Optional[V1BasicAuth] = None
        if username is not None and password is not None:
            auth = V1BasicAuth(
                username=V1ValueFromSecret(name=username.secret_name, key=username.key),
                password=V1ValueFromSecret(name=password.secret_name, key=password.key),
            )

        self.app_service_api.setup_image(
            app_name=app_name,
            body=V1AppServiceSetupImageBody(
                setup_image=Appsv1SetupImage(
                    repository=repository,
                    tag=tag,
                    digest=digest,
                    basic_auth=auth,
                ),
            ),
        )

    def setup_volume_requests(self, app_name: str, volume_requests: list[V1SetupVolume]):
        assert len(volume_requests) > 0

        self.app_service_api.setup_volumes(app_name=app_name,
                                                         body=AppServiceSetupVolumesBody(setup_volumes=volume_requests))

    def setup_secret_requests(self, app_name: str, secret_requests: list[str]):
        assert len(secret_requests) > 0

        self.app_service_api.setup_secrets(app_name=app_name,
                                                         body=AppServiceSetupSecretsBody(secret_names=secret_requests))

    def setup_resource_requests(self, app_name: str, resource_requests: V1ResourceClaim):
        self.app_service_api.setup_resources(app_name=app_name, body=AppServiceSetupResourcesBody(
            resource_claim=resource_requests
        ))

    def setup_autoscaling_policy(self, app_name: str,
                                 min_workers: int = 1,
                                 max_workers: int = 1,
                                 max_queue_size: int = 9999999999,
                                 max_idle_time: int = 9999999999):
        self.app_service_api.setup_auto_scaling_policy(app_name=app_name,
                                                                     body=AppServiceSetupAutoScalingPolicyBody(
                                                                 auto_scaling_policy=V1AutoscalingPolicy(
                                                                     built_in_policy=V1BuiltInPolicy(
                                                                         min_worker_num=min_workers,
                                                                         max_worker_num=max_workers,
                                                                         max_queue_num=max_queue_size,
                                                                         max_idle_time=max_idle_time,
                                                                     )
                                                                 ),
                                                             ))

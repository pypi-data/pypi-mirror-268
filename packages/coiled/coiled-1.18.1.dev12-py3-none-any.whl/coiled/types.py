from enum import Enum
from logging import getLogger
from pathlib import Path
from typing import BinaryIO, Dict, List, Optional, Tuple, Union

from typing_extensions import Literal, TypedDict
from urllib3.util import parse_url

logger = getLogger("coiled.package_sync")


event_type_list = Literal[
    "add_role_to_profile",
    "attach_gateway_to_router",
    "attach_subnet_to_router",
    "create_vm",
    "create_machine_image",
    "create_scheduler" "create_worker",
    "delete_machine_image",
    "create_fw_rule",
    "create_fw",
    "create_network_cidr",
    "create_subnet",
    "create_network",
    "create_log_sink",
    "create_router",
    "create_iam_role",
    "create_log_bucket",
    "create_storage_bucket",
    "create_instance_profile",
    "check_log_sink_exists",
    "check_or_attach_cloudwatch_policy",
    "delete_vm",
    "delete_route",
    "get_firewall",
    "get_network",
    "get_subnet",
    "get_policy_arn",
    "get_log_group",
    "gcp_instance_create",
    "net_gateways_get_or_create",
    "scale",
]


class CondaPlaceHolder(dict):
    pass


class PackageInfo(TypedDict):
    name: str
    path: Optional[Path]
    source: Literal["pip", "conda"]
    channel_url: Optional[str]
    channel: Optional[str]
    subdir: Optional[str]
    conda_name: Optional[str]
    version: str
    wheel_target: Optional[str]


class PackageSchema(TypedDict):
    name: str
    source: Literal["pip", "conda"]
    channel: Optional[str]
    conda_name: Optional[str]
    client_version: Optional[str]
    specifier: str
    include: bool
    file: Optional[int]


class ResolvedPackageInfo(TypedDict):
    name: str
    source: Literal["pip", "conda"]
    channel: Optional[str]
    conda_name: Optional[str]
    client_version: Optional[str]
    specifier: str
    include: bool
    note: Optional[str]
    error: Optional[str]
    sdist: Optional[BinaryIO]
    md5: Optional[str]


class PackageLevelEnum(int, Enum):
    """
    Package mismatch severity level
    Using a high int so we have room to add extra levels as needed

    Ordering is allow comparison like

    if somelevel >= PackageLevelEnum.STRICT_MATCH:
        <some logic for high or critical levels>
    """

    CRITICAL = 100
    STRICT_MATCH = 75
    WARN = 50
    NONE = 0
    LOOSE = -1
    IGNORE = -2
    MATCH_MINOR = -3


class ApproximatePackageRequest(TypedDict):
    name: str
    priority_override: Optional[PackageLevelEnum]
    python_major_version: str
    python_minor_version: str
    python_patch_version: str
    source: Literal["pip", "conda"]
    channel_url: Optional[str]
    channel: Optional[str]
    subdir: Optional[str]
    conda_name: Optional[str]
    version: str
    wheel_target: Optional[str]


class ApproximatePackageResult(TypedDict):
    name: str
    conda_name: Optional[str]
    specifier: Optional[str]
    include: bool
    note: Optional[str]
    error: Optional[str]
    channel_url: Optional[str]
    client_version: Optional[str]


class PiplessCondaEnvSchema(TypedDict, total=False):
    name: Optional[str]
    channels: List[str]
    dependencies: List[str]


class CondaEnvSchema(TypedDict, total=False):
    name: Optional[str]
    channels: List[str]
    dependencies: List[Union[str, Dict[str, List[str]]]]


class SoftwareEnvSpec(TypedDict):
    packages: List[PackageSchema]
    raw_pip: Optional[List[str]]
    raw_conda: Optional[CondaEnvSchema]


# This function is in this module to prevent circular import issues
def parse_conda_channel(package_name: str, channel: str, subdir: str) -> Tuple[Optional[str], str]:
    """Return a channel and channel_url for a conda package with any extra information removed."""
    # Handle unknown channels
    if channel == "<unknown>":
        logger.warning(f"Channel for {package_name} is unknown, setting to conda-forge")
        channel = "conda-forge"
    # Strip subdir from channel
    if channel.endswith(f"/{subdir}"):
        channel = channel[: -len(f"/{subdir}")]
    # Handle channel urls
    if channel.startswith(("http:", "https:")):
        channel_url = channel
        channel = parse_url(channel).path or ""
        if channel:
            channel = channel.strip("/")
        channel = channel
    # TODO: Actually upload these files to S3
    elif channel.startswith("file:"):
        logger.warning(f"Channel for {package_name} is a local file, which is not currently supported")
        channel_url = channel
        channel = channel
    else:
        domain = "repo.anaconda.com" if channel.startswith("pkgs/") else "conda.anaconda.org"
        channel_url = f"https://{domain}/{channel}"
        channel = channel
    return (channel or None), channel_url


class CondaPackage:
    def __init__(self, meta_json: Dict, prefix: Path):
        self.prefix = prefix
        self.name: str = meta_json["name"]
        self.version: str = meta_json["version"]
        self.subdir: str = meta_json["subdir"]
        self.files: str = meta_json["files"]
        self.depends: List[str] = meta_json.get("depends", [])
        self.constrains: List[str] = meta_json.get("constrains", [])
        self.channel, self.channel_url = parse_conda_channel(self.name, meta_json["channel"], self.subdir)

    def __repr__(self):
        return (
            f"CondaPackage(meta_json={{'name': {self.name!r}, 'version': "
            f"{self.version!r}, 'subdir': {self.subdir!r}, 'files': {self.files!r}, "
            f"'depends': {self.depends!r}, 'constrains': {self.constrains!r}, "
            f"'channel': {self.channel!r}}}, prefix={self.prefix!r})"
        )

    def __str__(self):
        return f"{self.name} {self.version} from {self.channel_url}"


class PackageLevel(TypedDict):
    name: str
    level: PackageLevelEnum
    source: Literal["pip", "conda"]


class ApiBase(TypedDict):
    id: int
    created: str
    updated: str


class SoftwareEnvironmentBuild(ApiBase):
    state: Literal["built", "building", "error", "queued"]


class SoftwareEnvironmentSpec(ApiBase):
    latest_build: Optional[SoftwareEnvironmentBuild]


class SoftwareEnvironmentAlias(ApiBase):
    name: str
    latest_spec: Optional[SoftwareEnvironmentSpec]


class ArchitectureTypesEnum(str, Enum):
    """
    All currently supported architecture types
    """

    X86_64 = "x86_64"
    ARM64 = "aarch64"

    def __str__(self) -> str:
        return self.value

    @property
    def conda_suffix(self) -> str:
        if self == ArchitectureTypesEnum.X86_64:
            return "64"
        else:
            return self.value

    @property
    def vm_arch(self) -> Literal["x86_64", "arm64"]:
        if self == ArchitectureTypesEnum.ARM64:
            return "arm64"
        else:
            return self.value


class ClusterDetailsState(TypedDict):
    state: str
    reason: str
    updated: str


class ClusterDetailsProcess(TypedDict):
    created: str
    name: str
    current_state: ClusterDetailsState
    instance: dict


class ClusterDetails(TypedDict):
    id: int
    name: str
    workers: List[ClusterDetailsProcess]
    scheduler: Optional[ClusterDetailsProcess]
    current_state: ClusterDetailsState
    created: str


class FirewallOptions(TypedDict):
    """
    A dictionary with the following key/value pairs

    Parameters
    ----------
    ports
        List of ports to open to cidr on the scheduler.
        For example, ``[22, 8786]`` opens port 22 for SSH and 8786 for client to Dask connection.
    cidr
        CIDR block from which to allow access. For example ``0.0.0.0/0`` allows access from any IP address.
    """

    ports: List[int]
    cidr: str


class BackendOptions(TypedDict, total=False):
    """
    A dictionary with the following key/value pairs

    Parameters
    ----------
    region_name
        Region name to launch cluster in. For example: us-east-2
    zone_name
        Zone name to launch cluster in. For example: us-east-2a
    firewall
        Deprecated; use ``ingress`` instead.
    ingress
        Allows you to specify multiple CIDR blocks (and corresponding ports) to open for ingress
        on the scheduler firewall.
    spot
        Whether to request spot instances.
    spot_on_demand_fallback
        If requesting spot, whether to request non-spot instances if we get fewer spot instances
        than desired.
    spot_replacement
        By default we'll attempt to replace interrupted spot instances; set to False to disable.
    multizone
        Tell the cloud provider to pick zone with best availability, we'll keep workers all in the
        same zone, scheduler may or may not be in that zone as well.
    use_dashboard_public_ip
        Public IP is used by default, lets you choose to use private IP for dashboard link.
    use_dashboard_https
        When public IP address is used for dashboard, we'll enable HTTPS + auth by default.
        You may want to disable this if using something that needs to connect directly to
        the scheduler dashboard without authentication, such as jupyter dask-labextension.
    network_volumes
        Very experimental option to allow mounting SMB volume on cluster nodes.
    docker_shm_size
        Non-default value for shm_size.
    """

    region_name: Optional[str]
    zone_name: Optional[str]
    firewall: Optional[FirewallOptions]  # TODO deprecate, use ingress instead
    ingress: Optional[List[FirewallOptions]]
    spot: Optional[bool]
    spot_on_demand_fallback: Optional[bool]
    spot_replacement: Optional[bool]
    multizone: Optional[bool]
    use_dashboard_public_ip: Optional[bool]
    use_dashboard_https: Optional[bool]
    send_prometheus_metrics: Optional[bool]  # TODO deprecate
    prometheus_write: Optional[dict]  # TODO deprecate
    network_volumes: Optional[List[dict]]
    docker_shm_size: Optional[str]


class AWSOptions(BackendOptions, total=False):
    """
    A dictionary with the following key/value pairs plus any pairs in :py:class:`BackendOptions`

    Parameters
    ----------
    keypair_name
        AWS Keypair to assign worker/scheduler instances. This would need to be an existing keypair in your
            account, and needs to be in the same region as your cluster. Note that Coiled can also manage
            adding a unique, ephemeral keypair for SSH access to your cluster;
            see :doc:`ssh` for more information.
    use_placement_group
        If possible, this will attempt to put workers in the same cluster placement group (in theory this can
        result in better network between workers, since they'd be physically close to each other in datacenter,
        though we haven't seen this to have much benefit in practice).
    """

    keypair_name: Optional[str]
    use_placement_group: Optional[bool]


class GCPOptions(BackendOptions, total=False):
    """
    A dictionary with GCP specific key/value pairs plus any pairs in :py:class:`BackendOptions`
    """

    scheduler_accelerator_count: Optional[int]
    scheduler_accelerator_type: Optional[str]
    worker_accelerator_count: Optional[int]
    worker_accelerator_type: Optional[str]

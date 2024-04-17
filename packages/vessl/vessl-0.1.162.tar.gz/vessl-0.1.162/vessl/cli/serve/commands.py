"""
Serving command definition and delegation.
"""

import json
import os
import sys
import time
from typing import List, Optional, TextIO

import click
import yaml

from openapi_client import V1Autoscaling
from openapi_client.models import (
    ResponseModelServiceInfo,
    secret_upsert_generic_secret_api_input,
)
from openapi_client.models.response_kernel_cluster import ResponseKernelCluster
from openapi_client.models.v1_autoscaling import V1Autoscaling
from openapi_client.models.v1_auxiliary_form import V1AuxiliaryForm
from openapi_client.models.v1_command import V1Command
from openapi_client.models.v1_env_form import V1EnvForm
from openapi_client.models.v1_import_form import V1ImportForm
from openapi_client.models.v1_model_ref_form import V1ModelRefForm
from openapi_client.models.v1_port_path import V1PortPath
from openapi_client.models.v1_resources_form import V1ResourcesForm
from openapi_client.models.v1_serve_revision_service_form import (
    V1ServeRevisionServiceForm,
)
from vessl import vessl_api
from vessl.cli._base import VesslCommand, VesslGroup, vessl_argument, vessl_option
from vessl.cli._util import (
    print_data,
    print_debug,
    print_error,
    print_error_result,
    print_info,
    print_success,
    print_table_tabulate,
    prompt_checkbox,
    prompt_choices,
    prompt_confirm,
    prompt_text,
)
from vessl.cli.serve.util import print_gateway, print_revision
from vessl.internal.vessl_model import VesslModel
from vessl.kernel_cluster import list_cluster_presets
from vessl.organization import _get_organization_name
from vessl.secret import list_generic_secrets
from vessl.serving import (
    _wait_for_gateway_enabled,
    _wait_for_revision_to_launch,
    abort_in_progress_rollout,
    abort_in_progress_rollout_by_name,
    create_active_revision_replacement_rollout,
    create_revision_from_yaml,
    get_recent_rollout,
    launch_revision,
    list_revisions,
    list_services,
    read_gateway,
    read_revision,
    terminate_revision,
    update_model_service,
    update_revision_autoscaler_config,
)
from vessl.util.constant import (
    VESSL_SERVICE_TENSORFLOW_BASE_IMAGE_TEMPLATE,
    VESSL_SERVICE_TORCH_BASE_IMAGE_TEMPLATE,
)
from vessl.util.exception import VesslApiException

from .command_options import format_option, service_name_option

cli = VesslGroup("serve")


@cli.command("list", cls=VesslCommand)
def serving_list():
    """
    List servings in current organization.
    """
    servings: List[ResponseModelServiceInfo] = list_services(
        organization=vessl_api.organization.name
    ).results

    print(f"{len(servings)} serving(s) found.\n")
    for serving in servings:
        kernel_cluster: ResponseKernelCluster = serving.kernel_cluster
        status: str = serving.status  # "ready", "running", "error"

        print(f"{serving.name} (cluster {kernel_cluster.name}): status {status.capitalize()}")


@cli.group("revision")
def cli_revision():
    """
    Root command for revision-related commands.
    """
    pass


@cli.command("abort-update", cls=VesslCommand)
@service_name_option
def abort_update(service: ResponseModelServiceInfo):
    """
    Abort the current revision update.
    """
    try:
        abort_in_progress_rollout(service=service)
    except VesslApiException as e:
        print(f"Failed to abort the service update: {e.message}")
        sys.exit(1)


@cli.command("create", cls=VesslCommand)
@click.option(
    "-f",
    "--file",
    type=click.File("r"),
    required=True,
    help="Path to YAML file for service revision definition.",
)
@click.option(
    "-y",
    "--no-prompt",
    type=click.BOOL,
    is_flag=True,
    help="do not ask anything while creating revision"
)
@click.option(
    "-l",
    "--launch",
    type=click.BOOL,
    is_flag=True,
    help="Launch after creating revision.",
)
@click.option(
    "-a",
    "--set-current-active",
    type=click.BOOL,
    is_flag=True,
    help="Launch and send traffic to the created revision. If another live revision exists, replace the existing revision.",
)
@click.option(
    "--force",
    type=click.BOOL,
    is_flag=True,
    help="force to abort the existing rollout.",
)
def revision_create_with_yaml(
    file: TextIO,
    no_prompt: bool,
    launch: bool,
    set_current_active: bool,
    force: bool,
):
    yaml_body = file.read()
    try:
        yaml_loaded = yaml.safe_load(yaml_body)
    except yaml.YAMLError as e:
        print(f"Error: invalid YAML\n{e}")
        sys.exit(1)

    service_name = yaml_loaded["name"]
    max_timeout = 8 * 60  # sec

    ## Check if the service is already rolling out
    ongoing_rollout_exists = False
    try:
        recent_rollout = get_recent_rollout(service_name)
        if recent_rollout and recent_rollout.status == "rolling_out":
            ongoing_rollout_exists = True
            print_error(f"Error: the service {service_name} is currently rolling out.")
            if not force:
                print_error("Use --force option to abort the existing rollout.")
                sys.exit(1)
    except VesslApiException as e:
        print_debug("No existing rollout found.")
        pass

    ## Abort the existing rollout if --force
    if ongoing_rollout_exists and force:
        if abort_in_progress_rollout_by_name(service_name):
            print_info("Waiting for the existing rollout to be aborted...")
            time.sleep(30)
        
    ## create revision
    try:
        revision = create_revision_from_yaml(
            organization=vessl_api.organization.name, yaml_body=yaml_body
        )
    except VesslApiException as e:
        if e.status == 400:
            print_error("Error: failed to create revision (invalid parameters).")
            print_error_result(e.message)
        else:
            print_error("Error: failed to create revision. (internal error).")
        sys.exit(1)


    ## launch or set-active
    if set_current_active:
        launch = True
    if not launch and not no_prompt:
        launch = prompt_confirm("Do you want to launch this revision immediately?")
    if launch:
        if not set_current_active and not no_prompt:
            set_current_active = prompt_confirm("Do you want to replace the current open-to-public revision?")

    try:
        if set_current_active:
            create_active_revision_replacement_rollout(
                organization=vessl_api.organization.name,
                model_service_name=revision.model_service_name,
                desired_active_revisions_to_weight_map={revision.number: 100},
            )
        elif launch:
            launch_revision(
                organization=vessl_api.organization.name,
                service_name=revision.model_service_name,
                revision_number=revision.number,
            )
        print_info("Successfully triggered revision launch.")
        if not no_prompt:
            _wait_for_revision_to_launch(service_name=service_name, revision_number=revision.number, print_output=True)
        revision = read_revision(
            organization=vessl_api.organization.name,
            service_name=revision.model_service_name,
            revision_number=revision.number,
        )
        print_revision(revision)
        
    except VesslApiException as e:
        print_error("Error: failed to launch revision.")
        print_error_result(e.message)
        sys.exit(1)

    ## Wait for the gateway to be enabled
    if set_current_active:
        gateway = read_gateway(
            organization=vessl_api.organization.name,
            service_name=revision.model_service_name,
        )
        if not no_prompt:
            _wait_for_gateway_enabled(gateway=gateway, service_name=revision.model_service_name, print_output=True)

        print_info("Endpoint is enabled.")
        gateway = read_gateway(
                organization=vessl_api.organization.name,
                service_name=service_name,
            )
        print_gateway(gateway)
        print_info(f"You can test your service via {gateway.endpoint}")


@cli_revision.command("show", cls=VesslCommand)
@service_name_option
@click.option("--number", "-n", required=True, type=int, help="Number of revision.")
@format_option
def revision_show(service: ResponseModelServiceInfo, number: int, format: str):
    """
    Show current status and information about a service revision.
    """
    try:
        revision = read_revision(
            organization=vessl_api.organization.name,
            service_name=service.name,
            revision_number=number,
        )
    except VesslApiException as e:
        print(f"Failed to read revision #{number} of service {service.name}: {e.message}")
        sys.exit(1)

    if format == "json":
        print(json.dumps(revision.to_dict(), default=str))
    else:
        print_revision(revision, verbose=True)


@cli_revision.command("list", cls=VesslCommand)
@service_name_option
@format_option
def revision_list(service: ResponseModelServiceInfo, format: str):
    """
    List all revisions.
    """
    try:
        revisions = list_revisions(
            organization=vessl_api.organization.name,
            service_name=service.name,
        )
    except VesslApiException as e:
        print(f"Failed to list revisions of serving {service.name}: {e.message}")
        sys.exit(1)

    if format == "json":
        print(json.dumps([r.to_dict() for r in revisions], default=str))
    else:
        print(f"{len(revisions)} revision(s) found.\n")
        for i, revision in enumerate(revisions):
            if i > 0:
                print()
            print_revision(revision)


@cli_revision.command("terminate", cls=VesslCommand)
@service_name_option
@click.option("--number", "-n", required=True, type=int, help="Number of revision.")
def revision_terminate(service: ResponseModelServiceInfo, number: int):
    """
    Terminate specified revision.
    """
    try:
        terminate_revision(
            organization=vessl_api.organization.name,
            service_name=service.name,
            revision_number=number,
        )
        print("Successfully terminated revision.")
    except VesslApiException as e:
        print(f"Failed to terminate revision #{number} of serving {service.name}: {e.message}")
        sys.exit(1)


@cli_revision.command("scale", cls=VesslCommand)
@service_name_option
@click.option("--number", "-n", required=True, type=int, help="Number of revision.")
@click.option("--min", required=False, type=int, help="Number of min replicas.")
@click.option("--max", required=False, type=int, help="Number of max replicas.")
@click.option("--target", required=False, type=int, help="Target resource utilization.")
@click.option("--metric", required=False, type=str, help="Metric for autoscaling.")
def revision_update_autoscaler_config(
    service: ResponseModelServiceInfo,
    number: int,
    min: Optional[int],
    max: Optional[int],
    target: Optional[int],
    metric: Optional[str],
):
    """
    Update revision's autoscaler config
    """
    try:
        current_revision = read_revision(
            organization=vessl_api.organization.name,
            service_name=service.name,
            revision_number=number,
        )

        conf: V1Autoscaling = current_revision.revision_spec.autoscaling
        if conf is None:
            conf = V1Autoscaling(
                min=1,
                max=1,
                metric="cpu",
                target=60,
            )
        if min is not None:
            conf.min = min
        if max is not None:
            conf.max = max
        if target is not None:
            conf.target = target
        if metric is not None:
            conf.metric = metric

        update_revision_autoscaler_config(
            organization=vessl_api.organization.name,
            service_name=service.name,
            revision_number=number,
            autoscaling=conf,
        )
        print("Successfully updated autoscaler config.")
    except VesslApiException as e:
        print(
            f"Failed to update autoscaler config of revision #{number} of serving {service.name}: {e.message}"
        )
        sys.exit(1)


@cli.group("gateway")
def cli_gateway():
    """
    Root command for gateway-related commands.
    """
    pass


@cli_gateway.command("show", cls=VesslCommand)
@service_name_option
@format_option
def gateway_show(service: ResponseModelServiceInfo, format: str):
    """
    Show current status of the gateway of a serving.
    """
    try:
        gateway = read_gateway(
            organization=vessl_api.organization.name,
            service_name=service.name,
        )
    except VesslApiException as e:
        print(f"Failed to read gateway of serving {service.name}: {e.message}")
        sys.exit(1)

    if format == "json":
        print(json.dumps(gateway.to_dict(), default=str))
    else:
        print_gateway(gateway)


@cli.command("update", cls=VesslCommand)
@click.option(
    "--number",
    "-n",
    required=False,
    type=int,
    multiple=True,
    help="Number of revisions to launch."
)
@click.option(
    "--weight",
    "-w",
    required=False,
    type=int,
    multiple=True,
    help="Number of traffic weight for the revision",
)
@click.option(
    "--interactive",
    is_flag=True,
    type=click.BOOL,
    help="Update service interactively"
)
@service_name_option
def update(service: ResponseModelServiceInfo, number: List[int], weight: List[int], interactive: bool):
    # TODO(seokju) revisit later
    if not interactive:
        update_model_service(service, number, weight)
        return

    """
    Current Gateway
    """
    gateway_current = read_gateway(
        organization=vessl_api.organization.name, service_name=service.name
    )
    print_info(f"Current Endpoint Host: {gateway_current.endpoint}")
    print_info("Traffic Rules")
    if gateway_current.rules:
        current_rules = [
            {
                "Revision Number": i.revision_number,
                "Traffic Weight": f'{i.traffic_weight}%',
            }
            for i in gateway_current.rules
        ]
        print_table_tabulate(current_rules)

    """
    Current Revisions Status
    """
    revisions = list_revisions(organization=vessl_api.organization.name, service_name=service.name)
    revision_data = [
        {
            "Revision Number": revision.number,
            "Min Replicas": revision.revision_spec.autoscaling.min if revision.revision_spec.autoscaling else "N/A",
            "Max Replicas": revision.revision_spec.autoscaling.max if revision.revision_spec.autoscaling else "N/A",
            "Status": revision.status,
        }
        for revision in revisions
    ]
    print_info(f"Current Revisions")
    print_table_tabulate(revision_data)

    """
    Get Rollout Spec
    """
    target_revisions = []
    while True:
        weights = []
        print_info("Rollout Target")
        target_revisions_result = prompt_checkbox(
            "Choose revisions to launch",
            [f"Revision {rev.number}: {rev.message}" for rev in revisions],
        )
        if len(target_revisions_result) == 0:
            print_error("Please select at least one revision.")
            continue
        target_revisions = ([
            {
                'number': int(rev_summary.split(":")[0].split(" ")[1]),
                'message': ':'.join(rev_summary.split(":")[1:]).strip()
            } for rev_summary in target_revisions_result
        ])
        target_revisions.sort(key=lambda x: x['number'])
        weights = []
        for i, revision in enumerate(target_revisions):
            if i == len(target_revisions) - 1:
                remaining_weight = 100 - sum(weights)
                print_info(f"Last revision will take the rest of the traffic.({remaining_weight}%)")
                weights.append(remaining_weight)
            else:
                while True:
                    w = prompt_text(f"How much traffic should revision {revision['number']} receive?(in percentage)")
                    if not w.isdigit():
                        print_error("Please type an integer between 0 and 100.")
                    elif int(w) > 100 or int(w) < 0:
                        print_error("Please type an integer between 0 and 100.")
                    elif sum(weights) + int(w) > 100:
                        print_error("Total weight should not exceed 100.")
                    else:
                        weights.append(int(w))
                        break

        print_table_tabulate(
            [
                {
                    "Revision Number": revision['number'],
                    "Message": revision['message'],
                    "Traffic Weight": f'{weight}%',
                } for revision, weight in zip(target_revisions, weights)
            ],
        )
        if prompt_confirm("Do you want to proceed as above?"):
            break
    update_model_service(service, [r['number'] for r in target_revisions], weights)


@cli.command("create-yaml", cls=VesslCommand, help="Create a service.yaml file with .vessl.model.lock file")
@vessl_argument("service_name", type=str)
@vessl_argument("message", type=str)
@vessl_option("-k","--api-key", "use_api_key", type=bool, is_flag=True)
def create_yaml(
    service_name: str,
    message: str,
    use_api_key: bool = False,
):
    organization_name = _get_organization_name()

    lockfile_path = ".vessl.model.lock"
    lockfile = VesslModel.from_lockfile(lockfile_path)
    if lockfile is None:
        print_error("The lockfile is not found.")
        return

    try:
        msr = vessl_api.model_service_read_api(
            organization_name=organization_name,
            model_service_name=service_name,
        )
    except Exception as e:
        if e.status == 404:
            print_error(f"Model service {service_name} not found. You should first create a service.")
            return
        print_error(f"Failed to read model service: {e}")
        return

    print_info(f"Service name of {service_name} found.")

    # clusters = list_clusters()
    # cluster_name = prompt_choices("Cluster", [x.name for x in clusters])
    # cluster = list(filter(lambda x: x.name == cluster_name, clusters))[0]
    cluster = msr.kernel_cluster
    print_info(f"Using {cluster.name} cluster configured by the service.")

    presets = list_cluster_presets(cluster.id)
    preset_name = prompt_choices("Preset", [x.name for x in presets])
    preset = list(filter(lambda x: x.name == preset_name, presets))[0]

    secret_name = None
    if use_api_key:
        print_info("Select API key for authentication.")
        secrets = list_generic_secrets()
        if len(secrets) == 0:
            print_info("No secrets registered.")
            if prompt_confirm("Do you want to create a new secret?", default=True):
                secret_name = _create_secret()
            else:
                print_error("No secret selected.")
                return
        else:
            secret_names = [x.credentials_name for x in secrets]
            secret_names.append("Create a new secret")
            secret_name = prompt_choices("Secret", secret_names)
            if secret_name == "Create a new secret":
                secret_name = _create_secret()

    service = V1ServeRevisionServiceForm(
        expose=3000,
        healthcheck=V1PortPath(path="/",port=3000),
        monitoring=[V1PortPath(path="/metrics",port=3000)],
        autoscaling=V1Autoscaling(min=1, max=2, metric="cpu", target=50),
        auxiliary=V1AuxiliaryForm(
            runner_type=_get_runner_type(lockfile.type),
        )
    ).to_dict()

    form = {
        "name":service_name,
        "message":message,
        "env":(
            None
            if use_api_key is None or secret_name is None
            else {
                "SERVICE_AUTH_KEY": V1EnvForm(
                    secret=secret_name,
                    source="secret",
                ).to_dict()
            }
        ),
        "image": _generate_image_name(lockfile),
        "resources": V1ResourcesForm(
            cluster=cluster.name,
            preset=preset.name,
        ).to_dict(),
        "import": {
            "/model": _sanitize_model_form(V1ImportForm(
                model=V1ModelRefForm(
                    organization_name=organization_name,
                    model_repository_name=lockfile.repository_name,
                    model_number=lockfile.model_number,
                )
            ))
        },
        "run": [
            V1Command(
                command=lockfile.entrypoint,
                workdir="/model/"+os.getcwd().split("/")[-1],
            ).to_dict()
        ],
        "ports": [V1PortPath(port=3000).to_dict()],
        "service":service,
    }

    with open("service.yaml", "w") as f:
        cleaned = _sanitize(form)
        b = yaml.dump(cleaned, default_flow_style=False, sort_keys=False)
        b = b.replace("_import", "import")
        f.write(b)
    
    print_success("service.yaml created.")

def _create_secret() -> str:
    secret_name = prompt_text("Secret name")
    secret_value = prompt_text("Secret value")
    resp = vessl_api.secret_upsert_generic_secret_api(
        organization_name=vessl_api.organization.name,
        secret_upsert_generic_secret_api_input=secret_upsert_generic_secret_api_input.SecretUpsertGenericSecretAPIInput(
            secret_name=secret_name,
            value=secret_value,
        )
    )
    print_info(f"Secret {resp.credentials_name} created.")
    return resp.credentials_name

def _get_runner_type(model_runner_type: str) -> str:
    if model_runner_type == "vessl" or model_runner_type == "hf-transformers" or model_runner_type == "torch":
        return "vessl"
    elif model_runner_type == "bento":
        return "bento"
    else:
        raise ValueError(f"Unsupported model runner type: {model_runner_type}")

def _sanitize(yaml_obj):
    if isinstance(yaml_obj, dict):
        cleaned = dict((k, _sanitize(v)) for k, v in yaml_obj.items() if v is not None)
        return cleaned
    elif isinstance(yaml_obj, list):
        cleaned = [_sanitize(v) for v in yaml_obj if v is not None]
        return cleaned
    else:
        return yaml_obj

def _generate_image_name(
    vesslmodel: VesslModel,
):
    if vesslmodel.framework_type == "torch":
        return VESSL_SERVICE_TORCH_BASE_IMAGE_TEMPLATE.format(
            **{
                "pytorch_version": vesslmodel.pytorch_version,
                "cuda_version": vesslmodel.cuda_version,
            }
        )
    elif vesslmodel.framework_type == "tensorflow":
        return VESSL_SERVICE_TENSORFLOW_BASE_IMAGE_TEMPLATE.format(
            **{
                "tensorflow_version": vesslmodel.tensorflow_version,
                "cuda_version": vesslmodel.cuda_version,
            }
        )
    raise ValueError("Either pytorch_version or tensorflow_version must be provided")

def _sanitize_model_form(form: V1ImportForm):
    return f"vessl-model://{form.model.organization_name}/{form.model.model_repository_name}/{form.model.model_number}"
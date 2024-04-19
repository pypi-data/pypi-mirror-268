import yaml
from depot.config import DepotConfig
from prettytable import PrettyTable
from depot.cluster_spec import ClusterSpec
from depot.jobfile import JobSpec
from depot.provider_spec import ProviderSpec
from depot_api.api import default_api
from depot_api.models.job_instance_in import JobInstanceIn
from depot_api.models.cluster_in import ClusterIn
from depot_api.models.provider import Provider
from git_ai.metrics.experiment import get_new_exp_name
from git_ai.cmd.ai_repo import AIRepo
import pygit2
import os


def login(username: str, password: str):
    default_api.DefaultApi().login_login_post(username=username, password=password)


def list_clusters(config: DepotConfig):

    response = config.api().list_clusters_clusters_get()
    providers = config.api().list_providers_providers_get()
    provider_types = config.api().list_providers_types_provider_types_get()
    provider_type_dict2 = {p['id']: p['name'] for p in provider_types}
    provider_type_dict = {
        prov['id']: provider_type_dict2[prov['provider_type_id']] for prov in providers}
    provider_dict = {p['id']: p['name'] for p in providers}
    table = PrettyTable()
    table.field_names = ['Name', 'Provider', 'Provider Type']
    for cluster in response:
        table.add_row([cluster['name'], provider_dict[cluster['provider_id']],
                      provider_type_dict[cluster['provider_id']]])
    print(table)


def list_provider_types(config: DepotConfig):
    response = config.api().list_providers_types_provider_types_get()
    table = PrettyTable()
    table.field_names = ['Name', 'Module']
    for provider_type in response:
        table.add_row([provider_type['name'], provider_type['module']])
    print(table)


def list_providers(config: DepotConfig):
    provider_types = config.api().list_providers_types_provider_types_get()
    provider_types_dict = {p['id']: p['name'] for p in provider_types}
    response = config.api().list_providers_providers_get()
    table = PrettyTable()
    table.field_names = ['Name', 'Type']
    for provider in response:
        table.add_row(
            [provider['name'], provider_types_dict[provider['provider_type_id']]])
    print(table)


def list_jobs(config: DepotConfig):
    response = config.api().list_job_instances_job_instances_get()
    table = PrettyTable()
    table.field_names = ['Name', 'Status']
    for job in response:
        table.add_row([job['name'], job['status']])
    print(table)


def start_job(config: DepotConfig, cluster_name: str):
    try:
        repo_folder = pygit2.discover_repository(os.getcwd())
        if not repo_folder:
            print("Cannot find a git repository in the current folder. Please run this command from a git repository.")
            return

        repo = AIRepo(repo_folder)
        job_spec = JobSpec.from_file(
            os.path.join(repo.workdir, '.jobfile.yaml'))
        job_instance_name = get_new_exp_name(repo)
        clusters = config.api().list_clusters_clusters_get()
        cluster = [c for c in clusters if c['name'] == cluster_name]
        if not cluster:
            print(f"Cluster {cluster_name} does not exist.")
            return
        cluster = cluster[0]
        repo_url = repo.remotes['origin'].url
        response = config.api().create_job_instance_job_instances_post(JobInstanceIn(
            repository_url=repo_url,
            starting_commit=repo.head.target.hex,
            userlogin=config.login,
            job_name=job_spec.name,
            cluster_id=cluster['id'],
            name=job_instance_name
        ))

        job_launched = config.api().read_job_instance_job_instances_job_instance_id_get(
            response['id'])

        print(f"Job {job_launched['name']} started.")
        return 0
    except Exception as e:
        print(f"Error starting job: {e}")
        return 1


def log(config: DepotConfig, job_name: str):
    instances = config.api().list_job_instances_job_instances_get()
    instance = [i for i in instances if i['name'] == job_name]
    if not instance:
        print(f"Job {job_name} does not exist.")
        return
    
    instance = instance[0]
    response = config.api().read_log_logs_job_instance_id_get(instance['id'])
    print(response)
    print(response['log'])


def create_provider(config: DepotConfig, spec_file: str) -> int:

    try:
        spec = ProviderSpec.from_file(spec_file)
        with open(spec.credentials, 'r') as file:
            credentials = file.read()
        provider_types = config.api().list_providers_types_provider_types_get()
        provider_type = [
            p for p in provider_types if p['name'] == spec.provider_type]
        if not provider_type:
            print(f"Provider type {spec.provider_type} is not supported")
            return 1
        response = config.api().create_provider_providers_post(Provider(
            name=spec.name,
            provider_type_id=int(provider_type[0]['id']),
            credentials=credentials,
            userlogin=config.login))
        return 0
    except Exception as e:
        print(f"Error creating provider: {e}")
        return 1


def create_cluster(config: DepotConfig, spec_file: str) -> int:
    try:
        spec = ClusterSpec.from_file(spec_file)
        providers = config.api().list_providers_providers_get()
        provider = [
            p for p in providers if p['name'] == spec.provider]
        if not provider:
            print(f"Provider {spec.provider} does not exist.")
            return 1
        response = config.api().create_cluster_clusters_post(ClusterIn(
            name=spec.name,
            provider_id=provider[0]['id'],
            nodes=spec.nodes,
            userlogin=config.login))
        return 0
    except Exception as e:
        print(f"Error creating cluster: {e}")
        return 1

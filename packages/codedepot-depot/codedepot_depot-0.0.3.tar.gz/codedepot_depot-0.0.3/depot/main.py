import argparse
from venv import create

from depot.config import DepotConfig
from depot.api import create_provider, create_cluster, list_clusters, list_jobs, list_provider_types, list_providers, start_job, log


def parse_args():
    # Create the top-level parser
    parser = argparse.ArgumentParser(
        description="Command line tool for managing jobs, clusters, and providers.")
    parser.add_argument('--version', action='store_true',
                        help='Print the version of the tool')
    # Create subparsers for the main commands
    subparsers = parser.add_subparsers(dest='command', help='Main commands')

    # Subparser for the 'login' command
    login_parser = subparsers.add_parser('login', help='Log into the system')

    # Subparser for the 'log' command
    log_parser = subparsers.add_parser('log', help="Check a job instance's log")
    log_parser.add_argument('name', help='Name of the job instance')

    # Subparser for the 'job' command
    job_parser = subparsers.add_parser('job', help='Job operations')
    job_subparsers = job_parser.add_subparsers(
        dest='job_command', help='Job sub-commands')

    # Sub-commands under 'job'
    job_start_parser = job_subparsers.add_parser('start', help='Start a job')
    job_start_parser.add_argument(
        'cluster_name', help='Name of the cluster used to run the job.')
    job_subparsers.add_parser('list', help='List all jobs')
    job_stop_parser = job_subparsers.add_parser('stop', help='Stop a job')
    job_stop_parser.add_argument('name', help='Name of the job to stop')

    # Subparser for the 'cluster' command
    cluster_parser = subparsers.add_parser(
        'cluster', help='Cluster operations')
    cluster_subparsers = cluster_parser.add_subparsers(
        dest='cluster_command', help='Cluster sub-commands')

    # Sub-commands under 'cluster'
    cluster_create_parser = cluster_subparsers.add_parser(
        'create', help='Create a cluster')
    cluster_create_parser.add_argument(
        'spec', help='Filename of the cluster configuration')
    cluster_subparsers.add_parser('list', help='List all clusters')

    # Subparser for the 'provider' command
    provider_parser = subparsers.add_parser(
        'provider', help='Provider operations')
    provider_subparsers = provider_parser.add_subparsers(
        dest='provider_command', help='Provider sub-commands')

    # Sub-commands under 'provider'
    provider_create_parser = provider_subparsers.add_parser(
        'create', help='Create a provider')
    provider_create_parser.add_argument(
        'spec', help='Filename of the provider configuration')
    provider_subparsers.add_parser('list', help='List all providers')
    provider_subparsers.add_parser(
        'list_types', help='List available providers')

    # Parse the arguments
    return parser.parse_args()


def main():
    args = parse_args()
    if args.version:
        print("0.0.3")
        return

    if args.command == 'login':
        DepotConfig.create()
        return

    config = DepotConfig.default()
    if not config:
        print("Please log in by running `depot login` first.")
        return

    if args.command == 'job':
        if args.job_command == 'start':
            start_job(config, args.cluster_name)
        elif args.job_command == 'list':
            list_jobs(config)
        elif args.job_command == 'stop':
            print(f"Stopping job {args.name}...")
        elif args.job_command == 'log':
            print(f"Stopping job {args.name}...")
    elif args.command == 'cluster':
        if args.cluster_command == 'create':
            print(f"Creating cluster from {args.spec}...")
            create_cluster(config, args.spec)
        elif args.cluster_command == 'list':
            list_clusters(config)
    elif args.command == 'provider':
        if args.provider_command == 'create':
            print(f"Creating provider from spec {args.spec}...")
            create_provider(config, args.spec)
        elif args.provider_command == 'list':
            list_providers(config)
        elif args.provider_command == 'list_types':
            list_provider_types(config)
    elif args.command == 'log':
        print(f"Getting log for job {args.name}...")
        log(config, args.name)


if __name__ == "__main__":
    main()

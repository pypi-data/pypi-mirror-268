from argparse import ArgumentParser
import staticjinjaplus


def cli() -> None:
    arg_parser = ArgumentParser(
        description='The staticjinjaplus CLI which should be your main and only way to interact with staticjinjaplus.'
    )

    command_arg_parser = arg_parser.add_subparsers(dest='command', required=True)

    build_arg_parser = command_arg_parser.add_parser('build', help='Build the site')
    build_arg_parser.add_argument(
        '-w', '--watch',
        help='Automatically rebuild the site when templates are modified',
        action='store_true'
    )

    command_arg_parser.add_parser('clean', help='Delete and recreate the output directory')

    command_arg_parser.add_parser('publish', help='Build and publish the site (using `rsync` through SSH)')

    command_arg_parser.add_parser('serve', help='Serve the output directory through HTTP')

    args = arg_parser.parse_args()

    config = staticjinjaplus.load_config()

    if args.command == 'build':
        staticjinjaplus.build(config, args.watch)
    elif args.command == 'clean':
        staticjinjaplus.clean(config)
    elif args.command == 'publish':
        staticjinjaplus.publish(config)
    elif args.command == 'serve':
        staticjinjaplus.serve(config)

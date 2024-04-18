from argparse import Namespace, ArgumentParser
import os


def parse_arguments() -> tuple[Namespace, list]:
    known: Namespace
    unknown: list
    parser: ArgumentParser = ArgumentParser('Running in parallel mode')

    # anubis-specific stuff
    parser.add_argument('--aggregate', type=str, default='results.json')
    parser.add_argument('--features', type=str, default=['features'], nargs='*')
    parser.add_argument('--output', type=str, default='.tempoutput')
    parser.add_argument('--pass-threshold', type=float, default=1.0)
    parser.add_argument('--processes', type=int, default=10)
    parser.add_argument('--unit', type=str, default='example')
    parser.add_argument('--log-file', type=str)

    # flags
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--hide-failed', action='store_true')
    parser.add_argument('--hide-passed', action='store_true')
    parser.add_argument('--hide-summary', action='store_true')
    parser.add_argument('--pass-with-no-tests', action='store_true')
    parser.add_argument('--quiet', default=False, action='store_true')

    # sent directly to behave
    parser.add_argument('--tags', type=str, nargs='*', action='append', default=[])
    parser.add_argument('-D', action='append')

    known, unknown = parser.parse_known_args()

    # format anything that needs to be formatted
    # output files
    known.log_file = os.path.join(known.output, 'latest.log') if not known.log_file else known.log_file
    known.output = os.path.join(os.getcwd(), known.output)
    known.aggregate = os.path.join(known.output, known.aggregate)

    # update user definitions
    user_defs: Namespace = Namespace()
    for user_def in known.D:
        data = user_def.split('=')
        setattr(user_defs, data[0], True if len(data) == 1 else data[-1])
    known.D = user_defs

    return known, unknown

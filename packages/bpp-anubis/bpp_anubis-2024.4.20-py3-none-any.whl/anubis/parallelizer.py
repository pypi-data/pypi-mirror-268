import os.path
from os.path import join
from behave.runner import Runner
from behave.configuration import Configuration


def test_runner(*data) -> str:
    p_index, args, args_unknown, tests = data
    junit_dir: str = join(args.output, "junit_results")
    output_file: str = join(args.output, 'json_results', str(p_index) + '.json')

    if not os.path.isdir(junit_dir):
        os.makedirs(junit_dir, exist_ok=True)

    if not os.path.isdir(join(args.output, 'json_results')):
        os.makedirs(join(args.output, 'json_results'), exist_ok=True)

    # set up the args required to kick off a test run
    command_args = [f'-D {k}={v}' for k, v in vars(args.D).items()]
    command_args.extend(['-D', f'parallel={p_index}'])
    command_args.extend(['-f', 'json', '-o', f'{output_file}'])
    command_args.extend(['--junit', f'--junit-directory={junit_dir}'])
    command_args.extend(f'--tags={tag}' for tag_group in args.tags for tag in tag_group)
    command_args.append('--no-summary')
    command_args.append('--capture')
    command_args.extend(args_unknown)
    command_args.extend(tests)
    config = Configuration(command_args=command_args)

    # run the tests
    Runner(config).run()
    return output_file

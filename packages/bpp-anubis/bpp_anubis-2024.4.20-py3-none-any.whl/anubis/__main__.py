# __main__.py
import logging
import os
import shutil
import sys
from anubis import arg_parser_main, results
from anubis.feature_file_parser import get_tests
from anubis.parallelizer import test_runner
from anubis.text import print_console_output
from behave.model import Feature, Scenario, ScenarioOutline
from datetime import datetime
from multiprocessing import Pool


def main() -> int:
    # Misc Setup -------------------------------------------------------------------------------------------------------
    start: datetime = datetime.now()
    args, args_unknown = arg_parser_main.parse_arguments()
    print_console_output('startup_statement', **vars(args))

    # Set up output dirs and files -------------------------------------------------------------------------------------
    # create a directory that will contain results and be exported
    print_console_output('output_statement', **vars(args))
    os.makedirs(args.output, exist_ok=True)

    # set up logging
    logging.basicConfig(
        filename=args.log_file,
        filemode='w',
        level=logging.DEBUG,
        format='[%(asctime)s] [%(levelname)s] %(message)s',
        datefmt='%H:%M:%S'
    )
    logger: logging.Logger = logging.getLogger()
    logger.info('Args: \n\t' + "\n\t".join(str(a) for a in vars(args).items()))

    # Run the tests ----------------------------------------------------------------------------------------------------
    print_console_output('parameter_statement', **vars(args))
    # get all testable tests and run them
    tests_to_run: list[Feature | Scenario | ScenarioOutline] = get_tests(args.features, args.tags, args.unit)
    passed, failed, total = 0, 0, 0
    best_split: int = -(-len(tests_to_run) // args.processes)
    max_proc: int = min(best_split, args.processes)
    test_split: dict = {i: [] for i in range(max_proc)}

    # split the tests into groups
    i: int = 0
    while len(tests_to_run) > 0:
        test_split[i].append(tests_to_run.pop())
        i = (i + 1) % max_proc

    # run the tests and handle the output
    if not args.dry_run and best_split > 0:
        print_console_output('running_statement', test_split=test_split, **vars(args))

        with Pool(processes=max_proc) as pool:
            run_args: list = [(i, args, args_unknown, [t.location.filename for t in tests]) for i, tests in test_split.items()]
            output_files: list = pool.starmap(test_runner, run_args)

        results.write_result_aggregate(files=output_files, aggregate_out_file=args.aggregate)
        logging.info(f'output files: {output_files}')

        # logic to print out the results
        passed, failed, total = results.get_result_values(args.aggregate)
        results.print_result_summary(args, start, datetime.now(), passed, failed)
        logger.info(f'passed: {passed}, failed: {failed}')
    else:
        print_console_output('dry_run_statement', test_split=test_split, **vars(args))
    if args.output.endswith('.tempoutput'): shutil.rmtree(args.output)

    # exit correctly
    if args.pass_with_no_tests or total == 0:
        print_console_output('end_statement', **vars(args))
        return 0
    return 1 - int(passed/total >= args.pass_threshold)  # python boolean int to exit code


if __name__ == '__main__':
    sys.exit(main())

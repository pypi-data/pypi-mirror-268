import os
from behave.model import Feature as BehaveFeature, Scenario, ScenarioOutline
from behave.model_core import FileLocation
from behave.parser import parse_file
from behave.tag_expression import TagExpression
from glob import glob
from pathlib import Path


def matches_tags(tags: list, tag_expression: TagExpression) -> bool:
    """Given a list of tags and a tag expression, figure out if the tags match the tag expression"""
    # if there are no tags or no tag expression, the test is testable
    if not tag_expression:
        return True
    if not tags:
        return False

    booleans: list = []
    for and_group in tag_expression.ands:
        group_booleans: list = []
        for tag in and_group:
            if tag.startswith('-') or tag.startswith('not '):
                group_booleans.append(tag not in tags)
            else:
                group_booleans.append(tag in tags)
        booleans.append(all(group_booleans))
    return all(booleans)


def get_tests(paths: list, tags: list, unit: str) -> list[BehaveFeature]:
    """Given a list of feature files and tags, return a list of tests matching those criteria"""
    parsed_gherkin = parse_tests(paths)
    return get_testable_tests(parsed_gherkin, tags, unit)


def parse_tests(paths: list) -> list[BehaveFeature]:
    """Given a list of feature files parse each feature and return list of tests"""
    parsed_gherkin: list[BehaveFeature] = []

    # get all paths to the feature files and take care of duplicates
    all_paths: list = []
    for path in paths:
        all_paths.extend([path] if os.path.isfile(path) else glob(f'{path}/**/*.feature', recursive=True))

    # parse the feature files, remove None cases
    for path in set([Path(str(Path(path).absolute())) for path in all_paths]):
        parsed_gherkin.append(parse_file(path))

    return [gherkin for gherkin in parsed_gherkin if gherkin]


def get_testable_tests(gherkin: list[BehaveFeature], tags: list[list[str]], unit) -> list[BehaveFeature]:
    """given a list of tests and tags, return tests that match those tags"""
    tags: list = [tag for group in tags for tag in group]
    testable_tests: list = []
    expression: TagExpression = TagExpression(tags)

    if unit.lower() == 'feature':
        testable_tests.extend([f for f in gherkin if matches_tags(f.tags, expression)])
    elif unit.lower() == 'scenario':
        testable_tests.extend([s for feature in gherkin for s in feature if matches_tags(s.effective_tags, expression)])
    else:  # unit == 'example'
        for s in [s for feature in gherkin for s in feature if matches_tags(s.effective_tags, expression)]:
            if isinstance(s, ScenarioOutline):
                for example, row in [(e, r) for e in s.examples for r in e.table.rows]:
                    setattr(row, 'location', FileLocation(f'{example.filename}', row.line))
                testable_tests.extend(row for ex in s.examples for row in ex.table.rows)
            elif isinstance(s, Scenario):
                testable_tests.append(s)
    [setattr(item, 'location', FileLocation(os.path.join(os.getcwd(), f'{item.location}'), item.line)) for item in testable_tests]
    return testable_tests

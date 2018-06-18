import json

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), 'discover_opendap'))
from discover_opendap import discover
from run_cumulus_task import run_cumulus_task

def task(event, context):
    input = event.input
    sources = input.sources
    boundary = input.boundary
    return discover(sources, boundary)

def handler(event, context):
    return run_cumulus_task(task, event, context)

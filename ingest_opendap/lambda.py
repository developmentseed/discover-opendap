import json

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), 'ingest_opendap'))
from ingest_opendap import ingest
from run_cumulus_task import run_cumulus_task

def task(event, context):
    input = event.input
    sources = input.sources
    boundary = input.boundary
    return ingest(sources, boundary)

def handler(event, context):
    return run_cumulus_task(task, event, context)

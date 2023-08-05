#!/bin/bash

set -e

if [[ ${MODE} = "WORKER" ]]; then
    echo "Starting Worker"
    python run_worker.py
else
     echo "Executing Workflow"
    python run_workflow.py
fi

#!/bin/bash

echo "domain_name: $1"
echo "error: $2"

python3 ./detect_dnssec_configuration_errors.py $1 $2
python3 ./analyze_visualize_error_logs.py $1 $2

echo "DONE"

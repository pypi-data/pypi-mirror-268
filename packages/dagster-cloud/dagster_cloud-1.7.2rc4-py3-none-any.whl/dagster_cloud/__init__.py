import sys

import dagster_plus

# Redirect all imports to dagster_plus
sys.modules["dagster_cloud"] = dagster_plus

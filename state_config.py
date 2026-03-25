"""
State configuration for this WashingtonDischargeWatch instance.

All state-specific values are centralized here. To deploy for a new state,
run: python deploy_new_state.py <STATE_CODE>

This file is overwritten by deploy_new_state.py — do not add logic here.
"""

STATE_CODE = "WA"
STATE_NAME = "Washington"
APP_NAME = "WashingtonDischargeWatch"
APP_TAGLINE = "Washington Discharge Monitoring"
DOMAIN = "washingtondischargewatch.org"
DATA_FILE = "wa_exceedances_launch_ready.csv"
CONTACT_EMAIL = "data@washingtondischargewatch.org"
MAILING_ADDRESS = ""
TIMEZONE_LABEL = "PST"
EPA_REGION = 10

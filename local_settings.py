'''
Configuration Settings

Includes keys for Twilio, etc.  Second stanza intended for Heroku deployment.
'''

# Uncommet to configure in file.
ACCOUNT_SID = "ACada83e74041961d67e5911551a72327e" 
AUTH_TOKEN = "fbbec006e81886090a0170a42dd2cf4d"
BSSSPAM_APP_SID = "AP2d4146f2a6513803f80a93cc470851ab"
BSS_SPAM_ID = "+18148301515"


# Begin Heroku configuration - configured through environment variables.
import os
ACCOUNT_SID = os.environ['ACCOUNT_SID']
AUTH_TOKEN = os.environ['AUTH_TOKEN']
BSSSPAM_APP_SID = os.environ['BSSSPAM_APP_SID']
BSS_SPAM_ID = os.environ['BSS_SPAM_ID']

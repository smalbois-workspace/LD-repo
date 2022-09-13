#!/usr/bin/env python
from decouple import config
import ldclient
from ldclient.config import Config

# sdk_key for the LaunchDarkly SDK key (found in LaunchDarklyPlatform) -
# Use Production key if .env variable ENVIRONMENT == production else default to Test env
if config('ENVIRONMENT') == 'production1':
    sdk_key = config('SDK_KEY_PRODUCTION')
else:
    sdk_key = config('SDK_KEY_TEST')

# Set feature_flag_key to the feature flag key you want to evaluate
# Hardcoded the flag name here.....
feature_flag_key = "test-demographic-users"

def show_message(s):
    print("*** %s" % s)
    print()

if __name__ == "__main__":
    if not sdk_key:
        show_message("Please create or edit a .env file and make sure the SDK Keys are set to initialise your LaunchDarkly SDK first")
        exit()

    ldclient.set_config(Config(sdk_key))

    # The SDK starts up the first time ldclient.get() is called
    if ldclient.get().is_initialized():
        show_message("SDK successfully initialized!")
    else:
        show_message("SDK failed to initialize")
        exit()

    # Set up the user properties for this test. This users will not appear in the UI since a rule is created.
    user = {
        "key": "seb-user-key",
        "name": "Seb",
        "firstName": "Seb",
        "lastName": "Malbois",
        "email": "seb@gmail.com",
        "custom": {
            "gender": "male",
            "age": 20
        }
    }

    flag_value = ldclient.get().variation(feature_flag_key, user, False)

    show_message("Feature flag '%s' is returning %s for this user" % (feature_flag_key, flag_value))
    show_message("Promo Discount to apply is %s percent and the loyalty is %s" % (flag_value["promoDiscount"],flag_value["loyalty"]))

    # Here we ensure that the SDK shuts down cleanly and has a chance to deliver analytics
    # events to LaunchDarkly before the program exits. If analytics events are not delivered,
    # the user properties and flag usage statistics will not appear on your dashboard. In a
    # normal long-running application, the SDK would continue running and events would be
    # delivered automatically in the background.
    ldclient.get().close()

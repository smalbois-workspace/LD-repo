# Seb's Sample app

Below, you'll find the basic build procedure. Extra detailed information can be found in the 'LaunchDarkly UseCase and Approach.pdf' file.

This demo requires Python version 3.5 or higher.

## Build instructions

1)	Get the project from github here: https://github.com/smalbois-workspace/LD-repo.git

2)	Install the LaunchDarkly Python SDK by running `pip3 install -r requirements.txt`

3)	Create a .env file in the root directory

```yaml
SDK_KEY_PRODUCTION=<SDK KEY PRODUCTION>
SDK_KEY_TEST=<SDK KEY TEST>
ENVIRONMENT=production
```

Note: please add your SDK Key to the different environments (Production and Test are the only available environments here)

4)	Update the .env file with your SDK key (since ENVIRONMNENT set to production please copy and paste the SDK_KEY from Step 2 to SDK_KEY_PRODUCTION)

5)	Make sure the name of the feature flag key set in the script file FeatureFlags.py for variable feature_flag_key is set to the feature flag key you created previously (in this case test-demographic-users)

6)	Execute the script and verify that you are seeing the following:

`python3 FeatureFlags.py`

*** SDK successfully initialized!

*** Feature flag 'test-demographic-users' is returning {'loyalty': 'bronze', 'promoDiscount': 10} for this user

*** Promo Discount to apply is 10 percent and the loyalty is bronze

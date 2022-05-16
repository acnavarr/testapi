from properties import CONFIG

def before_feature(context, feature):
    context.api_host = CONFIG['api_host']
    context.api_key = CONFIG['api_key']
    context.params = None

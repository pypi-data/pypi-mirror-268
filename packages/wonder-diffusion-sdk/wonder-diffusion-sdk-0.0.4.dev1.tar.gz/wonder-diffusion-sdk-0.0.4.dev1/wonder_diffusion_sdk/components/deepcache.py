def enable_deepcache(pipeline, cache_interval=3, cache_branch_id=0):
    try:
        from DeepCache import DeepCacheSDHelper
    except Exception as e:
        print(f'Cannot import DeepCacheSDHelper: {e}')

    helper = DeepCacheSDHelper(pipe=pipeline)
    helper.set_params(cache_interval=cache_interval,
                      cache_branch_id=cache_branch_id)
    helper.enable()

    return helper

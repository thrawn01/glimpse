
def set_defaults(CONF):
    CONF.set_default('logging_exception_prefix',
                     '%(color)s%(asctime)s.%(msecs)03d TRACE %(name)s'
                     ' [01;35m%(instance)s[00m')
    CONF.set_default('logging_debug_format_suffix', '[00;33mfrom'
                     '(pid=%(process)d) %(funcName)s '
                     '%(pathname)s:%(lineno)d[00m')
    CONF.set_default('logging_default_format_string', '%(asctime)s.%(msecs)03d'
                     ' %(color)s%(levelname)s %(name)s [[00;36m-%(color)s] '
                     '[01;35m%(instance)s%(color)s%(message)s[00m')
    CONF.set_default('logging_context_format_string', '%(asctime)s.%(msecs)03d'
                     '%(color)s%(levelname)s %(name)s [[01;36m%(request_id)s'
                     '[00;36m%(user_id)s %(project_id)s%(color)s]'
                     '[01;35m%(instance)s%(color)s%(message)s[00m')
    CONF.set_default('debug', True)

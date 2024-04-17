from logger_local.LoggerComponentEnum import LoggerComponentEnum

REACTION_LOCAL_PYTHON_PACKAGE_COMPONENT_ID = 168
REACTION_LOCAL_PYTHON_PACKAGE_COMPONENT_NAME = 'reaction_local/tests/test_reaction.py'

REACTION_LOCAL_PYTHON_LOGGER_CODE = {
    'component_id': REACTION_LOCAL_PYTHON_PACKAGE_COMPONENT_ID,
    'component_name': REACTION_LOCAL_PYTHON_PACKAGE_COMPONENT_NAME,
    'component_category': LoggerComponentEnum.ComponentCategory.Code.value,
    'developer_email': 'tal.g@circ.zone'
}

REACTION_LOCAL_PYTHON_LOGGER_TEST = REACTION_LOCAL_PYTHON_LOGGER_CODE.copy()
REACTION_LOCAL_PYTHON_LOGGER_TEST['component_category'] = LoggerComponentEnum.ComponentCategory.Unit_Test.value

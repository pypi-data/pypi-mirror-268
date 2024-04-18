# -*- coding: utf-8 -*-
import logging


logger = logging.getLogger(__name__)


default_profile = 'profile-rer.externalnews:default'


def to_1100(context):
    """
    """
    logger.info('Upgrading rer.externalnews to version 1100')
    context.runImportStepFromProfile(default_profile, 'repositorytool')
    context.runImportStepFromProfile(default_profile, 'difftool')
    context.runImportStepFromProfile(
        default_profile,
        'typeinfo',
        run_dependencies=True)

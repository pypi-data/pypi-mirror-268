#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 说明：
#    更新
# History:
# Date          Author    Version       Modification
# --------------------------------------------------------------------------------------------------
# 2024/4/18    xiatn     V00.01.000    新建
# --------------------------------------------------------------------------------------------------
import pkg_resources
import pip


def update_package():
    installed_version = pkg_resources.get_distribution('<your-package>').version
    available_version = pip._vendor.packaging.version.parse(
        pip._internal.utils.misc.get_installed_version('<your-package>'))

    if available_version > installed_version:
        print(f"A newer version ({available_version}) is available. Updating...")
        # pip.main(['install', '--upgrade', '<your-package>'])

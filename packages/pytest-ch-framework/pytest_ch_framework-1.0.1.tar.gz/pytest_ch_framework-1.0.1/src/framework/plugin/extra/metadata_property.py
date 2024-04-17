from typing import Sequence, MutableSequence

import pytest
from ...io.config import Properties


@pytest.hookimpl(trylast=True)
def pytest_sessionfinish(session, exitstatus):
    config = session.config
    metadata = config.pluginmanager.getplugin("metadata")
    if metadata:
        try:
            from pytest_metadata.plugin import metadata_key
            meta: dict = config.stash[metadata_key]
        except ImportError:  # pytest-metadata < 3.x
            meta: dict = config._metadata["Base URL"]

        # 控制下meta要显示出来的数据
        not_show_in_report: MutableSequence[str] = meta.get("not_show_in_report", [])
        not_show_in_report.append("not_show_in_report")
        p = Properties.load_from_str(
            map(
                lambda item: f'{item[0]}={item[1]}',
                filter(
                    lambda item: item[0] not in not_show_in_report,
                    meta.items()
                )
            )
        )
        p.write_file("environment.properties")

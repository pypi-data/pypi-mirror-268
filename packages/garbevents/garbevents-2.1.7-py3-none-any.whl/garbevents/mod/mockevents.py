#!/usr/bin/python
"""
@Author  :  Lijiawei
@Date    :  2022/7/12 7:48 下午
@Desc    :  mock events line.
"""
import json
import re
import typing

from mitmproxy import ctx
from mitmproxy import exceptions
from mitmproxy import flowfilter
from mitmproxy import http
from mitmproxy.utils.spec import parse_spec


class MockEventsSpec(typing.NamedTuple):
    matches: flowfilter.TFilter
    subject: str
    replacement: str


def parse_mock_events_spec(option: str) -> MockEventsSpec:
    spec = MockEventsSpec(*parse_spec(option))

    try:
        re.compile(spec.subject)
    except re.error as e:
        raise ValueError(f"Invalid regular expression {spec.subject!r} ({e})")

    return spec


class MockEvents:
    def __init__(self):
        self.replacements: list[MockEventsSpec] = []

    def load(self, loader):
        loader.add_option(
            "mock_events",
            typing.Sequence[str],
            [],
            """
            使用"|flow-filter|url-regex|replacement-json"形式的模式将远程资源映射到本地json，其中分隔符是|。
            """,
        )

    def configure(self, updated):
        if "mock_events" in updated:
            self.replacements = []
            for option in ctx.options.mock_events:
                try:
                    spec = parse_mock_events_spec(option)
                except ValueError as e:
                    raise exceptions.OptionsError(
                        f"Cannot parse mock_events option {option}: {e}"
                    ) from e

                self.replacements.append(spec)

    def request(self, flow: http.HTTPFlow) -> None:
        if flow.response or flow.error or not flow.live:
            return
        url = flow.request.pretty_url
        for spec in self.replacements:
            if spec.matches(flow) and re.search(spec.subject, url):
                try:
                    contents = json.dumps(spec.replacement)
                except (TypeError, KeyError):
                    contents = {}
                flow.response.set_text(contents)

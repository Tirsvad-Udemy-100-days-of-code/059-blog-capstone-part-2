"""
@file
@brief Unit test: the entry point starts the server on the configured address.
"""

import pytest

from blog import constants, main


def test_main_runs_server_on_configured_host_and_port(monkeypatch: pytest.MonkeyPatch) -> None:
    """@brief main() calls app.run with HOST and PORT."""
    calls: list[tuple[str, int]] = []

    def fake_run(host: str, port: int) -> None:
        calls.append((host, port))

    monkeypatch.setattr(main.app, "run", fake_run)
    main.main()
    assert calls == [(constants.HOST, constants.PORT)]

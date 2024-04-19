import uuid

from typer.testing import CliRunner

from lumaCLI.main import app

runner = CliRunner()


def test_status():
    fake_uuid = uuid.uuid4()
    result = runner.invoke(
        app,
        ["status", "--luma-url", "http://localhost:8000", "--ingestion-id", fake_uuid],
    )
    assert result.exit_code == 0

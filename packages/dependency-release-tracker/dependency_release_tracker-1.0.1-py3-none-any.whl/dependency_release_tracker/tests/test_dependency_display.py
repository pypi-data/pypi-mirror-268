import pytest
from unittest.mock import patch
from rich.console import Console

from dependency_release_tracker.display.dependency_display import DependencyDisplay
from dependency_release_tracker.models.dependency import Dependency


# Fixture para criar uma lista de dependências
@pytest.fixture
def sample_dependencies():
    return [
        Dependency(
            name="libA",
            latest_version="2.0.0",
            current_version="1.0.0",
            published_at="2023-01-01T12:00:00Z",
            notes="Update available",
            url="http://example.com/libA",
        ),
        Dependency(
            name="libB",
            latest_version="1.5.0",
            current_version="1.5.0",
            published_at="2023-01-02T12:00:00Z",
            notes="",
            url="http://example.com/libB",
        ),
    ]


# Teste para verificar a exibição no modo simplificado
def test_display_simple_output(sample_dependencies):
    with patch.object(Console, "print") as mock_print:
        display = DependencyDisplay()
        display.display(sample_dependencies, simple_output=True)

        # Verifica se os prints contêm a saída esperada
        assert mock_print.call_count > 0  # Verifica se algo foi impresso
        mock_print.assert_any_call(
            "\n"
        )  # Verifica se novas linhas são impressas para espaçamento
        mock_print.assert_any_call(
            contains="(UPDATED)", style="bold"
        )  # Verifica a exibição do status atualizado


# Teste para verificar a exibição no modo detalhado
def test_display_detailed_output(sample_dependencies):
    with patch.object(Console, "print") as mock_print:
        display = DependencyDisplay()
        display.display(sample_dependencies, simple_output=False)

        # Verifica se a saída inclui notas de lançamento formatadas
        mock_print.assert_any_call(contains="Release notes:")
        mock_print.assert_any_call(
            contains="http://example.com/libA"
        )  # Verifica se o URL está presente


# Utilização de capsys para capturar saída
def test_display_with_capsys(capsys, sample_dependencies):
    display = DependencyDisplay()
    display.display(sample_dependencies, simple_output=True)
    captured = capsys.readouterr()
    assert (
        "libA" in captured.out
    )  # Verifica se o nome da dependência é parte da saída capturada
    assert "---" in captured.out  # Verifica se a divisória está presente

from unittest.mock import MagicMock, patch

import app.main as main_mod


def test_ask_routes_to_faq():
    fake_route = MagicMock()
    fake_route.name = "faq"

    with patch.object(main_mod, "router", MagicMock(return_value=fake_route)):
        with patch.object(main_mod, "faq_chain", return_value="FAQ answer"):
            result = main_mod.ask("What is return policy?")

    assert result == "FAQ answer"


def test_ask_routes_to_sql():
    fake_route = MagicMock()
    fake_route.name = "sql"

    with patch.object(main_mod, "router", MagicMock(return_value=fake_route)):
        with patch.object(main_mod, "sql_chain", return_value="SQL answer"):
            result = main_mod.ask("Show me shoes under 3000")

    assert result == "SQL answer"
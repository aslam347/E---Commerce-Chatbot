from unittest.mock import MagicMock, patch

import app.faq as faq


def test_generate_answer():
    fake_client = MagicMock()
    fake_client.chat.completions.create.return_value = MagicMock(
        choices=[
            MagicMock(
                message=MagicMock(content="Test answer")
            )
        ]
    )

    with patch.object(faq, "groq_client", fake_client):
        result = faq.generate_answer(
            "What is return policy?",
            "Returns allowed in 7 days"
        )

    assert result == "Test answer"


def test_faq_chain():
    fake_result = {
        "metadatas": [[{"answer": "Refund is processed in 5 days"}]]
    }

    with patch.object(faq, "get_relevant_qa", return_value=fake_result):
        with patch.object(faq, "generate_answer", return_value="Refund in 5 days"):
            answer = faq.faq_chain("How long for refund?")

    assert answer == "Refund in 5 days"
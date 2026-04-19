# from semantic_router import Route, RouteLayer
from semantic_router.layer import RouteLayer
from semantic_router.route import Route
from semantic_router.encoders import HuggingFaceEncoder

encoder = HuggingFaceEncoder(
    name="sentence-transformers/all-MiniLM-L6-v2"
)

# faq = Route(
#     name='faq',
#     utterances=[
#         "What is the return policy of the products?",
#         "Do I get discount with the HDFC credit card?",
#         "How can I track my order?",
#         "What payment methods are accepted?",
#         "How long does it take to process a refund?",
#     ]
# )
faq = Route(
    name='faq',
    utterances=[
        "What is the return policy of the products?",
        "Do I get discount with the HDFC credit card?",
        "How can I track my order?",
        "What payment methods are accepted?",
        "How long does it take to process a refund?",
        "Can I cancel or modify my order after placing it?",
        "What should I do if I receive a damaged product?",
        "How do I use a promo code during checkout?",
        "Do you offer international shipping?",
        "How to get refund?"
    ]
)

sql = Route(
    name='sql',
    utterances=[
        "I want to buy nike shoes that have 50% discount.",
        "Are there any shoes under Rs. 3000?",
        "Do you have formal shoes in size 9?",
        "Are there any Puma shoes on sale?",
        "What is the price of puma running shoes?",
    ]
)

router = RouteLayer(routes=[faq, sql], encoder=encoder)

if __name__ == "__main__":
    print(router("What is your policy on defective product?").name)
    print(router("Pink Puma shoes in price range 5000 to 1000").name)
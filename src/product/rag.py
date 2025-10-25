from src.database import SessionLocal
from .models import Product


class RAGSystem:
    '''
    simple RAG system to retrieve data from db and generate answer for user.
    '''
    def __init__(self, ai_model):
        self.ai_model = ai_model

    def retrieve_products(self, user_message):
        """
        Simple keyword-based retrieval (can extend with embeddings later).
        """
        session = SessionLocal()
        all_products = session.query(Product).all()
        relative_products = list()
        for product in all_products:
            if product.name in user_message or product.name.replace(" ", "") in user_message.replace(" ", ""):
                relative_products.append(f"{product.name}: {product.description} | قیمت: {product.price}")
        session.close()
        return relative_products

    def generate_answer(self, user_message):
        products = self.retrieve_products(user_message)

        prompt = f"""
        Based on the following products exist in database, answer the user's message in Persian.
        If the information does not exist in the database, politely say so.
        
        Products:
        {products}
        
        User Question: {user_message}
        
        Please provide a helpful and accurate response in Persian.
        """

        answer = self.ai_model.generate_response(prompt)
        return answer

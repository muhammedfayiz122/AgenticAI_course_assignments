import streamlit as st
from product_assistent_bot import ProductAssistant

st.set_page_config(
    page_title="Product Assistant",
    page_icon="💬",
    layout="centered"
)

st.title("Chatbot")
st.caption("Search for Products")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

def generate_response():
    """
    """
    try:
        query = st.chat_input("Enter product name to search : ")
        if query:
            try:
                llm_chain = ProductAssistant().llm_chain()
                response = llm_chain.invoke({"input": query})
                print(response)
                if response:
                    try:
                        if isinstance(response,list):
                            print("output is list")
                            for product in response:
                                print(type(product))
                                details_html = "<ul>"
                                for detail in product['product_details']:
                                    details_html += f"<li>{detail}</li>"
                                details_html += "</ul>"
                                st.markdown(f"""
                                        <div style="border:1px solid #ddf; padding:15px; border-radius:10px; margin-bottom:15px; background-color:rgb(58 58 58);">
                                            <h2 style="color:#fff;">{product['product_name']}</h2>
                                            <p style="font-size:16px; color:#fff;">{details_html}</p>
                                            <p style="color:#fff;"><strong>Price:</strong> ₹{product['tentative_price']}</p>
                                        </div>
                                    """,
                                    unsafe_allow_html=True
                                )

                        elif isinstance(response, dict):
                            print("output is in dict")
                            print(len(response))
                            st.markdown(f"""
                                    <div style="border:1px solid #ddd; padding:15px; border-radius:10px; margin-bottom:15px; background-color:#f7f7f7">
                                        <h2 style="color:#333;">{response['product_name']}</h2>
                                        <p style="font-size:16px;">{response['product_details']}</p>
                                        <p><strong>Price:</strong> {response['tentative_price']}</p>
                                    </div>
                                """,
                                unsafe_allow_html=True
                            )

                    except Exception as e:
                        print(f"Error : {e}")
                        st.write(response)

            except Exception as e:
                try:
                    st.write(f"Error : {e}")  
                except Exception as e:
                    print(f"Streamlit not working : {e}")
    except Exception as e:
            print(f"Error : {e}")

if __name__ == "__main__":
    generate_response()



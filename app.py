import streamlit as st
import requests

st.set_page_config(page_title="n8n", page_icon="📈")
st.markdown(
    """
    <h1 style='text-align:center'>
        <img src="https://uxwing.com/wp-content/themes/uxwing/download/brands-and-social-media/n8n-icon.png" width="70" style="margin-left: 7px;">
        <span style='color:#fa2dab;'>Integration with Streamlit UI</span>
    </h1>
    """,
    unsafe_allow_html=True
)

query = st.text_input("🔍 Enter your query")
submit = st.button("🚀 Get Answer")

if submit and query:
    st.info("Sending request to AI pipeline...")

    # Your n8n webhook endpoint
    webhook_url = "https://uv4.app.n8n.cloud/webhook-test/new"
    
    try:
        # Send POST request with plain JSON input
        response = requests.post(webhook_url, json={"query": query})
        content_type = response.headers.get("Content-Type", "")

        if response.status_code == 200:
            # ✅ Expecting plain text response
            if "text" in content_type.lower() or response.text.strip():
                st.success("✅ generated successfully!")
                st.write(response.text.strip())  # ← plain text output
            else:
                st.warning("⚠️ No text returned from n8n workflow.")
        else:
            st.error(f"❌ Request failed: {response.status_code}")
            st.text(response.text)

    except Exception as e:
        st.error(f"⚠️ Exception occurred: {str(e)}")

import streamlit as st

from rhdzmota.ext.streamlit_webapps.page_view import PageView


class PVEmailACLSuccess(PageView):
    def view(self):
        st.success("We have send your access link via the provided email!")

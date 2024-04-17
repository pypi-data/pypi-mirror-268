from rhdzmota.ext.streamlit_webapps.page_view import PageView


class PVEmailACLFailure(PageView):

    def view(self):
        return st.error("Sorry! There seems to be an issue.")

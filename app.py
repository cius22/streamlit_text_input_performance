import streamlit as st
import numpy as np
import plotly.express as px
import plotly.io as pio


@st.cache_data()
def compute_figures(n_figures=30, n_points=100000):
    figures = {}

    for i in range(0,n_figures):
        title = f"Figure {i}"
        fig = px.histogram(np.random.normal(100, 50, n_points))
        figures[title] = pio.to_json(fig, engine='auto')

    return figures


@st.cache_data(experimental_allow_widgets=True)
def visualize_figures(n_figures, n_points):
    figures = compute_figures(n_figures, n_points)
    st.write("")
    st.subheader('Many figures')

    for title, fig in figures.items():
        st.write(title)
        st.plotly_chart(pio.from_json(fig, engine='auto'), use_container_width=True)
        st.write("")


def main():

    st.set_page_config(
        page_title="Text input testing",
        page_icon="🧊"
    )

    if "show" not in st.session_state:
        st.session_state['show'] = False

    st.header("TEXT INPUT PERFORMANCE TESTING")

    with st.form("Form example"):
        _ = st.text_input("Try this text input:")
        _ = st.text_area("Try this text area:")

        # Feel free to try out other input widgets
        # _ = st.checkbox("Try this checkbox:")
        # _ = st.toggle("Try this toggle:")
        # _ = st.radio("Try this radio:", ["A", "B", "C"])
        # _ = st.selectbox("Try this selectbox:", ["A", "B", "C"])
        # _ = st.multiselect("Try this multiselect:", ["A", "B", "C"])
        # _ = st.slider("Try this slider:", 0, 100, 5)
        # _ = st.select_slider("Try this select_slider:", ["A", "B", "C"])
        # _ = st.number_input("Try this number_input:", 0, 100)
        # _ = st.date_input("Try this date_input:")
        # _ = st.time_input("Try this time_input:")

        submit_col_1, submit_col_2 = st.columns(2)
        with submit_col_1:
            confirm = st.form_submit_button("Submit")
        with submit_col_2:
            if confirm:
                st.write("You just clicked a useless button!")


    st.subheader("Enable/disable figures to observe their effects on the text input")

    col_1, col_2 = st.columns(2)

    with col_1:
        n_figures = st.number_input("How many figures?", 1, 100, 30)
        if st.session_state['show']:
            if st.button("Hide figures", use_container_width=True):
                st.session_state['show'] = False
                st.rerun()
        else:
            if st.button("Show figures", use_container_width=True):
                st.session_state['show'] = True
                st.rerun()

    with col_2:
        n_points = st.number_input("How many points per figure?", 1, 1000000, 10000)
        if st.button("Free cached data", use_container_width=True):
            st.cache_data.clear()


    if st.session_state['show']:
        visualize_figures(n_figures, n_points)


if __name__ == '__main__':
    main()
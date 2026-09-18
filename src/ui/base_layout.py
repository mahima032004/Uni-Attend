import streamlit as st


def style_theme_tokens():
    """Defines the colour palette for both light and dark mode.

    The browser picks the right block automatically based on the user's
    system theme, and Streamlit follows the same system theme, so the
    hardcoded colours here stay in sync with Streamlit's own widgets.

    Call this once, before any other style function.
    """
    st.markdown("""
        <style>
            :root {
                --ua-page:     #5865F2;
                --ua-dash:     #E0E3FF;
                --ua-card:     #E0E3FF;
                --ua-heading:  #1A1B3A;
                --ua-body:     #3A3B5C;
                --ua-brand:    #FFFFFF;
                --ua-primary:  #5865F2;
                --ua-accent:   #EB459E;
                --ua-btn-text: #FFFFFF;
            }

            @media (prefers-color-scheme: dark) {
                :root {
                    --ua-page:     #1B1D3A;
                    --ua-dash:     #14152B;
                    --ua-card:     #2A2D5C;
                    --ua-heading:  #E0E3FF;
                    --ua-body:     #B4B8E6;
                    --ua-brand:    #C7CBFF;
                    --ua-primary:  #7A85F5;
                    --ua-accent:   #F06BB4;
                    --ua-btn-text: #12132A;
                }
            }
        </style>
    """, unsafe_allow_html=True)


def style_background_home():
    st.markdown("""
        <style>
            .stApp {
                background: var(--ua-page) !important;
            }

            .stApp div[data-testid="stColumn"] {
                background-color: var(--ua-card) !important;
                padding: 2.5rem !important;
                border-radius: 5rem !important;
            }

            .stApp div[data-testid="stColumn"] h1,
            .stApp div[data-testid="stColumn"] h2 {
                color: var(--ua-heading) !important;
            }
        </style>
    """, unsafe_allow_html=True)


def style_background_dashboard():
    st.markdown("""
        <style>
            .stApp {
                background: var(--ua-dash) !important;
            }
        </style>
    """, unsafe_allow_html=True)


def style_base_layout():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

            #MainMenu, footer, header {
                visibility: hidden;
            }

            .block-container {
                padding-top: 1.5rem !important;
            }

            h1 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 3.5rem !important;
                line-height: 1.1 !important;
                margin-bottom: 0rem !important;
                color: var(--ua-heading) !important;
            }

            h2 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 2rem !important;
                line-height: 0.9 !important;
                margin-bottom: 0rem !important;
                color: var(--ua-heading) !important;
            }

            h3, h4 {
                font-family: 'Outfit', sans-serif;
                color: var(--ua-heading) !important;
            }

            p, label, .stMarkdown {
                font-family: 'Outfit', sans-serif;
                color: var(--ua-body) !important;
            }

            button {
                border-radius: 1.5rem !important;
                background-color: var(--ua-primary) !important;
                color: var(--ua-btn-text) !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
            }

            button[kind="secondary"] {
                border-radius: 1.5rem !important;
                background-color: var(--ua-accent) !important;
                color: var(--ua-btn-text) !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
            }

            button[kind="tertiary"] {
                border-radius: 1.5rem !important;
                background-color: var(--ua-heading) !important;
                color: var(--ua-page) !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
            }

            button:hover {
                transform: scale(1.05);
            }

            button p {
                color: inherit !important;
            }
        </style>
    """, unsafe_allow_html=True)
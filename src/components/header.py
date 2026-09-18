
import streamlit as st


def header_home():

    logo_url = "https://images.openai.com/static-rsc-4/SuVfNqm-UGVmND92Cs2tUDTbk7_SBOTT0VQvZG0OP2kgJn9zsSrxmaufxowmpLbFI9GL1lm-suQE725d3aTCgUTtb5eiooyb41m3kjVlv_djEmHcRHmNXOXP25S8iJt_qXU_zhLzj3v4_Wj4TjTnHT9xOastdmDQQnhpss9bZEJLke9Z04gJVoxEcNTePcvz?purpose=fullsize"
    
    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px; margin-top:30px">
            <img src='{logo_url}' style='height:100px;' />
            <h1 style='text-align:center; color:#E0E3FF'>UniAttend</h1>
        </div>   
                
                """, unsafe_allow_html=True)


def header_dashboard():

    logo_url = "https://images.openai.com/static-rsc-4/SuVfNqm-UGVmND92Cs2tUDTbk7_SBOTT0VQvZG0OP2kgJn9zsSrxmaufxowmpLbFI9GL1lm-suQE725d3aTCgUTtb5eiooyb41m3kjVlv_djEmHcRHmNXOXP25S8iJt_qXU_zhLzj3v4_Wj4TjTnHT9xOastdmDQQnhpss9bZEJLke9Z04gJVoxEcNTePcvz?purpose=fullsize"
    
    st.markdown(f"""
        <div style="display:flex; align-items:center; justify-content:center; gap:10px">
            <img src='{logo_url}' style='height:85px;' />
            <h2 style='text-align:left; color:#5865F2'>UniAttend</h2>
        </div>   
                
                """, unsafe_allow_html=True)
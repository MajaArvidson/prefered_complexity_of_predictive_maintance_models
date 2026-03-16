import streamlit as st # type: ignore
import time
import uuid
import pandas as pd

from utils.navigation import set_page, scroll_to_top
from utils.generate_cases import generate_case_sequence, features
from utils.data_logger import save_response

def case_page():

	scroll_to_top()

	if "case_sequence" not in st.session_state:
		st.session_state.case_sequence = generate_case_sequence()
		st.session_state.case_index = 0
		st.session_state.start_time = time.time()
		st.session_state.participant_id = str(uuid.uuid4())

	cases = st.session_state.case_sequence
	index = st.session_state.case_index

	if index >= len(cases):
		set_page("survey")

	case = cases[index]
    
	st.header(f"Case {index + 1} of {len(cases)}")

	left, right = st.columns([5,1])

	with left:
		st.progress((index + 1)/len(cases))

	with right:
		next_clicked = st.button("Next Case →", use_container_width=True)

	st.space("medium")

	st.subheader("Telemetry Data")
	df = pd.DataFrame([[str(case[f]) for f in features]], columns=features)
	st.dataframe(df, hide_index=True)

	left2, _, right2 = st.columns([4,1,2])

	with left2:
		st.subheader("AI Recommendation")
		st.text(case["recommendation"])

	with right2:
		st.metric("Confidence", f"{round(max(case['confidence'])*100,2)}%", border=True, width="stretch", height="stretch")

	st.subheader("Reasoning")
	st.code("IF " + ",\nAND ".join(case["explanation"]))

	st.space("medium")

	with st.container(border=True):
		trust = st.slider("I trust the model's recommendation", 1, 7)
		understanding = st.slider("I understand why the model made this decision", 1, 7)
		comfort = st.slider("I feel comfortable relying on this system", 1, 7)
		follow = st.radio("Would you follow the recommendation?", ["Yes", "No"])

	st.space("small")

	if next_clicked:
		response_time = time.time() - st.session_state.start_time

		response = {
            "participant_id": st.session_state.participant_id,
            "case_index": index,
            "model": case["model_name"],	
            "trust": trust,
            "understanding": understanding,
            "comfort": comfort,
            "follow": follow,
            "response_time": response_time
        }

		save_response(response)

		st.session_state.case_index += 1
		st.session_state.start_time = time.time()

		if st.session_state.case_index >= len(cases):
			st.session_state.page = "survey"

		st.rerun()
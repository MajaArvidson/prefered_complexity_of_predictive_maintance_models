import streamlit as st # type: ignore
import pandas as pd
import random
import joblib

@st.cache_resource
def load_models():
    simple_model = joblib.load("models/simple_model.pkl")
    complex_model = joblib.load("models/complex_model.pkl")
    return {"simple": simple_model, "complex": complex_model}

models = load_models()

base_cases = [
    {"cpu_usage": 5.0, "memory_usage": 30.0, "disk_io": 5.0, "network_latency": 20.0},
    {"cpu_usage": 95.0, "memory_usage": 30.0, "disk_io": 10.0, "network_latency": 25.0},
    {"cpu_usage": 20.0, "memory_usage": 97.0, "disk_io": 5.0, "network_latency": 30.0},
    {"cpu_usage": 25.0, "memory_usage": 40.0, "disk_io": 450.0, "network_latency": 20.0},
    {"cpu_usage": 30.0, "memory_usage": 35.0, "disk_io": 10.0, "network_latency": 450.0},
    {"cpu_usage": 85.0, "memory_usage": 90.0, "disk_io": 300.0, "network_latency": 400.0},
    {"cpu_usage": 75.0, "memory_usage": 80.0, "disk_io": 450.0, "network_latency": 40.0},
    {"cpu_usage": 90.0, "memory_usage": 95.0, "disk_io": 5.0, "network_latency": 35.0}
]

features = list(base_cases[0].keys())

def generate_case_sequence():
    cases = []

    model_order = random.choice([["simple", "complex"], ["complex", "simple"]])

    for base in base_cases:
        for model in model_order:
            case = base.copy()

            model_obj = models[model]
            model_case = pd.DataFrame([case])
            case["model_name"] = model
            case["model_obj"] = model_obj

            case["recommendation"] = model_obj.predict(model_case)[0]
            case["confidence"] = model_obj.predict_proba(model_case)[0]
            case["explanation"] = tree_path(model_obj, model_case)

            cases.append(case)

    random.shuffle(cases)
    return cases

def tree_path(model, case):
    tree = model.tree_
    feature = tree.feature
    threshold = tree.threshold

    node_indicator = model.decision_path(case)
    leaf_id = model.apply(case)

    rules = []

    for node_id in node_indicator.indices:
        if leaf_id[0] == node_id:
            continue
        feature_name = features[feature[node_id]]
    
        if case.iloc[0, feature[node_id]] <= threshold[node_id]:
            threshold_sign = "<="
        else:
            threshold_sign = ">"
            
        rules.append(
            f"{feature_name} {threshold_sign} {round(threshold[node_id],2)}"
        )

    return rules
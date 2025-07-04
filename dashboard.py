import streamlit as st
import pandas as pd
import plotly.express as px
import subprocess
import time
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Test Results Dashboard",
    page_icon="📊",
    layout="wide"
)

# Title
st.title("Test Results Dashboard")

# Session state to persist test data
if "test_data" not in st.session_state:
    st.session_state.test_data = {
        "test_name": [],
        "status": [],
        "execution_time": [],
        "timestamp": []
    }

# Function to run a specific test
def run_test(test_file):
    start_time = time.time()
    try:
        result = subprocess.run(
            ["python", "-m", "pytest", test_file, "--tb=short", "-q"],
            capture_output=True,
            text=True
        )
        end_time = time.time()
        execution_time = round(end_time - start_time, 2)

        stdout = result.stdout
        stderr = result.stderr

        # Determine status from stdout
        if "1 passed" in stdout.lower():
            status = "Pass"
        elif "1 failed" in stdout.lower():
            status = "Fail"
        else:
            status = "Error"

        # Show log
        st.code(stdout + "\n" + stderr)

        return {
            "status": status,
            "execution_time": execution_time,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    except Exception as e:
        st.error(f"Exception: {e}")
        return {
            "status": "Error",
            "execution_time": 0,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

# Function to run all tests
def run_all_tests():
    for category, tests in test_categories.items():
        for test_file in tests:
            st.write(f"Running {test_file}...")
            result = run_test(test_file)
            st.session_state.test_data["test_name"].append(test_file)
            st.session_state.test_data["status"].append(result["status"])
            st.session_state.test_data["execution_time"].append(result["execution_time"])
            st.session_state.test_data["timestamp"].append(result["timestamp"])

# Sidebar for test selection
st.sidebar.header("Test Controls")

# Test categories
test_categories = {
    "Login Tests": [
        "tests/test_Login/Login_successfully.py",
        "tests/test_Login/Invalid_email.py",
        "tests/test_Login/Invalid_pass.py",
        "tests/test_Login/blank_email.py",
        "tests/test_Login/blank_pass.py"
    ],
    "Customer Page Tests": [
        "tests/test_Customer_page/Checking_table.py",
        "tests/test_Customer_page/Search_successfully.py",
        "tests/test_Customer_page/Test_Add_Source_successfully.py",
        "tests/test_Customer_page/Test_Add_Source_failed_with_blank_name.py",
        "tests/test_Customer_page/Test_Add_Source_failed_with_blank_file.py",
        "tests/test_Customer_page/Test_customer_detail.py",
        "tests/test_Customer_page/Test_number_of_inquiry_card.py",
        "tests/test_Customer_page/Test_redirect_inquiry.py",
        "tests/test_Customer_page/Testing_Chatbot.py"
    ],
    "Knowledge Page Tests": [
        "tests/test_Knowledge_page/Delete_file_successfully.py",
        "tests/test_Knowledge_page/Delete_file_cancel.py",
        "tests/test_Knowledge_page/Download_file_successfully.py",
        "tests/test_Knowledge_page/Download_file_cancel.py"
    ]
}

# Run all tests button
if st.sidebar.button("Run All Tests"):
    with st.spinner("Running all tests..."):
        run_all_tests()
        st.success("All tests completed!")

# Test category selection
selected_category = st.sidebar.selectbox("Select Test Category", list(test_categories.keys()))

# Individual test selection
selected_test = st.sidebar.selectbox("Select Test", test_categories[selected_category])

# Run selected test button
if st.sidebar.button("Run Selected Test"):
    with st.spinner(f"Running {selected_test}..."):
        result = run_test(selected_test)
        st.session_state.test_data["test_name"].append(selected_test)
        st.session_state.test_data["status"].append(result["status"])
        st.session_state.test_data["execution_time"].append(result["execution_time"])
        st.session_state.test_data["timestamp"].append(result["timestamp"])
        st.success(f"Test completed in {result['execution_time']:.2f} seconds")

# Main dashboard metrics
col1, col2, col3 = st.columns(3)

test_data = st.session_state.test_data
with col1:
    st.metric("Total Tests", len(test_data["test_name"]))

with col2:
    passed_tests = test_data["status"].count("Pass")
    st.metric("Passed Tests", passed_tests)

with col3:
    failed_tests = len(test_data["status"]) - passed_tests
    st.metric("Failed Tests", failed_tests)

# Pie chart for test results
if test_data["test_name"]:
    df = pd.DataFrame(test_data)
    fig = px.pie(df, names="status", title="Test Results Distribution")
    st.plotly_chart(fig)

# Detailed test results table
if test_data["test_name"]:
    st.subheader("Detailed Test Results")
    df = pd.DataFrame(test_data)
    st.dataframe(df, use_container_width=True)

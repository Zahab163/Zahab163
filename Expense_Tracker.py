import streamlit as st

# --- Page Config ---
st.set_page_config(page_title="Financial Health Analyzer", layout="centered")

# --- Title & Intro ---
st.title("EXPENSE TRACKER")
st.markdown("Analyze your financial health and savings habits.")

# --- Personal Info ---
st.header("Personal Information")
name = st.text_input("Enter your name:")
profession = st.text_input("Enter your profession:")

if name and profession:
    st.success(f"Welcome **{name.title()}**! Let's analyze your financial health as a **{profession.title()}**.")

# --- Income Input ---
st.header("Monthly Income")
income = st.number_input("Enter your total monthly income (PKR):", min_value=0)

# --- Expense Input ---
st.header("Expense Breakdown")
essentials = st.number_input("Essentials (e.g., rent, utilities):", min_value=0)
wants = st.number_input("Wants (e.g., dining out, entertainment):", min_value=0)
save = st.number_input("Savings or Investments:", min_value=0)

# --- Expense Submission ---
with st.form("expense_form"):
    amount = st.number_input("Add a new expense amount:", min_value=0)
    category = st.text_input("Expense category:")
    submitted = st.form_submit_button("Submit")

if submitted and amount > 0:
    st.success(f"Expense of PKR {amount} in category '{category}' submitted!")

# --- Financial Analysis ---
if income > 0:
    expense = essentials + wants
    savings = save
    savings_percent = (savings / income) * 100 if income else 0
    essentials_percent = (essentials / income) * 100
    wants_percent = (wants / income) * 100
    save_percent = (savings / income) * 100

    st.subheader("Expense Distribution")
    st.write(f"**Essentials:** {essentials_percent:.2f}%")
    st.write(f"**Wants:** {wants_percent:.2f}%")
    st.write(f"**Saves/Invests:** {save_percent:.2f}%")

    # --- Savings Goal ---
    st.header("Savings Goal")
    goals = st.slider("Set your savings goal (% of income):", 0, 100, 20)
    diff = round(goals - savings_percent, 2)

    if round(goals, 2) == round(savings_percent, 2):
        st.success(f"Congratulations {name.title()}! You have achieved your savings goal.")
    else:
        st.info(f"You're **{abs(diff):.2f}%** {'above' if diff < 0 else 'away from'} your goal.")

    # --- Summary ---
    st.header("Summary")
    st.markdown(f"""
    **Name:** {name.title()}  
    **Profession:** {profession.title()}  
    **Income:** PKR {income:,.0f}  
    **Expenses:** PKR {expense:,.0f}  
    **Savings:** PKR {savings:,.0f} ({savings_percent:.2f}%)  
    **Essentials:** {essentials_percent:.2f}%  
    **Wants:** {wants_percent:.2f}%  
    **Saves/Invests:** {save_percent:.2f}%  
    **Savings Goal:** {goals}%  
    **Status:** {abs(diff):.2f}% {'above' if diff < 0 else 'away from'} your goal  
    """)
else:
    st.warning("Please enter your income to analyze your financial health.")
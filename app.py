import streamlit as st


def get_bot_reply(user_message: str) -> tuple[str, str]:
    """Return the chatbot reply and an explanation of the rule that fired."""

    cleaned_message = user_message.strip().lower()

    if cleaned_message in ("hello", "hi", "hey"):
        return "Hi!", "Used the first if condition because the user sent a greeting."
    elif cleaned_message in ("how are you", "how are you?"):
        return "I'm fine, thanks!", "Entered the elif branch that handles 'how are you' statements."
    elif cleaned_message in ("bye", "goodbye"):
        return "Goodbye!", "Matched the farewell elif branch for goodbye statements."
    else:
        return (
            "I didn't understand that yet.",
            "Fell through to the else block since no predefined rule matched.",
        )


def init_chat_state() -> None:
    """Ensure Streamlit session state has a place to store the conversation."""

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []


def main() -> None:
    """Render the Streamlit interface for the rule-based chatbot."""

    st.set_page_config(page_title="Rule-Based Chatbot", page_icon="🤖")
    st.title("Simple Rule-Based Chatbot")
    st.write(
        "This demo shows how a chatbot can respond using functions, if-elif rules, and a loop "
        "that displays the conversation. Enter one of the accepted statements to see the logic "
        "explanation for each reply."
    )

    init_chat_state()

    with st.form(key="chat_form", clear_on_submit=True):
        user_message = st.text_input("Type a message:")
        submitted = st.form_submit_button("Send")

    if submitted and user_message:
        reply, explanation = get_bot_reply(user_message)
        st.session_state.chat_history.append(
            {
                "user": user_message,
                "bot": reply,
                "explanation": explanation,
            }
        )

    for turn in st.session_state.chat_history:
        st.markdown(
            f"**You:** {turn['user']}\n\n"
            f"**Bot:** {turn['bot']}\n\n"
            f"**Explanation:** {turn['explanation']}"
        )

    st.info(
        "Core Python concepts used: functions to organize code, if-elif-else to make decisions, "
        "a loop to display the running conversation, and Streamlit input/output widgets for the UI."
    )


if __name__ == "__main__":
    main()


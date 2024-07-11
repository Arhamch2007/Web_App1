import streamlit as st
import functions

chores = functions.get_todos()


def add_todo():
    chore = st.session_state['new_todo'] + "\n"
    chores.append(chore)
    functions.write_todos(chores)


st.title("My To-Do App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")
for index, chore in enumerate(chores):
    checkbox = st.checkbox(chore, key=chore)
    if checkbox:
        chores.pop(index)
        functions.write_todos(chores)
        del st.session_state[chore]
        st.rerun()

st.text_input(label="Enter a todo", placeholder='Add new todo...', 
              on_change=add_todo, key='new_todo')


def task_tool(task):
    return f"[Task Tool] Task added: {task}"

def calendar_tool(event):
    return f"[Calendar Tool] Event scheduled: {event}"

def notes_tool(note):
    return f"[Notes Tool] Note saved: {note}"


def main_agent(user_input):
    user_input = user_input.lower()

    if "task" in user_input:
        return task_tool(user_input)
    elif "meeting" in user_input or "schedule" in user_input:
        return calendar_tool(user_input)
    elif "note" in user_input:
        return notes_tool(user_input)
    else:
        return "Main Agent: Input not recognized"


memory = []

def store_memory(entry):
    memory.append(entry)

def show_memory():
    return "\n".join(memory) if memory else "No memory yet"


def run():
    print("Multi-Agent AI System Started")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        if user_input.lower() == "memory":
            print(show_memory())
            continue

        response = main_agent(user_input)
        store_memory(response)
        print("AI:", response)


if __name__ == "__main__":
    run()

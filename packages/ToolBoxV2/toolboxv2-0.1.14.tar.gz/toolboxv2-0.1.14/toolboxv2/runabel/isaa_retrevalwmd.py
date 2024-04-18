import datetime

from toolboxv2 import Style

url = "C:\\Users\\Markin\\Isaa\\ObsidianMd\\Main\\Uni\\Ausland\\Analysis_I_und_Lineare_Algebra.pdf"
NAME = "irWmd"


# path = "C:\\Users\\Markin\\Downloads\\[WiSe_2324]_B_&_K_1708251943\\Kurs_WiSe_2324_Berechenbarkei..._.2978590"


def run(app, args):
    from toolboxv2.mods.audio import speech_stream
    from toolboxv2.mods.isaa import Tools
    from toolboxv2.mods.isaa.AgentFramwork import functions_to_llm_functions
    from toolboxv2.mods.isaa.isaa_modi import get_multiline_input
    isaa: Tools = app.get_mod("isaa")

    def print_prompt(msg_data):

        messages = msg_data.get('messages', {})
        print(Style.GREEN2("PROMPT START "))
        for message in messages:
            caller = Style.WHITE(message.get('role', 'NONE').upper()) if message.get('role',
                                                                                     'NONE') == 'user' else 'NONE'
            caller = Style.CYAN(message.get('role', 'NONE').upper()) if message.get('role',
                                                                                    'NONE') == 'system' else caller
            caller = Style.VIOLET2(message.get('role', 'NONE').upper()) if message.get('role',
                                                                                       'NONE') == 'assistent' else caller
            print(f"\n{caller}\n{Style.GREY(message.get('content', '--#--'))}\n")
        print(Style.GREEN("PROMPT END -- "))

    isaa.register_agents_setter(lambda x: x
                                .set_amd_model("ollama/llama2")
                                .set_stream(True)
                                .set_logging_callback(print_prompt)
                                # .set_logging_callback(isaa.print)
                                .set_verbose(True)
                                .set_max_tokens(1200)
                                .set_amd_stop_sequence(['\n\n\n'])
                                )
    isaa.init_isaa(name='think', build=True)

    def fuction_test(x: str):
        """Test returns the input"""
        return x

    def add(x: int, y: int):
        """adds 2 ints and returns the result"""
        return int(x.strip()) + int(y.strip())

    def get_time():
        """returns the time"""
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    isaa.get_agent_class('think').functions = functions_to_llm_functions([
        fuction_test, add, get_time
    ])  # crate_llm_function_from_langchain_tools(
    # ["ddg-search", "requests_get", "python_repl", "terminal", "sleep"])

    while app.alive:
        print("User (e) for exit:")
        user_input = get_multiline_input()
        if user_input == '\n'.join(['e']):
            app.alive = False
            break

        out = isaa.run_agent('think', user_input, persist=False, running_mode="oncex")
        if out:
            speech_stream(out)

    app.exit()

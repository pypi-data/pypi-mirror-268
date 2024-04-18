from toolboxv2 import Style

path = r"C:\Users\Markin\Downloads\[SoSe_2024]_IoSL_(Project)_1713358162"
NAME = "ir"


def run(app, args):
    from toolboxv2.mods.isaa import Tools
    from toolboxv2.mods.isaa.AgentFramwork import ProfessorMode
    from toolboxv2.mods.isaa.isaa_modi import get_multiline_input
    from toolboxv2.mods.isaa.subtools.file_loder import load_from_file_system

    isaa: Tools = app.get_mod("isaa")

    print("Loading Data")
    loder, docs_ = load_from_file_system(path, glob="**/*.pdf")
    print("Getting data...")
    data = docs_()
    print(f"Adding Data {len(data)}")
    isaa.get_context_memory().add_data('BKA', data)
    print("Saving Data")
    isaa.get_context_memory().crate_live_context('BKA')

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
                                # .set_logging_callback(print_prompt)
                                # .set_logging_callback(isaa.print)
                                .set_verbose(True)
                                .set_max_tokens(1200)
                                .set_amd_stop_sequence(['\n\n\n'])
                                )
    isaa.init_isaa(name='BKA', build=True)

    # isaa.get_agent_class('BKA').mode = ProfessorMode

    while app.alive:
        print("User (e) for exit:")
        user_input = get_multiline_input()
        if user_input == '\n'.join(['e']):
            app.alive = False
            break

        isaa.run_agent('BKA', user_input)

    app.exit()


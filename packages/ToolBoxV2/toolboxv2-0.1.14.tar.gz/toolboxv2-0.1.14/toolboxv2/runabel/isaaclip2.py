import platform
from urllib.parse import urlparse

import keyboard

# pyperclip.copy('The text to be copied to the clipboard.')
# pyperclip.paste()

import pyperclip
from toolboxv2 import Style, tbef
from dotenv import load_dotenv

load_dotenv()
NAME = "Iclip2"


def get_speak_input():
    pass


def get_input(speek_mode=False, min_=30):
    from toolboxv2.mods.isaa.isaa_modi import get_multiline_input
    if speek_mode:
        input("Start listig ->")
        print("User (e) for exit:")
        return get_multiline_input()
    print("User (e) for exit:")
    return get_multiline_input()


def get_buffer(buffer):
    if platform.system() != "Darwin":

        event = keyboard.read_event()

        if event.event_type == keyboard.KEY_DOWN:
            key_name = event.name

            if key_name in ['backspace', 'enter', 'space']:
                buffer = ' ' * 8
            else:
                buffer += str(key_name).lower()

            print(buffer[len(buffer) - 8:], end='\r')
    else:
        buffer = input(":")

    return buffer


def function_buffer_manager(buffer: str, functions: dict):
    for name in functions.keys():
        if name in buffer:
            return functions[name]
    return None


def run(app, args):
    from toolboxv2.mods.isaa import Tools as Isaa
    from toolboxv2.mods.isaa.AgentFramwork import MarkdownRefactorMode
    from toolboxv2.mods.isaa.subtools.file_loder import route_local_file_to_function
    from toolboxv2.mods.isaa.subtools.web_loder import route_url_to_function
    functions = {}
    register = lambda n, f: functions.__setitem__(n, f)
    speak_mode = [False, False]

    # Trigger word to process the text
    def toggle_helper(i):
        def _(*_):
            speak_mode[i] = not speak_mode[i]
            print("set speak_mode: ", speak_mode)

        return _

    isaa: Isaa = app.get_mod("isaa")

    isaa.summarization_mode = 1

    isaa.register_agents_setter(lambda x: x
                                .set_amd_model("ollama/llama2")
                                .set_stream(True)
                                .set_logging_callback(print_prompt)
                                # .set_stream_function(stram_print)
                                # .set_logging_callback(isaa.print)
                                # .set_verbose(True)
                                .set_max_tokens(1200)
                                .set_amd_stop_sequence(['\n\n\n'])
                                )

    def mas_text_sum(text):
        sum_text = isaa.mas_text_summaries(text)
        return isaa.run_agent("think", sum_text, all_mem=True)

    def questionl_helper(_):
        text = get_input(speek_mode=speak_mode[0])
        return isaa.run_agent("self", text, all_mem=False)

    def question_helper(_):
        text = get_input(speek_mode=speak_mode[0])
        return isaa.run_agent("think", text, all_mem=True)

    def exiquteion_once_helper(_):
        text = get_input(speek_mode=speak_mode[0])
        return isaa.run_agent("think", text, all_mem=True, running_mode='oncex')

    def lineIs_helper(_):
        text = get_input(speek_mode=speak_mode[0])
        return isaa.run_agent("think", text, all_mem=True, running_mode='lineIs')

    def url_getter(url):
        print("Parsing", url)
        parsed_url = urlparse(url)
        dont_len = parsed_url.netloc.count('.')
        domain = "www"
        if dont_len == 1:
            domain = parsed_url.netloc.split('.')[0]
        if dont_len >= 2:
            domain = parsed_url.netloc.split('.')[1]
        if "wikipedia.org" in parsed_url.netloc:  # https://de.wikipedia.org/wiki/Erster_Weltkrieg##url
            domain = "wikipedia"
        loder, docs_loder = route_url_to_function(url)
        docs = docs_loder
        if not isinstance(docs_loder, list):
            docs = docs_loder()
        isaa.get_context_memory().add_data(domain, docs)
        final_d = '\n\n'.join([doc.page_content for doc in docs])
        return mas_text_sum(final_d)

    def path_getter(path):
        print("Parsing", path)
        loder, docs_loder = route_local_file_to_function(path)
        docs = docs_loder()
        isaa.get_context_memory().add_data("localD", docs)
        final_d = '\n\n'.join([doc.page_content for doc in docs])
        return mas_text_sum(final_d)

    def refactor_helper(text):
        isaa.get_agent_class('self').mode = MarkdownRefactorMode
        res = isaa.run_agent("self", text=text, all_mem=True)
        isaa.get_agent_class('self').mode = None
        return res

    def exit_helper(*_):
        app.alive = False

    def save_mem_helper(*_):
        isaa.save_to_mem()

    register("##e", exit_helper)
    register("##sm", save_mem_helper)
    register("##si", toggle_helper(0))  # toggel speache input mode
    register("##so", toggle_helper(1))  # toogel speache output mode
    register("##sum", mas_text_sum)  # )Summaeryse( zummeryse clipborde & referra to known Nolage
    register("##url", url_getter)  # )web( read curent url from clipord -> must contain an http(s) url and summs the content & ask a question to a wep page
    register("##path", path_getter)  # -> path )folder / file( local data text pdf folders (image)
    register("##rfc", refactor_helper)  # )refactor( refactor agiven txt form the cliport asking for parameters.
    register("##q", question_helper)  # register("##cli",  # )refactor( refactor agiven txt form the cliport asking for parameters.
    register("##x1", exiquteion_once_helper)
    register("##x3", lineIs_helper)

    # isaa.get_context_memory().load_all()

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

    isaa.init_isaa(name='self', build=True)

    print(f"Script running in the background")
    f_names = list(functions.keys())
    print(f"init completed waiting for trigger word: {f_names}")
    buffer = ' ' * 8

    while app.alive:

        buffer = get_buffer(buffer)

        function = function_buffer_manager(buffer, functions)

        if function is None:
            continue

        context = pyperclip.paste()
        res = function(context)

        buffer = ' ' * 8

        if res is None:
            if speak_mode[1]:
                print("No data to verbalise")
            continue

        if speak_mode[1]:
            print("Start speaking")
            app.run_any(tbef.AUDIO.SPEECH_STREAM, text=res, use_cache=True, provider="piper")

        pyperclip.copy(res)

        print(f"waiting for trigger word:: {f_names}")

    app.exit()

    print("\n Exiting...")

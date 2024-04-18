import time

from toolboxv2 import App, AppArgs, Spinner, tbef, Style, get_app

from toolboxv2.utils import show_console

NAME = "mbgr"


# scraping :

# Emails
# Gmail MarkinHausmanns@gmail.com & Drrking883@gmail.com

def get_gmail_msg_tldr(app, n):
    gmail_msg = app.run_any(tbef.GMAILPROVIDER.SEARCH_MESSAGES, service=gmail_service_dr, query="TLDR")
    print(gmail_msg)
    # for msg in gmail_msg:
    _new_m = app.run_any(tbef.GMAILPROVIDER.READ_MESSAGE, service=gmail_service_dr, message=gmail_msg[n])
    print("New message:", _new_m)
    return _new_m, gmail_msg[n]


# and tuMail

# Uni Data Isis

# News Data
# ----------------------

# workflow :

# add event (read day plan ->
# collecting Email & uni & news data Present them in a md file and with a news reporter agent (verbal)

# ----------------------
# perma active :

# web ui
# isaa clip withe ask question verbal + data from day
# scrape web pages
# ----------------------
gmail_service_mh = None
gmail_service_dr = None


def read_n_tldr_event(n=0):
    from toolboxv2.mods.isaa import Tools
    from toolboxv2.mods.isaa.Agents import LLMMode
    global gmail_service_dr, gmail_service_mh
    app = get_app(f"{NAME}.running read event")
    with Spinner("Processioning Account"):
        gmail_service_dr = app.run_any(tbef.GMAILPROVIDER.GMAIL_AUTHENTICATE, name="main")
        print(gmail_service_dr)
    with Spinner("loading last TLDR"):
        tldr, msg_ = get_gmail_msg_tldr(app, n)
    with Spinner("\t\t\t\t\t\t Issa init"):
        isaa: Tools = app.get_mod("isaa")
        isaa.register_agents_setter(lambda x: x
                                    .set_amd_model("ollama/llama2")
                                    .set_stream(False)
                                    .set_verbose(False)
                                    .set_max_tokens(1200)
                                    )
        isaa.init_isaa(name='TLDR', build=True)

        isaa.get_agent_class('TLDR').mode = LLMMode(
            name="NEWS AGENT",
            description="Bietet Benutzern spannende und aktuelle Nachrichten in einer ansprechenden und informativen "
                        "Art und Weise.",
            system_msg="You are now in news agent mode. Deliver exciting and interesting news that informs and "
                       "engages the user. Make sure your answers are accurate, informed and relevant. Encourage users "
                       "to think critically and offer resources to delve deeper when appropriate. and add sources",
        post_msg="NewsAgent:",
            examples=None
        )
    with Spinner("\t\t\t\t\tReding TLDR"):
        agent_report = isaa.run_agent('TLDR', "today's TLDR report summarizes The key points in the artical for the "
                                              "user! : " + tldr,
                                      task_from='system')
    with Spinner("\t\t\t\tGenerating Audio"):
        print(agent_report)
        app.run_any(tbef.AUDIO.SPEECH_STREAM, text=agent_report)


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


def run(app: App, args: AppArgs):
    from toolboxv2.mods.EventManager.module import Tools as EventManagerClass, EventID
    # app.save_load("audio")
    # app.run_any(tbef.AUDIO.SPEECH_STREAM, text="Hallo das ist ein test")
    ev: EventManagerClass = app.run_any(tbef.EVENTMANAGER.GETEVENTMANAGERC)
    event = ev.make_event_from_fuction(read_n_tldr_event, "read_last_tldr", 6, threaded=True)
    ev.register_event(event=event)

    ev.trigger_event(EventID.crate(f"app.{app.id}", "read_last_tldr"))
    app.run_runnable('TBtray')

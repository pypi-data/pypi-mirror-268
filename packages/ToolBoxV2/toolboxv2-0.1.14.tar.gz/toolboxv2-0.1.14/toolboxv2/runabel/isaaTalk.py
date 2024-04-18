import os.path
import queue
import random
import time

import dill
import torch

from toolboxv2 import Spinner, Style,tbef

"""Console script for toolboxv2. Isaa Conversation Tool"""

NAME = "isaa-talk"


def print_prompt(msg_data):
    messages = msg_data.get('messages', {})
    print(Style.GREEN2("PROMPT START "))
    for message in messages:
        caller = message.get('role', 'NONE').upper()
        if caller == 'user':
            caller = Style.WHITE(caller)
        if caller == 'system':
            caller = Style.CYAN(caller)
        if caller == 'assistant':
            caller = Style.VIOLET2(caller)
        print(f"\n{caller}\n{Style.GREY(message.get('content', '--#--'))}\n")
    print(Style.GREEN("PROMPT END -- "))


def run(app, args):
    with Spinner("Importing modules..."):
        from toolboxv2.mods.isaa import Tools
        from toolboxv2.mods.audio import wake_word
        from toolboxv2.mods.audio.TBV2STT.transcription.liveTranscriptHfOpenai import init_live_transcript
    with Spinner("Starting Isaa..."):
        isaa: Tools = app.get_mod("isaa")
    with Spinner("Starting Audio..."):
        app.get_mod("audio").verbose = True

    isaa.register_agents_setter(lambda x: x
                                .set_amd_model("ollama/llama2")
                                # .set_stream(True)
                                .set_logging_callback(print_prompt)
                                # .set_logging_callback(isaa.print)
                                # .set_verbose(True)
                                .set_max_tokens(75)
                                .set_amd_stop_sequence(['\n\n\n'])
                                )

    isaa.init_isaa(name='think', build=True)
    # isaa.get_agent_class('think').mode = ProfessorMode
    mice_index = 1  # get_user_device_mice_id(audio)
    device_index = "cuda:0" if torch.cuda.is_available() else "cpu"
    amplitude_min = 5.4  # s30sek_mean(seconds=10, p=True, microphone_index=mice_index)
    print("mice id : ", mice_index)
    print("amplitude_min: ", amplitude_min)
    print("device_index: ", device_index)
    comm, que = init_live_transcript(chunk_duration=2.6,
                                     amplitude_min=amplitude_min,
                                     model="openai/whisper-base",
                                     microphone_index=mice_index,
                                     device=device_index)

    alive = True

    def spek_to_user(text: str):
        app.print(text)
        with Spinner("Generating audio..."):
            app.run_any(tbef.AUDIO.SPEECH, text=text, use_cache=False)
        # else:
        #     speech_stream(text, voice_index=0)

    isaa.speak = spek_to_user

    """
    Based on the information provided, Markin is currently studying MINT green, an orientation program for computer science studies at TU Berlin. However, he is not satisfied with the quality of education and is considering studying abroad or taking a gap year. To create a life plan for the next 2 years, we need more information about Markin's goals, interests, and priorities.

To help Markin, the following agents and tools can be utilized:

1. Career counselor: To identify career goals, interests, and suggest suitable paths and educational programs.
2. Education consultant: To evaluate the current educational program and suggest alternatives or universities that align with Markin's goals.
3. Financial advisor: To evaluate financial situations and suggest ways to finance education and living expenses.
4. Language learning tools: To learn a new language if studying abroad, such as Duolingo or Rosetta Stone.
5. Travel booking tools: To make travel arrangements, such as Expedia or Kayak.
6. Time management tools: To balance studies and other activities, such as calendars, to-do lists, and productivity apps.
7. Communication tools: To stay in touch with family and friends, such as Skype, WhatsApp, or Zoom.

The following skills would be helpful for this task:

- Get a differentiated point of view: To understand Markin's perspective and priorities.
- Search for information: To gather information about potential universities or programs.
- Calendar entry: To organize and schedule important dates and deadlines.
- Generate documents: To create and organize documents related to education and travel plans.
- Utilize tools: To identify and use tools and resources for organizing and planning.
- Read, analyze, and write summaries: To summarize and organize information about potential universities or programs.

It is essential to gather more information about Markin's situation and preferences before making any decisions or recommendations.

Ask questions to help to find a decisions or recommendations.
    """

    input("Press Enter to Start:")

    comm('start')

    issa_res = ""
    user_text = ""
    data = ""

    print("Hörche ..")
    time.sleep(6)

    while alive:
        while user_text == '':
            while que.qsize() != 0:
                try:
                    data = que.get(timeout=1)
                except:
                    print("- # -")
                    if data.endswith('.') or data.endswith('?') or data.endswith('!'):
                        pass
                    else:
                        data += '.'
                    break
                print(data)
                s_data = data.strip()
                if not data or s_data == 'you' or s_data == "Thank you.":
                    break
                user_text += data

        user_text = user_text.strip()

        data_c = user_text.lower()
        if data_c == "stop.":
            comm('stop')
            comm('exit')
            break
        # process = False if not user_text else user_text[-1] in ['.', '?', '!']

        print(f"\nInputs :\n\ttext={user_text}")
        if user_text:
            comm('stop')
            issa_res = isaa.run_agent('think', user_text, fetch_memory=False, persist=True, persist_mem=False)
            if not issa_res:
                issa_res = "sorry a problem pop during the proses of your request"
            user_text = ''

        # context = pyperclip.paste()
        # if context:
        #     self_agent_config.short_mem.text = context

        if issa_res:
            spek_to_user(issa_res)
            issa_res = ""
            comm('start')
            time.sleep(6)

        # input("Start listening: ")
    # except Exception as e:
    #    print('Error :', e)

    comm('exit')
    print("Auf wieder sehen")
    app.exit()

    return
"""

    while alive:
        if que.qsize() == 0:
            print("Hörche ..")
            time.sleep(4)
        while que.qsize() != 0:
            data = que.get()
            print(data)
            s_data = data.strip()
            if not data or s_data == 'you' or s_data == "Thank you.":
                # awake = False
                break
            else:
                awake = True

            # print(f'#{data}#', end=' ')
            user_text += data  # + ' '
            data_c = data.lower().strip()
            if data_c == "stop.":
                comm('stop')
                comm('exit')
                break
            if data_c in ['sleep', 'night']:
                awake = False
            if data.endswith('.') or data.endswith('?') or data.endswith('!'):
                process = True
                continue

        user_text = user_text.strip()
        # process = False if not user_text else user_text[-1] in ['.', '?', '!']

        print(f"\nInputs :\n\ttext={user_text}\n\t{process=}\n\t{awake=}")

        if not awake:
            isaa.print("Waiting for word")
            comm('stop')
            do_wake_up, user_text = wake_word(word="wake up",
                                              variants=["start", "wake", "isaa", "computer", "isar", "isar."],
                                              microphone_index=mice_index,
                                              amplitude_min=amplitude_min,
                                              model="openai/whisper-medium",
                                              do_exit=False,
                                              do_stop=False, ques=[comm, que])
            if not do_wake_up:
                break
            elif user_text:
                process = True

        if user_text and process:
            comm('stop')
            # with Spinner("Processing input..."):
            issa_res = isaa.run_agent('think', user_text, fetch_memory=False, persist=True, persist_mem=False)
            if not issa_res:
                issa_res = "sorry a problem pop during the proses of your request"
            process = False
            user_text = ''
        else:
            awake = False

        # context = pyperclip.paste()
        # if context:
        #     self_agent_config.short_mem.text = context

        if issa_res:
            # isaa.print("Respond")
            # isaa.print(issa_res)
            spek_to_user(issa_res)
            issa_res = ""
            comm('start')

        # input("Start listening: ")
    # except Exception as e:
    #    print('Error :', e)
"""

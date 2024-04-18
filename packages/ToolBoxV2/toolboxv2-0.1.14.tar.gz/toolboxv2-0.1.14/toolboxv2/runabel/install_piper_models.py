import os
import time
from datetime import datetime

from prompt_toolkit import HTML
from prompt_toolkit.shortcuts import yes_no_dialog

from toolboxv2 import tbef
from toolboxv2.utils.system.types import CallingObject, Result

NAME = 'pin'


def run(app, _):
    from toolboxv2.mods.CloudM.ModManager import download_files
    from toolboxv2.mods.audio.TBV2TTS.util import play_audio_bytes
    from toolboxv2.mods.isaa.subtools.web_loder import get_text_from_urls_vue
    global data_PIPER
    # app = get_app()
    # isaa = app.get_mod('isaa')
    # lang = isaa.text_classification('das ist ein kleiner test', model="papluca/xlm-roberta-base-language-detection")

    mpaths = os.getenv('PIPER_MODEL_PATH')

    current_url = "https://huggingface.co/rhasspy/piper-voices/tree/v1.0.0"
    language = []
    data_PIPER = {
        "language": [],
        "NL": {}
    }

    def list_all_l(_):
        t = get_text_from_urls_vue("https://huggingface.co/rhasspy/piper-voices/tree/v1.0.0", ["span"])
        print(t[1])  # page_content Enable JavaScript
        d = ''.join([b.page_content for b in t[1]]).split(' ')
        s = [k for _, k in enumerate(d) if len(k) == 2]
        data_PIPER["language"] = [k for k in s if
                                  not (k.lower() != k or k[0] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])]
        autocompletion_dict['get_available_codes_by_lang_code'] = {}
        [autocompletion_dict['get_available_codes_by_lang_code'].setdefault(k, None) for k in data_PIPER["language"] if k not in autocompletion_dict['get_available_codes_by_lang_code']]
        print(data_PIPER["language"])
        return Result.ok()

    def get_all_codes_by_lang(call_):
        lang = call_.function_name.lower()
        if len(data_PIPER["language"]) == 0:
            list_all_l(None)
        if lang not in data_PIPER["language"]:
            return Result.default_user_error("error in valid language")
        if lang not in data_PIPER:
            data_PIPER[lang] = {}
        t1 = get_text_from_urls_vue(f"https://huggingface.co/rhasspy/piper-voices/tree/v1.0.0/{lang}", ["span"])
        d = ''.join([b.page_content for b in t1[1]]).split(' ')
        s = [k for _, k in enumerate(d) if len(k) == 5 and '_' in k]
        autocompletion_dict[lang] = {}
        [autocompletion_dict[lang].setdefault(k, None) for k in s if k not in autocompletion_dict[lang]]
        if autocompletion_dict["names"] is None:
            autocompletion_dict["names"] = {}
        autocompletion_dict["names"][lang] = {}
        [autocompletion_dict["names"][lang].setdefault(k, None) for k in s if k not in autocompletion_dict[lang]]
        print(s)
        data_PIPER[lang]["C"] = s
        return Result.ok()

    def get_name(call_: CallingObject):
        lang = call_.function_name[:2].lower()
        if len(data_PIPER["language"]) == 0:
            list_all_l(None)
        if lang not in data_PIPER["language"]:
            return Result.default_user_error("Invalid language")
        if "C" not in data_PIPER[lang]:
            return Result.default_user_error("error in valid C")
        code = call_.function_name
        t2 = get_text_from_urls_vue(f"https://huggingface.co/rhasspy/piper-voices/tree/v1.0.0/{lang}/{code}", ["span"])
        d = ''.join([b.page_content for b in t2[1]]).split(' ')
        s = d[d.index('commits' if 'commits' in d else 'commit') + 1:]
        # s = [k for _, k in enumerate(d) if len(k) == 5 and '_' in k] # Nmaes
        print(s)
        data_PIPER[lang]["names"] = s
        for k in s:
            if k in data_PIPER['NL']:
                k += code[:2]
            data_PIPER["NL"][k] = [lang, code]
        return Result.ok()

    def get_LN(_):
        for k in data_PIPER["NL"]:
            print(k)
        return Result.ok(data_PIPER["NL"])

    def get_qulity(call_: CallingObject):
        name = call_.function_name
        if name not in data_PIPER["NL"]:
            return Result.default_user_error(f"invalid name {name}")
        lan, code = data_PIPER["NL"][name]
        t2 = get_text_from_urls_vue(f"https://huggingface.co/rhasspy/piper-voices/tree/v1.0.0/{lan}/{code}/{name}",
                                    ["span"])
        d = ''.join([b.page_content for b in t2[1]]).split(' ')
        s = d[d.index('commits' if 'commits' in d else 'commit') + 1:]
        options = ["high", "low", "medium"]
        avalabel_obtions = [k for k in options if k in s]
        print(avalabel_obtions)
        return Result.ok(avalabel_obtions)

    def _test_sampel(call_: CallingObject):
        name = call_.function_name
        options = ["high", "low", "medium"]
        if name not in data_PIPER["NL"]:
            return Result.default_user_error(f"invalid name {name}")
        lan, code = data_PIPER["NL"][name]
        option = call_.args[0].strip()
        if option not in options:
            return Result.default_user_error(f"invalid quality")
        url = f"https://huggingface.co/rhasspy/piper-voices/tree/v1.0.0/{lan}/{code}/{name}/{option}/samples"
        t2 = get_text_from_urls_vue(url,
                                    ["span"])
        d = ''.join([b.page_content for b in t2[1]]).split(' ')
        s = d[d.index('commits' if 'commits' in d else 'commit') + 1:]
        s1 = [k for k in s if k.endswith('.mp3')]
        s10 = s1[0]
        sampel_url = url + '/' + s10 + '?download=true'
        sampel_url = sampel_url.replace('tree', 'resolve')
        print(sampel_url)
        download_files([sampel_url], mpaths, "Download sampel for {name} {qulity}", print, filename=s10)
        time.sleep(5)
        with open(mpaths + '\\' + s10, 'rb') as f:
            audio_data = f.read()
        play_audio_bytes(audio_data)
        return Result.ok()

    def download_model(call_: CallingObject):
        name = call_.function_name
        options = ["high", "low", "medium"]
        if name not in data_PIPER["NL"]:
            return Result.default_user_error(f"invalid name {name}")
        lan, code = data_PIPER["NL"][name]
        option = call_.args[0].strip()
        if option not in options:
            return Result.default_user_error("invalid quality")

        url = f"https://huggingface.co/rhasspy/piper-voices/tree/v1.0.0/{lan}/{code}/{name}/{option}"
        t2 = get_text_from_urls_vue(url,
                                    ["span"])
        d = ''.join([b.page_content for b in t2[1]]).split(' ')
        s = d[d.index('commits' if 'commits' in d else 'commit') + 1:]
        s1 = [k for k in s if k.endswith('.onnx') or k.endswith('.json')]
        if len(s1) != 2:
            print(s1)
            return "invalid url"
        s10 = s1[0]
        s11 = s1[1]

        sampel_url = url + '/' + s10 + '?download=true'
        sampel_url = sampel_url.replace('tree', 'resolve')
        path_ = mpaths + f'{lan}/{code}/{option}/{name}'
        os.makedirs(path_, exist_ok=True)
        download_files([sampel_url], path_, "Download sampel for {name} {qulity}", print, filename=s10)

        sampel_url = url + '/' + s11 + '?download=true'
        sampel_url = sampel_url.replace('tree', 'resolve')
        download_files([sampel_url], path_, "Download sampel for {name} {qulity}", print, filename=s11)
        return Result.ok()

    def exit_(_):
        if 'main' in app.id:
            res = yes_no_dialog(
                title='Exit ToolBox',
                text='Do you want to Close the ToolBox?').run()
            app.alive = not res
        else:
            app.alive = False
        return Result.ok().set_origin("minicli::build-in")

    autocompletion_dict = {
        "exit": None,
        "list": None,
        "lanC": None,
        "names": None,
        "ac": None,
        "avalibal_c": None,
        "high": None,
        "low": None,
        "medium": None,
        "lisenv": None,
        "get": None,
    }
    bic = {
        "exit": exit_,
        "List_all_languages": list_all_l,
        "get_available_codes_by_lang_code": get_all_codes_by_lang,
        "get_name_by_code": get_name,
        "know_models": get_LN,
        "get_qulity": get_qulity,
        "lsen_to_sampel": _test_sampel,
        "get": download_model,
    }

    while app.alive:

        def get_rprompt():
            current_time: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return HTML(
                f'<b> App Infos: '
                f'{app.id} \nTime: {current_time}</b>')

        call = app.run_any(tbef.CLI_FUNCTIONS.USER_INPUT, completer_dict=autocompletion_dict,
                           get_rprompt=get_rprompt)

        print("", end="" + "start ->>\r")

        if call is None:
            continue

        if call.module_name == "open":
            autocompletion_dict = app.run_any(tbef.CLI_FUNCTIONS.UPDATE_AUTOCOMPLETION_MODS,
                                              autocompletion_dict=autocompletion_dict)

        running_instance = app.run_any(tbef.CLI_FUNCTIONS.CO_EVALUATE,
                                       obj=call,
                                       build_in_commands=bic)

    # options = ["samples", "low", "medium"]
    # download_files
    # avalabel_obtions = [k for k in options if k in s]
#
# print(avalabel_obtions)

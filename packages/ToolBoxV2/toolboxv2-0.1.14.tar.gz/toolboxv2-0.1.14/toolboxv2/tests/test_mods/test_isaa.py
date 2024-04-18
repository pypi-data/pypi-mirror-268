import json
import sys
import time
import unittest
from unittest.mock import patch, Mock, MagicMock
from bs4 import BeautifulSoup

from toolboxv2 import App, get_logger
from toolboxv2.mods import BROWSER
from toolboxv2.mods.isaa import Tools, Agents
from toolboxv2.mods.isaa.AgentUtils import get_ip, get_location, _extract_from_json, dilate_string
from toolboxv2.mods.isaa.Agents import AgentBuilder, Agent
from toolboxv2.mods.isaa.isaa_modi import (show_image_in_internet,
                                           browse_website, get_text_summary, get_hyperlinks, scrape_text,
                                           extract_hyperlinks, format_hyperlinks, scrape_links)
from toolboxv2.mods.isaa.module import extract_code

from toolboxv2.utils.toolbox import get_app


class TestIsaaBenchmarks(unittest.TestCase):
    isaa = None
    t0 = 0
    app = None

    @classmethod
    def setUpClass(cls):
        # Code, der einmal vor allen Tests ausgeführt wird
        cls.t0 = time.perf_counter()
        cls.app = App("test-TestIsaa")
        cls.app.mlm = "I"
        cls.app.debug = True
        cls.isaa: Tools = cls.app.get_mod('isaa')
        cls.isaa.load_keys_from_env()

    @classmethod
    def tearDownClass(cls):
        cls.app.remove_all_modules()
        cls.app.save_exit()
        cls.app.exit()
        cls.app.logger.info(f"Accomplished in {time.perf_counter() - cls.t0}")

    def setUp(self):
        self.app_mock = Mock()
        self.isaa = self.app.get_mod('isaa')

    def tearDown(self):
        self.isaa._on_exit()
        self.app.remove_mod('isaa')


class TestIsaa(unittest.TestCase):
    isaa = None
    t0 = 0
    app = None

    not_run = [
        'gpt-4',
        'gpt-3.5-turbo',
        'gpt-3.5-turbo-0613',
        'text-davinci-003',
        'gpt-4-0613',
        'code-davinci-edit-001',
        'text-curie-001',
        'text-babbage-001',
        'text-ada-001',
        'text-davinci-edit-001',
        'gpt-3.5-turbo-instruct',

        'google/flan-t5-small',
        'google/flan-t5-xxl',
        'databricks/dolly-v2-3b',
        'stabilityai/stablecode-instruct-alpha-3b',

        'gpt4all#GPT4All-13B-snoozy.ggmlv3.q4_0.bin',  # 5/
        'gpt4all#orca-mini-7b.ggmlv3.q4_0.bin',  # 4.5/10 :
        'gpt4all#orca-mini-3b.ggmlv3.q4_0.bin',  # for comm
        'gpt4all#wizardLM-13B-Uncensored.ggmlv3.q4_0.bin',
        'gpt4all#ggml-replit-code-v1-3b.bin',  # Hy ly crati
        'knkarthick/MEETING_SUMMARY'
    ]

    models = [
        'gpt4all#GPT4All-13B-snoozy.ggmlv3.q4_0.bin',  # 5/10 (summary/classify/pl_lv2 in : 13.75s
        'gpt4all#orca-mini-7b.ggmlv3.q4_0.bin',  # : 7.17s
        # 4.5/10 : Hily spesific if you have any questions related to programming or computer science, feel free to ask me! , classify
        'gpt4all#orca-mini-3b.ggmlv3.q4_0.bin',  # : 3.76s
        # for command exection and evalation prosseses 6/10 context classify (tool use) qa code summ
        'gpt4all#wizardLM-13B-Uncensored.ggmlv3.q4_0.bin',  # : 13.62s
        # Conversational and Thinking Sartegegs 7.4/10 summary classify   (q/a 1): py Lv2)
        'gpt4all#ggml-replit-code-v1-3b.bin',  # Hy ly crative # : 11.08s
    ]

    all4allModels = ['nous-hermes-13b.ggmlv3.q4_0.bin',
                     'GPT4All-13B-snoozy.ggmlv3.q4_0.bin',
                     'orca-mini-7b.ggmlv3.q4_0.bin',
                     'orca-mini-3b.ggmlv3.q4_0.bin',
                     'orca-mini-13b.ggmlv3.q4_0.bin',
                     'wizardLM-13B-Uncensored.ggmlv3.q4_0.bin',
                     'ggml-replit-code-v1-3b.bin',
                     'llama-2-7b-chat.ggmlv3.q4_0.bin'
                     ]
    # 18.10.2023 #'ggml-model-gpt4all-falcon-q4_0.bin',

    modes = []  # ["conversation", "tools", "talk", "free", "planning", "live"]
    agents = []  # ["self", "todolist", "search", "think", "TaskCompletion", "liveInterpretation", "summary", "thinkm", "code"]

    augment = {'tools':
                   {'lagChinTools': ['python_repl', 'requests_all', 'terminal', 'sleep',
                                     'wikipedia', 'llm-math', 'requests_get', 'requests_post',
                                     'requests_patch', 'requests_put', 'requests_delete'], 'huggingTools': [],
                    'Plugins': [], 'Custom': []}, 'Agents': {
        'self': {'name': 'self', 'mode': 'free', 'model_name': 'gpt-4', 'max_iterations': 6, 'verbose': True,
                 'personality': "\nResourceful: Isaa is able to efficiently utilize its wide range of capabilities and resources to assist the user.\nCollaborative: Isaa is work seamlessly with other agents, tools, and systems to deliver the best possible solutions for the user.\nEmpathetic: Isaa is understand and respond to the user's needs, emotions, and preferences, providing personalized assistance.\nInquisitive: Isaa is continually seek to learn and improve its knowledge base and skills, ensuring it stays up-to-date and relevant.\nTransparent: Isaa is open and honest about its capabilities, limitations, and decision-making processes, fostering trust with the user.\nVersatile: Isaa is adaptable and flexible, capable of handling a wide variety of tasks and challenges.\n                  ",
                 'goals': "Isaa's primary goal is to be a digital assistant designed to help the user with various tasks and challenges by leveraging its diverse set of capabilities and resources.",
                 'token_left': 3077, 'temperature': 0.06, '_stream': False, '_stream_reset': False,
                 'stop_sequence': ['\n\n\n', 'Execute:', 'Observation:', 'User:'], 'completion_mode': 'text',
                 'add_system_information': True, 'init_mem_state': False, 'binary_tree': None,
                 'agent_type': 'structured-chat-zero-shot-react-description',
                 'tools': ['memory_search', 'search_web', 'write-production-redy-code', 'mode_switch', 'think',
                           'image-generator', 'mini_task', 'memory', 'save_data_to_memory', 'crate_task',
                           'optimise_task', 'execute-chain', 'Python REPL', 'terminal', 'sleep', 'Google Search',
                           'DuckDuckGo Search', 'Wikipedia', 'Calculator', 'requests_get', 'requests_post',
                           'requests_patch', 'requests_put', 'requests_delete'], 'task_list': [],
                 'task_list_done': [], 'step_between': '', 'pre_task': None, 'task_index': 0},
        'categorize': {'name': 'categorize', 'mode': 'free', 'model_name': 'gpt-3.5-turbo-0613',
                       'max_iterations': 2, 'verbose': True, 'personality': '', 'goals': '', 'token_left': 4096,
                       'temperature': 0.06, '_stream': False, '_stream_reset': False,
                       'stop_sequence': ['\n\n\n', 'Observation:', 'Execute:'], 'completion_mode': 'text',
                       'add_system_information': True, 'init_mem_state': False, 'binary_tree': None,
                       'agent_type': 'structured-chat-zero-shot-react-description',
                       'tools': ['memory', 'save_data_to_memory', 'crate_task', 'optimise_task'], 'task_list': [],
                       'task_list_done': [], 'step_between': '', 'pre_task': None, 'task_index': 0},
        'think': {'name': 'think', 'mode': 'free', 'model_name': 'gpt-4', 'max_iterations': 1, 'verbose': True,
                  'personality': '', 'goals': '', 'token_left': 1347, 'temperature': 0.06, '_stream': True,
                  '_stream_reset': False, 'stop_sequence': ['\n\n\n'], 'completion_mode': 'chat',
                  'add_system_information': True, 'init_mem_state': False, 'binary_tree': None,
                  'agent_type': 'structured-chat-zero-shot-react-description',
                  'tools': ['memory', 'save_data_to_memory', 'crate_task', 'optimise_task'], 'task_list': [],
                  'task_list_done': [], 'step_between': '', 'pre_task': None, 'task_index': 0},
        'summary': {'name': 'summary', 'mode': 'free', 'model_name': 'gpt4all#ggml-model-gpt4all-falcon-q4_0.bin',
                    'max_iterations': 1, 'verbose': True, 'personality': '', 'goals': '', 'token_left': 4096,
                    'temperature': 0.06, '_stream': False, '_stream_reset': False, 'stop_sequence': ['\n\n'],
                    'completion_mode': 'chat', 'add_system_information': True, 'init_mem_state': False,
                    'binary_tree': None, 'agent_type': 'structured-chat-zero-shot-react-description',
                    'tools': ['memory', 'save_data_to_memory', 'crate_task', 'optimise_task'], 'task_list': [],
                    'task_list_done': [], 'step_between': '',
                    'pre_task': 'Act as an summary expert your specialties are writing summary. you are known to think in small and detailed steps to get the right result. Your task :',
                    'task_index': 0}}, 'customFunctions': {}, 'tasks': {}}  # 'google-search','ddg-search',

    @classmethod
    def setUpClass(cls):
        # Code, der einmal vor allen Tests ausgeführt wird
        cls.t0 = time.perf_counter()
        cls.app = App("test-TestIsaa")
        cls.app.mlm = "I"
        cls.app.debug = True
        cls.isaa: Tools = cls.app.get_mod('isaa')
        cls.isaa.load_keys_from_env()
        if "OPENAI_API_KEY" in cls.isaa.config:  # in cloud 0
            cls.models += [
                # 'gpt-4', 'text-davinci-003', 'gpt-3.5-turbo-0613',
                # 'text-curie-001',
                # 'text-babbage-001',
                # 'text-ada-001',
                # 'text-davinci-edit-001',
                # 'gpt-3.5-turbo-instruct',
                # 'gpt-3.5-turbo'', 'gpt-4-0613', 'code-davinci-edit-001'  #code- usles
            ]

        if "HUGGINGFACEHUB_API_TOKEN" in cls.isaa.config:
            cls.models += [
                # 'google/flan-t5-small',  # 2/10 ~ ? Knowledge  classify ?eval? : 0.48s
                # 'facebook/bart-large-cnn', # 0/10 spoling informtions Prompt?
                # 'tiiuae/falcon-40b', # -1
                # 'google/flan-t5-xxl',
                # eglisch text bot not mutch context 1/10 classify  tool use json to  (q/a 2) :: 0.51s
                # 'databricks/dolly-v2-3b',  # Knowledge 0/10 : 0.57s
                ## 'stabilityai/FreeWilly2', # to big
                ## 'jondurbin/airoboros-l2-70b-gpt4-1.4.1',
                ## 'TheBloke/llama-2-70b-Guanaco-QLoRA-fp16',
                ## 'TheBloke/gpt4-alpaca-lora_mlp-65B-HF',
                ## 'meta-llama/Llama-2-70b-hf',
                ## 'TheBloke/guanaco-65B-HF',
                ## 'huggyllama/llama-65b',
                # 'NousResearch/Nous-Hermes-Llama2-13b', # slow af | to big  No output
                # 'YeungNLP/firefly-llama2-13b', # slow ... nop
                # 'mosaicml/mpt-30b-chat',
                # 'openaccess-ai-collective/wizard-mega-13b',
                # 'deutsche-telekom/bert-multi-english-german-squad2',
                # conversation 'PygmalionAI/pygmalion-6b',
                # 'meta-llama/Llama-2-7b',
                # 'knkarthick/MEETING_SUMMARY',  # summary (q/a 12 : 0.20s
                # 'TheBloke/OpenAssistant-Llama2-13B-Orca-8K-3319-GGML',
                # 'TheBloke/Llama-2-7b-chat-fp16',
                # 'TheBloke/open-llama-7B-v2-open-instruct-GPTQ',
                # 'TheBloke/open-llama-13b-open-instruct-GPTQ',
                # 'TheBloke/falcon-7b-instruct-GPTQ',
                # 'TheBloke/Llama-2-7b-Chat-GPTQ',
                'stabilityai/stablecode-instruct-alpha-3b',
                'stabilityai/stablecode-completion-alpha-3b',
                'WizardLM/WizardCoder-Python-7B-V1.0',
                'WizardLM/WizardCoder-Python-13B-V1.0',
                'WizardLM/WizardMath-13B-V1.0',
                'WizardLM/WizardLM-7B-V1.0',
                'WizardLM/WizardCoder-1B-V1.0',
                'WizardLM/WizardLM-13B-V1.2',

            ]

        cls.isaa.config["DEFAULTMODEL0"] = "gpt-3.5-turbo-0613"  # "gpt-4"
        cls.isaa.config["DEFAULTMODEL1"] = "gpt-3.5-turbo-0613"  # "gpt-3.5-turbo-0613"
        cls.isaa.config["DEFAULTMODEL2"] = "text-curie-001"  # "text-davinci-003"
        cls.isaa.config["DEFAULTMODELCODE"] = "code-davinci-edit-001"  # "code-davinci-edit-001"
        cls.isaa.config["DEFAULTMODELSUMMERY"] = "text-curie-001"  # "text-curie-001"

    @classmethod
    def tearDownClass(cls):
        cls.app.remove_all_modules()
        cls.app.save_exit()
        cls.app.exit()
        cls.app.logger.info(f"Accomplished in {time.perf_counter() - cls.t0}")

    def setUp(self):
        self.app_mock = Mock()
        self.isaa = self.app.get_mod('isaa')

    def tearDown(self):
        self.isaa._on_exit()
        self.app.remove_mod('isaa')


class TestIsaaUnit(unittest.TestCase):

    def __init__(self, methodName: str = ...):
        super().__init__(methodName)
        self.app = get_app("test-IsaaUnit")

    @patch('requests.get')
    def test_get_ip(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'ip': '123.123.123.123'}
        mock_get.return_value = mock_response

        result = get_ip()
        self.assertEqual(result, '123.123.123.123')

    @patch('requests.get')
    def test_get_location(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {'city': 'Berlin', 'region': 'Berlin', 'country_name': 'Germany'}
        mock_get.return_value = mock_response

        result = get_location()
        try:
            res = result.result(timeout=15)
            self.assertEqual(res, 'city: Berlin,region: Land Berlin,country: Germany,')
        except Exception:
            pass

    def test_extract_code(self):
        x = 'Hallo 123 ```python\nprint("Hello, World!")\n```asdadw'
        result = extract_code(x)
        self.assertEqual(result, ('print("Hello, World!")\n', 'python'))

    # def test_genrate_image(self):
    #     mock_app = self.app
    #     inputs = {}
    #     model = 'stability-ai/stable-diffusion'
    #     with ValueError as err:
    #         res = genrate_image(inputs, mock_app, model)
    #
    #     print(res)
    @patch('os.system')
    def test_show_image_in_internet(self, mock_system):
        image_url = 'http://example.com/image.jpg'
        show_image_in_internet(image_url, BROWSER)
        mock_system.assert_called_once_with(f'start {BROWSER} {image_url}')

    def test_dilate_string(self):
        test_string = """
Zum Inhalt springen
Menü
Wohnen
Klimawandel
Krieg in der Ukraine
Alle Themen
Blog
TEILCHEN
Im Netz verstecken sich kleine Schätze – ZEIT ONLINE findet sie.
Über die Autoren
Janis Dietz22. Januar 2021
Einmal quer durch Havanna, bitte!

Plötzlich ist man in Havanna, Rio oder Jekatarinburg – „Drive & Listen“ macht es möglich. Foto: Andrei Luca/Youtube
Drive & Listen ist eine einfache aber sehnsuchtsschürende Anwendung, mit der man von zu Hause aus durch fremde Straßen fahren kann. Man klickt in einem Drop-Down-Menü auf eine von über 50 Städtenamen und schon ist man im Auto unterwegs, mitten in einer unbekannten Großstadt und begleitet von lokalen Radiosendern. Ich entscheide mich für die kubanische Hauptstadt. (Was hilft besser gegen Corona-Winterblues als karibisches Flair?) Und plötzlich fahre ich durch Havanna. Links das Meer, auf der rechten Seite ziehen die leicht verfallenen ehemaligen Prachtbauten an mir vorbei. Ab und an überhole ich einen alten Chevrolet oder Buick. Das Radio dudelt vor sich hin. Am liebsten würde ich jetzt ein Fenster öffnen und mein Gesicht in den karibischen Wind halten.  Weiter„Einmal quer durch Havanna, bitte!“


Dennis Schmees14. Januar 2021
Pflegekräfte in der Pandemie
„Nichts hätte mich darauf vorbereiten können“
Empfohlener redaktioneller Inhalt
An dieser Stelle finden Sie externen Inhalt, der den Artikel ergänzt. Sie können sich externe Inhalte mit einem Klick anzeigen lassen und wieder ausblenden.
  Externer Inhalt
Ich bin damit einverstanden, dass mir externe Inhalte angezeigt werden. Damit können personenbezogene Daten an Drittplattformen übermittelt werden. Mehr dazu in unserer Datenschutzerklärung.

Zu Beginn der Corona-Pandemie haben sich in einem Pflegeheim in Hessen mehr als zwei Dutzend Bewohnerinnen, Bewohner und Pflegekräfte mit dem Virus infiziert. Drei Menschen sind an der Erkrankung gestorben. Um das Erlebte zu verarbeiten, hat eine Krankenschwester ein Gedicht geschrieben.

Weiter„„Nichts hätte mich darauf vorbereiten können““


ÜBER DIESES BLOG
Nicht jedes Video ist eine Nachricht, nicht jede Grafik lohnt für einen Artikel. Wir teilen sie trotzdem via Twitter, Facebook oder sprechen mit Freunden darüber. Weil sie sehenswert sind, unterhaltsam und informativ. Damit sie nicht einfach wieder verschwinden, sammelt ZEIT ONLINE im Teilchen-Blog regelmäßig Kleines, aber Feines aus dem Netz. Folgen Sie dem Blog auch auf Twitter unter #Teilchen.
Andreas Loos22. Dezember 2020
Dieses Mathe-Game lässt Sie den Weihnachtsbaum vergessen
Weihnachten und Corona
Vorsicht, Suchtgefahr! © Screenshot imaginary.org
Im Weltraum gehen Coronaviren ja vermutlich schnell kaputt, wegen UV-Strahlung, Kälte und dergleichen. Und für einen einzelnen Astronauten allein – obendrein im Anzug – besteht überhaupt keine Ansteckungsgefahr. Insofern ist das Spiel, das Mathematiker für Weihnachten online gestellt haben, perfekt coronakonform.

Weiter„Dieses Mathe-Game lässt Sie den Weihnachtsbaum vergessen“


Dennis Schmees11. Dezember 2020
Doktor trotz Prüfungsangst
Empfohlener redaktioneller Inhalt
An dieser Stelle finden Sie externen Inhalt, der den Artikel ergänzt. Sie können sich externe Inhalte mit einem Klick anzeigen lassen und wieder ausblenden.
  Externer Inhalt
Ich bin damit einverstanden, dass mir externe Inhalte angezeigt werden. Damit können personenbezogene Daten an Drittplattformen übermittelt werden. Mehr dazu in unserer Datenschutzerklärung.

Schon die Vorstellung, einen Vortrag zu halten, lässt viele Menschen feuchte Hände bekommen. Das ist auch in Zeiten sozialer Distanz und Zoom-Meetings nicht anders. Ein Doktorand hat seinen Herzschlag vor, während und nach der Verteidigung seiner Doktorarbeit gemessen. Das Ergebnis: Ruhe zu bewahren ist trotz Anspannung möglich – und auch Freude sorgt für Herzrasen.

Weiter„Doktor trotz Prüfungsangst“


Tobias Dorfer1. Dezember 2020
Wenn Ärzte zu Tröstern werden
Corona-Intensivstation
Der Arzt Joseph Varon tröstet im United Memorial Medical Center in Houston an Thanksgiving einen Corona-Patienten. © Go Nakamura/Getty Images
Ein älterer Mann vergräbt seinen Kopf in den Armen eines Arztes. Er wird im United Memorial Medical Center in der US-Metropole Houston wegen Covid-19 behandelt. Der Arzt Joseph Varon hatte ihn am 26. November, dem Tag, an dem in den USA Thanksgiving gefeiert wird, in seinem Bett gefunden, weinend und um Hilfe rufend: „Ich möchte mit meiner Frau zusammen sein“, hatte der Mann gesagt. Varon kann nicht mehr tun als den Mann zu trösten.

Weiter„Wenn Ärzte zu Tröstern werden“


Dennis Schmees4. November 2020
World of Pandemieforschung
Empfohlener redaktioneller Inhalt
An dieser Stelle finden Sie externen Inhalt, der den Artikel ergänzt. Sie können sich externe Inhalte mit einem Klick anzeigen lassen und wieder ausblenden.
  Externer Inhalt
Ich bin damit einverstanden, dass mir externe Inhalte angezeigt werden. Damit können personenbezogene Daten an Drittplattformen übermittelt werden. Mehr dazu in unserer Datenschutzerklärung.

Eine virtuelle Pandemie verbreitet sich im Jahr 2005 im Spiel World of Warcraft. Die Entdeckungen, die die epidemiologische Forschung anschließend machte, lässt uns bis heute echte Pandemien besser verstehen.

Weiter„World of Pandemieforschung“


Tobias Dorfer27. Oktober 2020
Kasachstan
Wie Kasachstan vom „Borat“-Boom profitieren möchte
Empfohlener redaktioneller Inhalt
An dieser Stelle finden Sie externen Inhalt, der den Artikel ergänzt. Sie können sich externe Inhalte mit einem Klick anzeigen lassen und wieder ausblenden.
  Externer Inhalt
Ich bin damit einverstanden, dass mir externe Inhalte angezeigt werden. Damit können personenbezogene Daten an Drittplattformen übermittelt werden. Mehr dazu in unserer Datenschutzerklärung.

Frauenfeindlich, homophob, antisemitisch – so beschreibt der (fiktionale) Journalist Borat Sagdiyev im gleichnamigen Kinofilm sein Heimatland Kasachstan. Ein Land, das so rückständig beschrieben wird, wäre fast schon ein Fall für die Reisewarnungsabteilung des Auswärtigen Amtes. Und dennoch macht die Tourismusbehörde Kasachstans nun aus den zweifelhaften Zuschreibungen Gold.

Weiter„Wie Kasachstan vom „Borat“-Boom profitieren möchte“


Sasan Abdi-Herrle17. September 2020
Joko und Klaas machen das Grauen von Moria sichtbar
Empfohlener redaktioneller Inhalt
An dieser Stelle finden Sie externen Inhalt, der den Artikel ergänzt. Sie können sich externe Inhalte mit einem Klick anzeigen lassen und wieder ausblenden.
  Externer Inhalt
Ich bin damit einverstanden, dass mir externe Inhalte angezeigt werden. Damit können personenbezogene Daten an Drittplattformen übermittelt werden. Mehr dazu in unserer Datenschutzerklärung.

Verteilungsschlüssel, EU-Türkei-Abkommen, „Koalition der Willigen“: Das Flüchtlingsthema kann schnell einen virtuellen Charakter bekommen, wenn man es aus der sinnbildlichen „warmen Stube“ verfolgt. Dabei geht es bei aller komplexen Politik doch um Menschen. Die Entertainer Joko Winterscheidt und Klaas Heufer-Umlauf haben dazu beigetragen, das konkrete Grauen der Flüchtlinge und Migranten auf Lesbos sichtbarer zu machen. Dazu nutzten sie die Sendezeit, die sie am Dienstag „gewonnen“ hatten: Die Kurzdoku A Short Story of Moria über die Lage auf Lesbos lief am Mittwochabend zur Primetime auf ProSieben.

Weiter„Joko und Klaas machen das Grauen von Moria sichtbar“


Dennis Schmees2. September 2020
US-Wahlkampf
Joe Biden, der Präsident von Animal Crossing
Empfohlener redaktioneller Inhalt
An dieser Stelle finden Sie externen Inhalt, der den Artikel ergänzt. Sie können sich externe Inhalte mit einem Klick anzeigen lassen und wieder ausblenden.
  Externer Inhalt
Ich bin damit einverstanden, dass mir externe Inhalte angezeigt werden. Damit können personenbezogene Daten an Drittplattformen übermittelt werden. Mehr dazu in unserer Datenschutzerklärung.

Joe Bidens digitaler Wahlkampf geht in die nächste Runde. Während Donald Trump trotz Pandemie weiter große Wahlveranstaltungen abhält, setzen Joe Biden und Kamala Harris auf Livestreams und nun auch Videospiele. Weiter„Joe Biden, der Präsident von Animal Crossing“


Tobias Dorfer21. August 2020
„Ohne Joe Biden würde ich jetzt nicht zu Ihnen sprechen“
Empfohlener redaktioneller Inhalt
An dieser Stelle finden Sie externen Inhalt, der den Artikel ergänzt. Sie können sich externe Inhalte mit einem Klick anzeigen lassen und wieder ausblenden.
  Externer Inhalt
Ich bin damit einverstanden, dass mir externe Inhalte angezeigt werden. Damit können personenbezogene Daten an Drittplattformen übermittelt werden. Mehr dazu in unserer Datenschutzerklärung.

Der digitale Parteitag der US-Demokraten war in vielerlei Hinsicht bemerkenswert. Es waren die Tage der großen Worte. Von Biden selbst. Von Michelle Obama. Von Barack Obama. Von der Vizepräsidentschaftskandidatin Kamala Harris. Und am Ende auch von einem 13 Jahre alten Jungen aus New Hampshire.

Weiter„„Ohne Joe Biden würde ich jetzt nicht zu Ihnen sprechen““



1 / 2 / … / 122 NÄCHSTE SEITE


NEUESTE TEILCHEN
Einmal quer durch Havanna, bitte!
„Nichts hätte mich darauf vorbereiten können“
Dieses Mathe-Game lässt Sie den Weihnachtsbaum vergessen
Doktor trotz Prüfungsangst
Wenn Ärzte zu Tröstern werden
DIESES BLOG DURCHSUCHEN
Suche

Nach oben
Impressum Hilfe & Kontakt Unternehmen Karriere Presse Jobs Shop Inserieren Mediadaten
Bildrechte Rechte & Lizenzen AGB Datenschutz Privacy Einstellungen Cookies & Tracking Abo kündigen
        """
        res = dilate_string(test_string, 0, 2, 0)
        res1 = dilate_string(test_string, 1, 2, 0)
        res2 = dilate_string(test_string, 2, 2, 0)
        res3 = dilate_string(test_string, 3, 2, 0)
        print(len(test_string), len(res), len(res1), len(res2), len(res3), len(res) + len(res1) + len(res2) + len(res3))
        self.assertGreater(len(test_string), len(res))
        self.assertGreater(len(test_string), len(res1))
        self.assertGreater(len(test_string), len(res2))
        self.assertGreater(len(test_string), len(res3))

        first_itter = dilate_string(test_string, 0, 2, 0)
        second_itter = dilate_string(first_itter, 0, 2, 0)

        print(len(second_itter))

        first_itter_ab = dilate_string(test_string, 2, 2, 0)
        second_itter_ab = dilate_string(first_itter_ab, 0, 2, 0)

        print(len(second_itter_ab))

import datetime
import psutil

from prompt_toolkit import HTML
from prompt_toolkit.shortcuts import set_title, yes_no_dialog

from toolboxv2 import App, Result, tbef
from toolboxv2.utils import show_console
from toolboxv2.utils.extras.Style import cls
from toolboxv2.utils.system.types import CallingObject

NAME = 'cli'


async def run(app: App, args):
    try:
        set_title(f"ToolBox : {app.version}")
    except:
        pass
    threaded = False

    def bottom_toolbar():
        return HTML(f'Hotkeys shift:s control:c  <b><style bg="ansired">s+left</style></b> helper info '
                    f'<b><style bg="ansired">c+space</style></b> Autocompletion tips '
                    f'<b><style bg="ansired">s+up</style></b> run in shell')

    async def exit_(_):
        print("EXITING")
        if app.debug:
            app.hide_console()
        app.alive = False
        return Result.ok().set_origin("minicli::build-in")

    def set_debug_mode(call_: CallingObject) -> Result:
        if not call_.function_name:
            return (Result.default_user_error(info=f"sdm (Set Debug Mode) needs at least one argument on or off\napp is"
                                                   f" {'' if app.debug else 'NOT'} in debug mode")
                    .set_origin("minicli::build-in"))
        if call_.function_name.lower() == "on":
            app.debug = True
        elif call_.function_name.lower() == "off":
            app.debug = False
        else:
            return Result.default_user_error(info=f"{call_.function_name} != on or off").set_origin("minicli::build-in")
        return Result.ok(info=f"New Debug Mode {app.debug}").set_origin("minicli::build-in")

    def hr(call_: CallingObject) -> Result:
        if not call_.function_name:
            app.remove_all_modules()
            app.load_all_mods_in_file()
        if call_.function_name in app.functions:
            app.remove_mod(call_.function_name)
            if not app.save_load(call_.function_name):
                return Result.default_internal_error().set_origin("minicli::build-in")
        return Result.ok().set_origin("minicli::build-in")

    def open_(call_: CallingObject) -> Result:
        if not call_.function_name:
            app.load_all_mods_in_file()
            return Result.default_user_error(info="No module specified").set_origin("minicli::build-in")
        if not app.save_load(call_.function_name):
            return Result.default_internal_error().set_origin("minicli::build-in")
        return Result.ok().set_origin("minicli::build-in")

    def close_(call_: CallingObject) -> Result:
        if not call_.function_name:
            app.remove_all_modules()
            return Result.default_user_error(info="No module specified").set_origin("minicli::build-in")
        if not app.remove_mod(call_.function_name):
            return Result.default_internal_error().set_origin("minicli::build-in")
        return Result.ok().set_origin("minicli::build-in")

    def run_(call_: CallingObject) -> Result:
        if not call_.function_name:
            return (Result.default_user_error(info=f"Avalabel are : {list(app.runnable.keys())}")
                    .set_origin("minicli::build-in"))
        if call_.function_name in app.runnable:
            app.run_runnable(call_.function_name)
            return Result.ok().set_origin("minicli::build-in")
        return Result.default_user_error("404").set_origin("minicli::build-in")

    helper_exequtor = [None]

    def remote(call_: CallingObject) -> Result:
        if not call_.function_name:
            return Result.default_user_error(info="add keyword local or port and host").set_origin("minicli::build-in")
        if call_.function_name != "local":
            app.args_sto.host = call_.function_name
        if call_.kwargs:
            print("Adding", call_.kwargs)
        status, sender, receiver_que = app.run_runnable("daemon", as_server=False, programmabel_interface=True)
        if status == -1:
            return (Result.default_internal_error(info="Failed to connect, No service available")
                    .set_origin("minicli::build-in"))

        def remote_exex_helper(calling_obj: CallingObject):

            kwargs = {
                "mod_function_name": (calling_obj.module_name, calling_obj.function_name)
            }
            if calling_obj.kwargs:
                kwargs = kwargs.update(calling_obj.kwargs)

            if calling_obj.module_name == "exit":
                helper_exequtor[0] = None
                sender({'exit': True})
            sender(kwargs)
            while receiver_que.not_empty:
                print(receiver_que.get())

        helper_exequtor[0] = remote_exex_helper

        return Result.ok().set_origin("minicli::build-in")

    def cls_(_):
        cls()
        return Result.ok(info="cls").set_origin("minicli::build-in")

    def toggle_threaded(_):
        global threaded
        threaded = not threaded
        return Result.ok(info=f"in threaded mode {threaded}").set_origin("minicli::build-in").print()

    def infos(_):
        app.print_functions()
        return Result.ok(info=f"").set_origin("minicli::build-in")

    def colose_console(_):
        show_console(False)
        return Result.ok(info=f"").set_origin("minicli::build-in")

    def open_console(_):
        app.show_console(True)
        return Result.ok(info=f"").set_origin("minicli::build-in")

    bic = {
        "exit": exit_,
        "cls": cls_,
        "sdm:set_debug_mode": set_debug_mode,
        "open": open_,
        "close": close_,
        "run": run_,
        "infos": infos,
        "reload": hr,
        "remote": remote,
        "hide_console": colose_console,
        "show_console": open_console,
        "toggle_threaded": toggle_threaded,
        "..": lambda x: Result.ok(x),
    }

    all_modes = app.get_all_mods()

    # set up Autocompletion

    autocompletion_dict = {}
    autocompletion_dict = app.run_any(tbef.CLI_FUNCTIONS.UPDATE_AUTOCOMPLETION_LIST_OR_KEY, list_or_key=bic,
                                      autocompletion_dict=autocompletion_dict)

    autocompletion_dict_ = app.get_autocompletion_dict()

    if autocompletion_dict is None:
        autocompletion_dict = {}

    if autocompletion_dict_ is not None:
        autocompletion_dict = {**autocompletion_dict, **autocompletion_dict_}

    autocompletion_dict["sdm:set_debug_mode"] = {arg: None for arg in ['on', 'off']}
    autocompletion_dict["open"] = autocompletion_dict["close"] = autocompletion_dict["reload"] = \
        {arg: None for arg in all_modes}
    autocompletion_dict["run"] = {arg: None for arg in list(app.runnable.keys())}

    active_modular = ""

    running_instance = None
    call = CallingObject.empty()
    running = True
    while running:
        # Get CPU usage
        cpu_usage = psutil.cpu_percent(interval=1)

        # Get memory usage
        memory_usage = psutil.virtual_memory().percent

        # Get disk usage
        disk_usage = psutil.disk_usage('/').percent

        def get_rprompt():
            current_time: str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return HTML(
                f'<b> App Infos: '
                f'{app.id} \nCPU: {cpu_usage}% Memory: {memory_usage}% Disk :{disk_usage}%\nTime: {current_time}</b>')

        call = app.run_any(tbef.CLI_FUNCTIONS.USER_INPUT, completer_dict=autocompletion_dict,
                           get_rprompt=get_rprompt, bottom_toolbar=bottom_toolbar, active_modul=active_modular)

        print("", end="" + "start ->>\r")

        if call is None:
            continue

        if call.module_name == "open":
            autocompletion_dict = app.run_any(tbef.CLI_FUNCTIONS.UPDATE_AUTOCOMPLETION_MODS,
                                              autocompletion_dict=autocompletion_dict)

        running_instance = await app.run_any(tbef.CLI_FUNCTIONS.CO_EVALUATE,
                                             obj=call,
                                             build_in_commands=bic,
                                             threaded=threaded,
                                             helper=helper_exequtor[0])

        print("", end="" + "done ->>\r")
        running = app.alive

    if hasattr(app, 'timeout'):
        app.timeout = 2

    if running_instance is not None:
        print("Closing running instance")
        running_instance.join()
        print("Done")

    try:
        set_title("")
    except:
        pass
    app.exit()

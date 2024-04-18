import os

from toolboxv2.mods.CloudM.UI.vue import MyApp

if __name__ == "__main__":
    import threading

    #os.system(f"streamlit run {os.path.abspath(__file__).replace('runner', 'vue')} -")
    app = MyApp()
    app.mainloop()

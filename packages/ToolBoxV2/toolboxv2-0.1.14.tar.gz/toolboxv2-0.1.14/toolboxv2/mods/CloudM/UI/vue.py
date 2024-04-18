import threading

import customtkinter as ctk
import streamlit as st
import os
from PIL import Image

from toolboxv2 import get_app
from toolboxv2.mods.CloudM.UI.backend import get_user

from dotenv import dotenv_values, set_key
import os

from toolboxv2.mods.SocketManager import get_local_ip, get_public_ip


class EnvEditor(ctk.CTkScrollableFrame):
    def __init__(self, master, env_path, **kwargs):
        super().__init__(master, **kwargs)
        self.env_path = env_path
        self.env_data = dotenv_values(env_path)
        self.build_ui()

    def build_ui(self):
        row = 0
        for key, value in self.env_data.items():
            ctk.CTkLabel(self, text=key).grid(row=row, column=0, pady=5, sticky="w")
            entry = ctk.CTkEntry(self, show="*", width=200)
            entry.insert(0, value)
            entry.grid(row=row, column=1, pady=5, padx=5)
            show_button = ctk.CTkButton(self, text="Show", command=lambda e=entry: self.toggle_show(e))
            show_button.grid(row=row, column=2, pady=5, padx=5)
            row += 1

        # Eingabefelder für neue Schlüssel-Wert-Paare
        self.new_key_entry = ctk.CTkEntry(self)
        self.new_key_entry.grid(row=row, column=0, pady=5, padx=5)
        self.new_value_entry = ctk.CTkEntry(self)
        self.new_value_entry.grid(row=row, column=1, pady=5, padx=5)
        add_button = ctk.CTkButton(self, text="Add", command=self.add_key_value)
        add_button.grid(row=row, column=2, pady=5, padx=5)

    def toggle_show(self, entry):
        if entry.cget("show") == "*":
            entry.configure(show="")
        else:
            entry.configure(show="*")

    def add_key_value(self):
        key = self.new_key_entry.get()
        value = self.new_value_entry.get()
        if key and value:
            self.env_data[key] = value
            set_key(self.env_path, key, value)
            self.new_key_entry.delete(0, "end")
            self.new_value_entry.delete(0, "end")
            self.build_ui()  # UI neu aufbauen, um den neuen Schlüssel anzuzeigen


class MyApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.token_entry = None
        self.name_entry = None
        self.entry_email = None
        self.user = None
        self.title('Meine Anwendung')
        self.geometry('800x600')
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "assets")
        os.path.join(image_path, "img.png")
        logo_image = ctk.CTkImage(dark_image=Image.open(os.path.join(image_path, "img.png")),
                                  size=(740, 158))

        label = ctk.CTkLabel(self, image=logo_image, text="")
        label.pack(expand=True)

        # Tab Control
        self.tab_control = ctk.CTkTabview(self)
        self.tab_control.pack(fill="both", expand=True, padx=10, pady=10)

        # Infos Tab
        self.tab_infos = self.tab_control.add(name="Infos")
        self.infos_tab()
        # running instances local with pid

        # System Tab
        # self.tab_system = self.tab_control.add(name="System")
        # ctk.CTkLabel(self.tab_system, text="System-Bereich").pack(pady=20)
        # download mod install mods and runnabel / manage them remove
        # add runnabel to defauld start and rm

        # Settings Tab
        self.tab_settings = self.tab_control.add(name="Settings")
        ctk.CTkLabel(self.tab_settings, text="Settings-Bereich").pack(pady=20)
        self.env_editor()
        # clonfig the .env file add keys and co settings

    # def display_user_info(self):
    #
    #    ctk.CTkLabel(self.tab_user, text="User-Bereich").pack(pady=20)
    #    user = get_user("asd")
    #    if user is None:
    #        # Login Formular
    #        ctk.CTkLabel(self.tab_user, text="Name:").pack()
    #        name_entry = ctk.CTkEntry(self.tab_user)
    #        name_entry.pack()
    #
    #        ctk.CTkLabel(self.tab_user, text="Token:").pack()
    #        token_entry = ctk.CTkEntry(self.tab_user)
    #        token_entry.pack()
    #
    #        login_button = ctk.CTkButton(self.tab_user, text="Log In", command=self.login)
    #        login_button.pack()
    #
    #        create_acc_link = ctk.CTkLabel(self.tab_user, text="Create Account", cursor="hand2")
    #        create_acc_link.pack()
    #        create_acc_link.bind("<Button-1>", lambda e: self.open_create_account_page())
    #    else:
    #        # Benutzerdaten anzeigen
    #        ctk.CTkLabel(self.tab_user, text=f"Name: {user.name}").pack()
    #        ctk.CTkLabel(self.tab_user, text=f"Email: {user.email}").pack()
    #        ctk.CTkLabel(self.tab_user, text=f"Level: {user.level}").pack()
    #
    #        if user.name == "root":
    #            # Root-Benutzer Optionen
    #            ctk.CTkLabel(self.tab_user, text="Root User").pack()
    #            ctk.CTkButton(self.tab_user, text="Add User", command=self.add_user).pack()
    #            ctk.CTkButton(self.tab_user, text="Remove User", command=self.remove_user).pack()
    #            ctk.CTkButton(self.tab_user, text="Set User Level", command=self.set_user_level).pack()

    # def clear(self):
    #     pass
    #     for widget in self.tab_infos.winfo_children():
    #         widget.destroy()
    #     # for widget in self.tab_system.winfo_children():
    #     #     widget.destroy()
    #     for widget in self.tab_settings.winfo_children():
    #         widget.destroy()

    def infos_tab(self):

        ctk.CTkLabel(self.tab_infos, text="App-Infos").pack(pady=20)
        app = get_app(from_='cm_ui')
        ctk.CTkLabel(self.tab_infos, text=f"{app.id}").pack(pady=0)
        ctk.CTkLabel(self.tab_infos, text=f"Version: {app.version}").pack(pady=0)
        ctk.CTkLabel(self.tab_infos, text=f"Local IP: {get_local_ip()}").pack(pady=0)
        ctk.CTkLabel(self.tab_infos, text=f"Public IP: {get_public_ip()}").pack(pady=0)

    def env_editor(self):
        # self.clear()
        env_editor = EnvEditor(self.tab_settings, r"..\.env", width=680, height=280)
        env_editor.pack(pady=20, padx=20)


def main():
    # Tab Auswahl
    image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "assets")
    st.image(Image.open(os.path.join(image_path, "img.png")))
    print(os.path.join(image_path, "img.png"))
    User, Mods, System = st.tabs(['User', 'Mods', 'System'])

    with User:
        st.header("User-Bereich")
        user_token = st.text_input("User Token")
        # Hier könnten weitere Widgets für den User-Bereich hinzugefügt werden
        user = get_user(user_token)
        if user is None:
            # Login Formular
            name = st.text_input("Name")
            token = st.text_input("Token")
            if st.button("Log In"):
                # Implementiere Login-Logik hier
                pass
            st.markdown("[Create Account](http://localhost:5000/singin)")
        else:
            # Benutzerdaten anzeigen
            st.write(f"Name: {user.name}")
            st.write(f"Email: {user.email}")
            st.write(f"Level: {user.level}")

            if user.name == "root":
                # Root-Benutzer Optionen
                st.write("Root User")
                if st.button("Add User"):
                    # Implementiere Logik zum Hinzufügen eines Benutzers
                    pass
                if st.button("Remove User"):
                    # Implementiere Logik zum Entfernen eines Benutzers
                    pass
                if st.button("Set User Level"):
                    # Implementiere Logik zum Setzen des Benutzerlevels
                    pass

    with Mods:
        st.header("Mods-Bereich")
        # Hier könnten weitere Widgets für den Mods-Bereich hinzugefügt werden

    with System:
        st.header("System-Bereich")
        # Hier könnten weitere Widgets für den System-Bereich hinzugefügt werden


if __name__ == "__main__":
    main()

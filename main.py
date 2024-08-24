from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
import vlc
import webbrowser
from ftplib import FTP
from io import BytesIO

class AudioPlayerApp(App):
    def build(self):
        Window.clearcolor = (0.15, 0.15, 0.15, 1)  # Darker background for a modern look
        Window.size = (600, 400)
        
        self.player = vlc.MediaPlayer()
        self.url_dict = self.fetch_urls()  # Fetch URLs
        self.status = self.fetch_status()  # Fetch status

        if not self.status:
            self.stop_services()
            return self.create_unavailable_layout()
        
        return self.create_main_layout()

    def fetch_status(self):
        try:
            ftp_host = 'ftpupload.net'
            ftp_user = 'if0_37163008'
            ftp_password = 'hesmDnuLRwl'
            status_file_path = 'htdocs/status.txt'

            ftp = FTP(ftp_host)
            ftp.login(ftp_user, ftp_password)

            with BytesIO() as file:
                ftp.retrbinary(f'RETR {status_file_path}', file.write)
                file.seek(0)
                status = file.getvalue().decode('utf-8').strip().lower()

            ftp.quit()
            return status != 'off'
        except FTP.all_errors as e:
            print(f"FTP error: {e}")
        except Exception as e:
            print(f"Error fetching status: {e}")
        return False

    def fetch_urls(self):
        try:
            ftp_host = 'ftpupload.net'
            ftp_user = 'if0_37163008'
            ftp_password = 'hesmDnuLRwl'
            file_path = 'htdocs/urls.txt'

            ftp = FTP(ftp_host)
            ftp.login(ftp_user, ftp_password)

            with BytesIO() as file:
                ftp.retrbinary(f'RETR {file_path}', file.write)
                file.seek(0)
                url_lines = file.getvalue().decode('utf-8').splitlines()

            ftp.quit()

            url_dict = {}
            for line in url_lines:
                if ',' in line:
                    key, url = line.split(',', 1)
                    url_dict[key] = url
            return url_dict
        except FTP.all_errors as e:
            print(f"FTP error: {e}")
        except Exception as e:
            print(f"Error fetching URLs: {e}")
        return {}

    def create_unavailable_layout(self):
        layout = FloatLayout()
        
        status_label = Label(
            text="The service is currently unavailable.",
            size_hint=(None, None),
            size=(400, 40),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            color=(1, 0, 0, 1),  # Red color for error
            font_size='20sp'
        )
        layout.add_widget(status_label)
        
        return layout

    def create_main_layout(self):
        layout = FloatLayout()
        
        # Title bar
        title_bar = BoxLayout(size_hint=(1, None), height=40, orientation='horizontal', padding=[10, 5])
        title_bar.add_widget(Label(text="صوتيات ادهم", size_hint=(None, 1), width=200, color=(1, 1, 1, 1)))
        
        close_button = Button(text="✕", size_hint=(None, 1), width=40, background_color=(1, 0, 0, 1))
        close_button.bind(on_press=self.close_application)
        
        minimize_button = Button(text="_", size_hint=(None, 1), width=40, background_color=(0, 1, 0, 1))
        minimize_button.bind(on_press=self.minimize)
        
        title_bar.add_widget(close_button)
        title_bar.add_widget(minimize_button)
        layout.add_widget(title_bar)
        
        # Status Label
        self.status_label = Label(
            text="Status: Checking...",
            size_hint=(None, None),
            size=(400, 40),
            pos_hint={'center_x': 0.5, 'center_y': 0.75},
            color=(1, 0, 0, 1),  # Default to red until status is updated
            font_size='18sp'
        )
        layout.add_widget(self.status_label)
        
        # Entry field
        self.value_entry = TextInput(
            hint_text='ادخل الكود',
            size_hint=(None, None),
            size=(300, 40),
            pos_hint={'center_x': 0.5, 'center_y': 0.6},
            multiline=False
        )
        layout.add_widget(self.value_entry)
        
        # Buttons
        button_layout = BoxLayout(size_hint=(None, None), size=(600, 40), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        play_button = Button(text='تشغيل', background_color=(0, 1, 0, 1))
        play_button.bind(on_press=self.play_audio)
        stop_button = Button(text='إيقاف', background_color=(1, 0, 0, 1))
        stop_button.bind(on_press=self.stop_audio)
        button_layout.add_widget(play_button)
        button_layout.add_widget(stop_button)
        layout.add_widget(button_layout)
        
        # Facebook button
        facebook_button = Button(
            text='جروب كل حاجه في الدش',
            background_color=(0, 0, 1, 1),
            size_hint=(None, None),
            size=(200, 40),
            pos_hint={'center_x': 0.5, 'center_y': 0.4}
        )
        facebook_button.bind(on_press=self.open_facebook)
        layout.add_widget(facebook_button)
        
        # Developer label
        developer_label = Label(
            text='تطوير : أدهم حمدي',
            size_hint=(None, None),
            size=(200, 40),
            pos_hint={'center_x': 0.5, 'center_y': 0.3},
            color=(1, 1, 1, 1),
            font_size='16sp'
        )
        layout.add_widget(developer_label)
        
        # Update status label
        self.update_status_label()
        
        return layout

    def update_status_label(self):
        if self.status:
            self.status_label.text = "Status: Available"
            self.status_label.color = (0, 1, 0, 1)  # Green color for available
        else:
            self.status_label.text = "Status: Unavailable"
            self.status_label.color = (1, 0, 0, 1)  # Red color for unavailable

    def stop_services(self):
        if self.player:
            self.player.stop()
        print("All services stopped.")

    def play_audio(self, instance):
        value = self.value_entry.text
        url = self.url_dict.get(value)
        if url:
            media = vlc.Media(url)
            self.player.set_media(media)
            self.player.play()
        else:
            print("Invalid value")

    def stop_audio(self, instance):
        if self.player:
            self.player.stop()

    def open_facebook(self, instance):
        webbrowser.open("https://www.facebook.com/groups/adhamsat/")

    def close_application(self, instance):
        self.stop_audio()
        self.stop()

    def minimize(self, instance):
        Window.minimize()

if __name__ == '__main__':
    AudioPlayerApp().run()

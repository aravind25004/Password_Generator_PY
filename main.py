import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.togglebutton import ToggleButton

import random
import string

kivy.require('1.11.1')


class PasswordGeneratorApp(App):
    def build(self):
        # Create a root layout
        self.root_layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Create the first page
        self.create_instructions_page()

        return self.root_layout

    def create_instructions_page(self):
        # Instructions Layout
        instructions_layout = BoxLayout(orientation='vertical', spacing=10)

        instructions_label = Label(text="Welcome to the Password Generator App!\n\n"
                                        "Instructions:\n"
                                        "1. Enter your username.\n"
                                        "2. Specify the desired password length.\n"
                                        "3. Choose password strength (Strong/Weak).\n"
                                        "4. Click 'Generate Password'.\n"
                                        "5. Optionally, click 'Display Password' to see the details.\n\n"
                                        "Click 'Next' to proceed to the Password Generator.")
        instructions_layout.add_widget(instructions_label)

        next_button = Button(
            text='Next',
            on_press=self.switch_to_password_generator,
            size_hint=(None, None),
            size=(100, 50),
            pos_hint={'center_x': 0.5}
        )
        instructions_layout.add_widget(next_button)

        # Add the instructions layout to the root layout
        self.root_layout.add_widget(instructions_layout)

    def switch_to_password_generator(self, instance):
        # Remove the instructions layout
        self.root_layout.clear_widgets()

        # Create the password generator page
        self.create_password_generator_page()

    def create_password_generator_page(self):
        # Password Generator Layout
        generator_layout = BoxLayout(orientation='vertical', spacing=10)

        # Form Layout (Similar to your existing code)
        form_layout = BoxLayout(orientation='vertical', spacing=5)

        # Username Section
        username_layout = BoxLayout(orientation='horizontal', spacing=5)
        username_layout.add_widget(Label(text="Username:"))
        self.username_input = TextInput(multiline=False, input_type='text')
        username_layout.add_widget(self.username_input)
        form_layout.add_widget(username_layout)

        # Password Length Section
        password_length_layout = BoxLayout(orientation='horizontal', spacing=5)
        password_length_layout.add_widget(Label(text="Password Length:"))
        self.password_length_input = TextInput(multiline=False, input_type='number', input_filter='int')
        password_length_layout.add_widget(self.password_length_input)
        form_layout.add_widget(password_length_layout)

        # Password Strength Section
        password_strength_layout = BoxLayout(orientation='horizontal', spacing=5)
        password_strength_layout.add_widget(Label(text="Password Strength:"))
        strength_layout = BoxLayout(orientation='horizontal', spacing=5)
        self.strong_button = ToggleButton(text='Strong', group='strength', state='down')
        self.weak_button = ToggleButton(text='Weak', group='strength')
        strength_layout.add_widget(self.strong_button)
        strength_layout.add_widget(self.weak_button)
        password_strength_layout.add_widget(strength_layout)
        form_layout.add_widget(password_strength_layout)

        generator_layout.add_widget(form_layout)

        # Add the details_label
        self.details_label = TextInput(multiline=True, readonly=True, hint_text="Details will appear here")
        generator_layout.add_widget(self.details_label)

        # Buttons Layout (Similar to your existing code)
        buttons_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=50)

        generate_button = Button(text='Generate Password', on_press=self.generate_password)
        reset_button = Button(text='Reset', on_press=self.reset_form)
        display_button = Button(text='Display Password', on_press=self.display_password)

        buttons_layout.add_widget(generate_button)
        buttons_layout.add_widget(reset_button)
        buttons_layout.add_widget(display_button)

        generator_layout.add_widget(buttons_layout)

        # Add the generator layout to the root layout
        self.root_layout.add_widget(generator_layout)

    def generate_password(self, instance):
        try:
            password_length = int(self.password_length_input.text)
        except ValueError:
            self.details_label.text = "Invalid password length"
            return

        if self.strong_button.state == 'down':
            password = self.generate_strong_password(password_length)
        else:
            password = self.generate_weak_password(password_length)

        # Display generated password in the details
        self.generated_password = password
        self.details_label.text = f"The Password has been Successfully Generated"

    def generate_strong_password(self, length):
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(characters) for _ in range(length))

    def generate_weak_password(self, length):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(length))

    def reset_form(self, instance):
        self.username_input.text = ""
        self.password_length_input.text = ""
        self.strong_button.state = 'down'
        self.weak_button.state = 'normal'
        self.details_label.text = ""

    def display_password(self, instance):
        # Display details including generated password
        details = f"Details:\nUsername: {self.username_input.text}\nRequested Password Length: {self.password_length_input.text}\nPassword Type: {'Strong' if self.strong_button.state == 'down' else 'Weak'}\nGenerated Password: {self.generated_password}"
        self.details_label.text = details


if __name__ == '__main__':
    PasswordGeneratorApp().run()

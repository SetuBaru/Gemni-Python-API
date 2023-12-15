from kivymd.app import MDApp
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDIconButton
from backend import configure_genai, generate_response


class GeminiApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"  # Use dark theme

        # Root layout with scroll view
        root_layout = MDBoxLayout(orientation="vertical")
        chat_scroll_view = MDScrollView()
        chat_scroll_view.scroll_type = ["bars", "content"]
        root_layout.add_widget(chat_scroll_view)

        # Chat history layout
        self.chat_content = MDBoxLayout(orientation="vertical", size_hint_y=None, padding=(10, 10))
        chat_scroll_view.add_widget(self.chat_content)

        # Box layout for input and send button
        input_layout = MDBoxLayout(orientation="horizontal", adaptive_height=True)

        # Input box with auto-suggestions
        self.input_box = MDTextField(
            hint_text="Ask Gemini...",
            helper_text_mode="on_focus",
        )
        self.input_box.bind(on_text_validate=self.process_input)
        input_layout.add_widget(self.input_box)

        # Send button
        send_button = MDIconButton(icon="send")
        send_button.bind(on_release=self.send_message)
        input_layout.add_widget(send_button)

        root_layout.add_widget(input_layout)

        configure_genai()  # Configure GenAI backend

        return root_layout

    def process_input(self, instance):
        user_input = instance.text.strip()  # Get and trim user input
        if user_input:
            self.display_message(user_input, is_user=True)  # Display user's message
            self.generate_and_display_response(user_input)  # Generate & display Gemini's response
            instance.text = ""  # Clear input box

    def display_message(self, message, is_user=True):
        # Differentiate user and AI messages with color and style
        message_text = f"\n[{'You' if is_user else 'Gemini'}]: {message}"
        label = MDTextField(text=message_text, readonly=True, multiline=True)
        self.chat_content.add_widget(label)
        self.scroll_to_end()

    def scroll_to_end(self):
        # Scroll to the bottom of the chat content
        self.chat_content.height = sum(child.height for child in self.chat_content.children)
        self.chat_content.parent.scroll_y = 0

    def generate_and_display_response(self, prompt):
        response = generate_response(prompt)  # Generate Gemini's response
        self.display_message(response, is_user=False)
        self.scroll_to_end()

    def send_message(self, instance):
        user_input = self.input_box.text.strip()
        if user_input:
            self.display_message(user_input, is_user=True)  # Display user's message
            self.generate_and_display_response(user_input)  # Generate & display Gemini's response
            self.input_box.text = ""  # Clear input box


if __name__ == "__main__":
    GeminiApp().run()

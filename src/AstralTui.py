from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.widgets import Footer, Input
from algebra import ExpressionEvaluator

class AstralTui(App):
    BINDINGS = [
            Binding(key="q", action="quit", description="Quit the app"),
            Binding(
                key="question_mark",
                action="help",
                description="Show help screen",
                key_display="?",
            ),
            Binding(key="delete", action="delete", description="Delete the thing"),
            Binding(key="j", action="down", description="Scroll down", show=False),
        ]

    def compose(self) -> ComposeResult:
        yield Input(placeholder="Enter expression...", id="input")
        yield Footer()

    def on_input_submitted(self, message: Input.Submitted) -> None:
        expression = message.value
        try:
            result = ExpressionEvaluator(expression).evaluate()
            self.query_one("#input", Input).value = str(result)
        except Exception as e:
            self.query_one("#input", Input).value = f"Error: {str(e)}"

def __init__(self):
    AstralTui().run()

from textual.app        import App, ComposeResult
from textual.widgets    import Header, Footer
from textual.widget     import Widget



class Box(Widget):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)



class BaseApp(App):
    """A Textual app to manage stopwatches."""

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]
    CSS_PATH = ["test.tcss"]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Box(classes="one")
        yield Box(classes="two")
        yield Footer()

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark


if __name__ == "__main__":
    app = BaseApp()
    app.run()

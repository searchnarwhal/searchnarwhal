# example/example_browser.py
import tkinter as tk
from searchnarwhal.browser import Browser

class SearchNarwhalExampleApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("SearchNarwhal - Example App")
        self.geometry("1024x768")

        # URL Entry
        self.url_entry = tk.Entry(self, font=("Arial", 14))
        self.url_entry.pack(fill="x", padx=10, pady=5)
        self.url_entry.bind("<Return>", self.on_url_entered)

        # Browser from engine
        self.browser_view = Browser(self)
        self.browser_view.pack(fill="both", expand=True)

        # Load default tab
        self.browser_view.load_newtab()

    def on_url_entered(self, event=None):
        url = self.url_entry.get()
        self.browser_view.load_url(url)

if __name__ == "__main__":
    app = SearchNarwhalExampleApp()
    app.mainloop()

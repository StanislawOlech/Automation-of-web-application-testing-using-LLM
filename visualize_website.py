import tkinter as tk
from specification_generator import generate_specification
from website import Website


class WebsiteVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Website Visualizer")
        self.root.geometry("800x500")
        self.root.configure(bg="#f9f9fb")

        # Initialize state
        self.spec = generate_specification()
        self.website = Website(self.spec)
        self.entries = []      # to store input widgets
        self.indicators = []   # to store requirement status
        self.user_data = []    # [(index, value), ...]
        self.badness_value = tk.DoubleVar(value=0.0)

        self.create_ui()

    def create_ui(self):
        """Build the visual layout."""
        self.container = tk.Frame(self.root, bg="#f9f9fb")
        self.container.pack(fill="both", expand=True, padx=20, pady=10)

        # Create input elements dynamically
        for idx, (is_button, requirement) in enumerate(self.spec):
            frame = tk.Frame(self.container, bg="#ffffff", relief="ridge", bd=2)
            frame.pack(fill="x", pady=5)

            tk.Label(frame, text=f"Element {idx+1}: {requirement}",
                     font=("Arial", 10), bg="#ffffff", anchor="w").pack(side="left", padx=10, expand=True, fill="x")

            if is_button:
                btn = tk.Button(frame, text="Press", command=lambda i=idx: self.on_button_click(i))
                btn.pack(side="right", padx=10)
                self.entries.append(btn)
            else:
                entry = tk.Entry(frame)
                entry.pack(side="right", padx=10)
                entry.bind("<KeyRelease>", lambda event, i=idx: self.on_text_change(i))
                self.entries.append(entry)

            indicator = tk.Label(frame, text="❌", fg="red", bg="#ffffff", font=("Arial", 12))
            indicator.pack(side="right", padx=10)
            self.indicators.append(indicator)


        # Badness control
        slider_frame = tk.Frame(self.root, bg="#f9f9fb")
        slider_frame.pack(fill="x", pady=15)
        tk.Label(slider_frame, text="Badness:", font=("Arial", 12), bg="#f9f9fb").pack(side="left", padx=10)
        self.badness_slider = tk.Scale(
            slider_frame,
            variable=self.badness_value,
            from_=0.0, to=1.0,
            resolution=0.01,
            orient="horizontal",
            length=300,
            bg="#f9f9fb",
            highlightthickness=0,
            command=self.on_badness_change
        )
        self.badness_slider.pack(side="left", padx=10)
        tk.Label(slider_frame, textvariable=self.badness_value,
                 bg="#f9f9fb", font=("Arial", 10)).pack(side="left")


        # Control buttons
        control_frame = tk.Frame(self.root, bg="#f9f9fb")
        control_frame.pack(pady=10)

        tk.Button(control_frame, text="Generate new website", command=self.gen_new_website, bg="#ffd966").pack(side="left", padx=10)
        tk.Button(control_frame, text="Reset website", command=self.reset_state, bg="#ff9e66").pack(side="left", padx=10)
        tk.Button(control_frame, text="Exit", command=self.exit_app, bg="#ff6666").pack(side="left", padx=10)

        self.update_indicators()

    def on_text_change(self, idx):
        """Triggered when text in an entry changes."""
        self.collect_user_data()
        self.update_indicators()

    def on_badness_change(self, idx):
        """Triggered when a button is clicked."""
        self.website = Website(self.spec, self.badness_value.get())
        self.update_indicators()

    def on_button_click(self, idx):
        """Triggered when a button is clicked."""
        self.user_data.append((idx, None))
        self.update_indicators()

    def collect_user_data(self):
        """Gather data from all text boxes."""
        self.user_data = []
        for i, widget in enumerate(self.entries):
            if isinstance(widget, tk.Entry):
                self.user_data.append((i, widget.get()))
            else:
                # Button, skip unless pressed
                pass

    def update_indicators(self):
        """Ask Website() to evaluate requirements and update check marks."""
        try:
            states = self.website.use(self.user_data)
            for i, ok in enumerate(states):
                self.indicators[i].config(text="✅" if ok else "❌", fg="green" if ok else "red")
        except Exception as e:
            print("Error evaluating:", e)

    def gen_new_website(self):
        """Reset all UI and regenerate website spec."""
        for widget in self.root.winfo_children():
            widget.destroy()
        self.spec = generate_specification()
        self.website = Website(self.spec)
        self.entries.clear()
        self.indicators.clear()
        self.user_data.clear()
        self.create_ui()

    def reset_state(self):
        """Reset all UI and regenerate website spec."""
        for widget in self.root.winfo_children():
            widget.destroy()
        self.entries.clear()
        self.indicators.clear()
        self.user_data.clear()
        self.create_ui()

    def exit_app(self):
        self.root.destroy()


def visualize_website():
    root = tk.Tk()
    app = WebsiteVisualizer(root)
    root.mainloop()
    return 0


if __name__ == "__main__":
    visualize_website()

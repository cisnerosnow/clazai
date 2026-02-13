import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from pathlib import Path

class ZAIConfigApp:
    def __init__(self, root):
        self.root = root
        self.root.title("clazai")
        self.root.geometry("500x380")
        self.root.resizable(False, False)

        self.config_file = "zai_config.json"

        # Autodetect user home directory
        self.claude_settings_path = Path.home() / ".claude" / "settings.json"
        self.is_active = False

        self.setup_ui()
        self.load_config()
        self.check_activation_status()

    def setup_ui(self):
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        title_label = ttk.Label(
            main_frame,
            text="clazai",
            font=("Arial", 16, "bold")
        )
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 5))

        subtitle_label = ttk.Label(
            main_frame,
            text="claude code to z.ai toggle",
            font=("Arial", 9),
            foreground="gray"
        )
        subtitle_label.grid(row=1, column=0, columnspan=2, pady=(0, 15))

        api_label = ttk.Label(main_frame, text="API Token:")
        api_label.grid(row=2, column=0, sticky=tk.W, pady=5)

        self.api_entry = ttk.Entry(main_frame, width=40, show="*")
        self.api_entry.grid(row=2, column=1, pady=5, padx=(10, 0))

        self.show_var = tk.BooleanVar()
        show_check = ttk.Checkbutton(
            main_frame,
            text="Show token",
            variable=self.show_var,
            command=self.toggle_show_token
        )
        show_check.grid(row=3, column=1, sticky=tk.W, padx=(10, 0))

        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=4, column=0, columnspan=2, pady=20)

        save_button = ttk.Button(
            button_frame,
            text="Save",
            command=self.save_config,
            width=12
        )
        save_button.grid(row=0, column=0, padx=5)

        clear_button = ttk.Button(
            button_frame,
            text="Clear",
            command=self.clear_config,
            width=12
        )
        clear_button.grid(row=0, column=1, padx=5)

        help_button = ttk.Button(
            button_frame,
            text="Help",
            command=self.show_help,
            width=12
        )
        help_button.grid(row=0, column=2, padx=5)

        # Separator
        separator = ttk.Separator(main_frame, orient='horizontal')
        separator.grid(row=5, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=15)

        # Claude Integration Frame
        claude_frame = ttk.Frame(main_frame)
        claude_frame.grid(row=6, column=0, columnspan=2, pady=10)

        claude_label = ttk.Label(
            claude_frame,
            text="Claude Code Integration:",
            font=("Arial", 10, "bold")
        )
        claude_label.grid(row=0, column=0, pady=5)

        self.toggle_button = ttk.Button(
            claude_frame,
            text="Activar",
            command=self.toggle_activation,
            width=20
        )
        self.toggle_button.grid(row=1, column=0, pady=5)

        self.activation_status_label = ttk.Label(
            claude_frame,
            text="Estado: Desactivado",
            foreground="red",
            font=("Arial", 9)
        )
        self.activation_status_label.grid(row=2, column=0)

        status_frame = ttk.Frame(main_frame)
        status_frame.grid(row=7, column=0, columnspan=2, sticky=(tk.W, tk.E))

        self.status_label = ttk.Label(
            status_frame,
            text="",
            foreground="gray"
        )
        self.status_label.grid(row=0, column=0, sticky=tk.W)

        # Credit label
        credit_label = ttk.Label(
            status_frame,
            text="Made by @cisnerosnow",
            font=("Arial", 8),
            foreground="gray"
        )
        credit_label.grid(row=0, column=1, sticky=tk.E)

        # Configure grid weights to push credit to the right
        status_frame.columnconfigure(0, weight=1)
        status_frame.columnconfigure(1, weight=0)

    def toggle_show_token(self):
        if self.show_var.get():
            self.api_entry.config(show="")
        else:
            self.api_entry.config(show="*")

    def load_config(self):
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r') as f:
                    config = json.load(f)
                    self.api_entry.insert(0, config.get('api_token', ''))
                    self.status_label.config(
                        text="Configuration loaded",
                        foreground="green"
                    )
            except Exception as e:
                messagebox.showerror("Error", f"Error loading configuration: {str(e)}")

    def save_config(self):
        api_token = self.api_entry.get().strip()

        if not api_token:
            messagebox.showwarning("Warning", "Please enter an API token")
            return

        config = {'api_token': api_token}

        try:
            with open(self.config_file, 'w') as f:
                json.dump(config, f, indent=4)

            self.status_label.config(
                text="Configuration saved successfully!",
                foreground="green"
            )
            messagebox.showinfo("Success", "API token saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Error saving configuration: {str(e)}")

    def clear_config(self):
        self.api_entry.delete(0, tk.END)
        self.status_label.config(text="", foreground="gray")

    def show_help(self):
        help_window = tk.Toplevel(self.root)
        help_window.title("How to get Z.AI API Key")
        help_window.geometry("450x300")
        help_window.resizable(False, False)

        help_window.transient(self.root)
        help_window.grab_set()

        main_frame = ttk.Frame(help_window, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        title = ttk.Label(
            main_frame,
            text="How to get your Z.AI API Key",
            font=("Arial", 12, "bold")
        )
        title.pack(pady=(0, 15))

        instructions = """Follow these steps to obtain your API key:

1. Access Z.AI Open Platform

2. Register or Login to your account

3. Create an API Key in the API Keys
   management page

4. Copy your API Key for use

5. Paste it in the API Token field and
   click Save
"""

        instructions_label = ttk.Label(
            main_frame,
            text=instructions,
            justify=tk.LEFT,
            font=("Arial", 10)
        )
        instructions_label.pack(pady=10)

        close_button = ttk.Button(
            main_frame,
            text="Close",
            command=help_window.destroy,
            width=15
        )
        close_button.pack(pady=(10, 0))

        help_window.focus()

    def check_activation_status(self):
        """Check if Z.AI is currently activated in Claude settings"""
        try:
            if self.claude_settings_path.exists():
                with open(self.claude_settings_path, 'r', encoding='utf-8') as f:
                    settings = json.load(f)

                if 'env' in settings:
                    env = settings['env']
                    if (env.get('ANTHROPIC_BASE_URL') == 'https://api.z.ai/api/anthropic' and
                        'ANTHROPIC_AUTH_TOKEN' in env and
                        'ANTHROPIC_DEFAULT_HAIKU_MODEL' in env):
                        self.is_active = True
                        self.update_activation_ui()
                        return

            self.is_active = False
            self.update_activation_ui()
        except Exception as e:
            print(f"Error checking activation status: {e}")
            self.is_active = False
            self.update_activation_ui()

    def update_activation_ui(self):
        """Update UI based on activation status"""
        if self.is_active:
            self.toggle_button.config(text="Desactivar")
            self.activation_status_label.config(
                text="Estado: Activado",
                foreground="green"
            )
        else:
            self.toggle_button.config(text="Activar")
            self.activation_status_label.config(
                text="Estado: Desactivado",
                foreground="red"
            )

    def toggle_activation(self):
        """Toggle Z.AI activation in Claude settings"""
        api_token = self.api_entry.get().strip()

        if not self.is_active and not api_token:
            messagebox.showwarning(
                "Warning",
                "Please enter and save an API token before activating"
            )
            return

        if self.is_active:
            self.deactivate_zai()
        else:
            self.activate_zai(api_token)

    def activate_zai(self, api_token):
        """Activate Z.AI in Claude settings"""
        try:
            # Create .claude directory if it doesn't exist
            self.claude_settings_path.parent.mkdir(parents=True, exist_ok=True)

            # Load existing settings or create new
            settings = {}
            if self.claude_settings_path.exists():
                try:
                    with open(self.claude_settings_path, 'r', encoding='utf-8') as f:
                        settings = json.load(f)
                except json.JSONDecodeError:
                    settings = {}

            # Add or update env configuration
            if 'env' not in settings:
                settings['env'] = {}

            settings['env']['ANTHROPIC_AUTH_TOKEN'] = api_token
            settings['env']['ANTHROPIC_BASE_URL'] = 'https://api.z.ai/api/anthropic'
            settings['env']['API_TIMEOUT_MS'] = '3000000'
            settings['env']['ANTHROPIC_DEFAULT_HAIKU_MODEL'] = 'glm-4.5-air'
            settings['env']['ANTHROPIC_DEFAULT_SONNET_MODEL'] = 'glm-4.6'
            settings['env']['ANTHROPIC_DEFAULT_OPUS_MODEL'] = 'glm-4.6'

            # Write settings
            with open(self.claude_settings_path, 'w', encoding='utf-8') as f:
                json.dump(settings, f, indent=4)

            self.is_active = True
            self.update_activation_ui()
            messagebox.showinfo(
                "Success",
                f"Z.AI activated in Claude Code!\n\nSettings saved to:\n{self.claude_settings_path}"
            )
        except Exception as e:
            messagebox.showerror("Error", f"Error activating Z.AI: {str(e)}")

    def deactivate_zai(self):
        """Deactivate Z.AI in Claude settings"""
        try:
            if not self.claude_settings_path.exists():
                self.is_active = False
                self.update_activation_ui()
                return

            # Load existing settings
            with open(self.claude_settings_path, 'r', encoding='utf-8') as f:
                settings = json.load(f)

            # Remove Z.AI configuration
            if 'env' in settings:
                settings['env'].pop('ANTHROPIC_AUTH_TOKEN', None)
                settings['env'].pop('ANTHROPIC_BASE_URL', None)
                settings['env'].pop('API_TIMEOUT_MS', None)
                settings['env'].pop('ANTHROPIC_DEFAULT_HAIKU_MODEL', None)
                settings['env'].pop('ANTHROPIC_DEFAULT_SONNET_MODEL', None)
                settings['env'].pop('ANTHROPIC_DEFAULT_OPUS_MODEL', None)

                # Remove env key if empty
                if not settings['env']:
                    settings.pop('env')

            # Write updated settings
            with open(self.claude_settings_path, 'w', encoding='utf-8') as f:
                json.dump(settings, f, indent=4)

            self.is_active = False
            self.update_activation_ui()
            messagebox.showinfo("Success", "Z.AI deactivated from Claude Code!")
        except Exception as e:
            messagebox.showerror("Error", f"Error deactivating Z.AI: {str(e)}")

def main():
    root = tk.Tk()
    app = ZAIConfigApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

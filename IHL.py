import tkinter as tk
from tkinter import ttk
import csv
import webbrowser


class AboutWindow(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("About")
        self.geometry("300x200")

        about_text = (
            "Incident Handling Log\n"
            "Version 1.0\n"
            "Created by Memphis\n\n"
            "Released under the GNU Public License.\n"
            "For more information, visit:\n"
            "https://www.gnu.org/licenses/gpl-3.0.html"
        )

        label = tk.Label(self, text=about_text)
        label.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        button = tk.Button(self, text="Close", command=self.destroy)
        button.pack(padx=10, pady=10)


class IncidentLoggerApp:
    def __init__(self, master):
        self.master = master
        master.title("Incident Handling Log")

        self.categories = {
            "---Select Class---": [],
            "High": ["Unauthorized System Access", "Ransomware", "BEC", "Other"],
            "Medium": ["Information Gathering", "Malware", "Data Loss", "Other"],
            "Low": ["AUP Violation", "Phishing", "Service Disruption", "Other"]
        }

        self.incidents = []

        self.selected_class = tk.StringVar(master)
        self.selected_class.set("---Select Class---")
        self.selected_class.trace("w", self.populate_categories)

        self.selected_category = tk.StringVar(master)
        self.selected_category.set("---Select Category---")
        self.selected_category.trace("w", self.toggle_other_textbox)

        self.selected_soc_required = tk.StringVar(master)
        self.selected_soc_required.set("---Select---")

        self.selected_risk = tk.StringVar(master)
        self.selected_risk.set("---Select---")

        self.incident_date_entry = tk.Entry(master)

        self.name_entry = tk.Entry(master)

        self.incident_date_label = tk.Label(master, text="Incident Date:")
        self.incident_date_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.incident_date_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

        self.name_label = tk.Label(master, text="Name:")
        self.name_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.name_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        self.class_label = tk.Label(master, text="Class:")
        self.class_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.class_menu = ttk.OptionMenu(master, self.selected_class, *self.categories.keys())
        self.class_menu.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

        self.category_label = tk.Label(master, text="Category:")
        self.category_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.category_menu = ttk.OptionMenu(master, self.selected_category, "---Select Category---")
        self.category_menu.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

        self.other_label = tk.Label(master, text="Other:")
        self.other_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.other_entry = tk.Entry(master)  # Text box for "Other" category
        self.other_entry.grid(row=4, column=1, padx=10, pady=5, sticky="ew")
        self.other_entry.grid_remove()  # Hide it initially

        self.risk_label = tk.Label(master, text="Risk:")
        self.risk_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        self.risk_menu = ttk.OptionMenu(master, self.selected_risk, "---Select---", "High", "Medium", "Low")
        self.risk_menu.grid(row=5, column=1, padx=10, pady=5, sticky="ew")

        self.soc_required_label = tk.Label(master, text="SOC Required:")
        self.soc_required_label.grid(row=6, column=0, padx=10, pady=5, sticky="w")
        self.soc_required_menu = ttk.OptionMenu(master, self.selected_soc_required, "---Select---", "Yes", "No")
        self.soc_required_menu.grid(row=6, column=1, padx=10, pady=5, sticky="ew")

        self.event_description_label = tk.Label(master, text="Event Description:")
        self.event_description_label.grid(row=7, column=0, padx=10, pady=5, sticky="w")
        self.event_description_entry = tk.Entry(master)
        self.event_description_entry.grid(row=7, column=1, padx=10, pady=5, sticky="ew")

        self.systems_users_affected_label = tk.Label(master, text="System(s)/Users Affected:")
        self.systems_users_affected_label.grid(row=8, column=0, padx=10, pady=5, sticky="w")
        self.systems_users_affected_entry = tk.Entry(master)
        self.systems_users_affected_entry.grid(row=8, column=1, padx=10, pady=5, sticky="ew")

        self.resolution_label = tk.Label(master, text="Resolution:")
        self.resolution_label.grid(row=9, column=0, padx=10, pady=5, sticky="w")
        self.resolution_entry = tk.Entry(master)
        self.resolution_entry.grid(row=9, column=1, padx=10, pady=5, sticky="ew")

        self.date_completed_label = tk.Label(master, text="Date Completed:")
        self.date_completed_label.grid(row=10, column=0, padx=10, pady=5, sticky="w")
        self.date_completed_entry = tk.Entry(master)
        self.date_completed_entry.grid(row=10, column=1, padx=10, pady=5, sticky="ew")

        self.notes_label = tk.Label(master, text="Additional Notes:")
        self.notes_label.grid(row=11, column=0, padx=10, pady=5, sticky="w")
        self.notes_entry = tk.Entry(master)
        self.notes_entry.grid(row=11, column=1, padx=10, pady=5, sticky="ew")

        self.log_button = tk.Button(master, text="Log Incident", command=self.log_incident)
        self.log_button.grid(row=12, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

        self.search_label = tk.Label(master, text="Search:")
        self.search_label.grid(row=13, column=0, padx=10, pady=5, sticky="w")
        self.search_entry = tk.Entry(master)
        self.search_entry.grid(row=13, column=1, padx=10, pady=5, sticky="ew")
        self.search_button = tk.Button(master, text="Search", command=self.search_incidents)
        self.search_button.grid(row=13, column=2, padx=10, pady=5, sticky="ew")

        self.about_button = tk.Button(master, text="About", command=self.open_about_window)
        self.about_button.grid(row=0, column=2, padx=10, pady=5, sticky="ne")

        self.log_text = tk.Text(master, height=10, width=50)
        self.log_text.grid(row=14, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

        # Configure row and column weights to allow resizing
        master.grid_rowconfigure(14, weight=1)
        master.grid_columnconfigure((0, 1), weight=1)

        # Hide the "Other" label and entry initially
        self.other_label.grid_remove()
        self.other_entry.grid_remove()

        # Load existing incidents from CSV file
        self.load_incidents()

    def populate_categories(self, *args):
        selected_class = self.selected_class.get()
        categories = self.categories.get(selected_class, [])
        self.selected_category.set("---Select Category---")
        menu = self.category_menu["menu"]
        menu.delete(0, "end")
        for category in categories:
            menu.add_command(label=category, command=lambda sub=category: self.selected_category.set(sub))

    def toggle_other_textbox(self, *args):
        selected_category = self.selected_category.get()
        if selected_category == "Other":
            self.other_label.grid()  # Show the label for "Other" category
            self.other_entry.grid()  # Show the text box for "Other" category
        else:
            self.other_label.grid_remove()  # Hide the label for "Other" category
            self.other_entry.grid_remove()  # Hide the text box for "Other" category

    def log_incident(self):
        category = self.selected_category.get()
        if category == "Other":
            incident_category = self.other_entry.get()  # Use the content of the "Other" text box
        else:
            incident_category = category

        incident = {
            "Class": self.selected_class.get(),
            "Category": incident_category,  # Use the content of the "Other" text box if "Other" is selected
            "Date": self.date_completed_entry.get(),
            "Name": self.name_entry.get(),
            "Event Description": self.event_description_entry.get(),
            "System(s)/Users Affected": self.systems_users_affected_entry.get(),
            "Resolution": self.resolution_entry.get(),
            "Date Completed": self.date_completed_entry.get(),
            "Risk": self.selected_risk.get(),
            "SOC Required": self.selected_soc_required.get(),
            "Additional Notes": self.notes_entry.get()  # Adding additional notes to the incident
        }
        self.incidents.append(incident)
        self.save_incidents()
        self.update_log_text()

    def save_incidents(self):
        with open("incidents.csv", mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.incidents[0].keys())
            writer.writeheader()
            writer.writerows(self.incidents)

    def load_incidents(self):
        try:
            with open("incidents.csv", mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.incidents.append(row)
        except FileNotFoundError:
            pass

    def update_log_text(self, incidents=None):
        self.log_text.delete("1.0", tk.END)
        incidents = incidents or self.incidents
        for incident in incidents:
            self.log_text.insert(tk.END, f"Incident logged:\n{incident}\n\n")

    def search_incidents(self):
        query = self.search_entry.get().lower()
        search_results = [incident for incident in self.incidents if query in str(incident).lower()]
        self.update_log_text(search_results)

    def open_about_window(self):
        about_window = AboutWindow(self.master)


def main():
    root = tk.Tk()
    app = IncidentLoggerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
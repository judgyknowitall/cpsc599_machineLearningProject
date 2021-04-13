'''
CPSC 599 - Machine Learning Project
Team 7

@author: Abdullah

Graphical User Interface

References:
        https://tkdocs.com/tutorial/index.html
'''

from tkinter import *
import tkinter as tk
from tkinter import ttk
import traceback

class App:
    
    def __init__(self, root, model):
        
        root.title("COVID-19 Severity Predictor")
        self.loaded_model = model
        self.bg_colour = "#CCCCCC"
        self.default_blue = "#007FFF"
        
        # Creating content frame
        mainframe = tk.Frame(root, padx='12', pady='12', bg=self.bg_colour)
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.option_add("*Font", "Consolas")
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        
        tk.Label(mainframe, text="COVID-19 Severity Predictor", 
                fg=self.default_blue, bg=self.bg_colour, font=("Consolas", 24)).grid(column=1, row=1, sticky=(N), columnspan=3)

        tk.Label(mainframe, text="WARNING: Any predicitions made by this application are not medical advice. By using this application, you release the authors of any liabilities that occur from its use.", 
                fg="red", bg=self.bg_colour, font=("Consolas", 13), wraplength=250, justify="left").grid(column=3, row=7, sticky=(W), rowspan=7)

        # Widgets for user entry
        self.fever = StringVar()
        tk.Label(mainframe, text="Fever:", bg=self.bg_colour).grid(column=1, row=2, sticky=(W))
        fever_combo = ttk.Combobox(mainframe, width=10, textvariable=self.fever,
                values=('Yes', 'No'))
        fever_combo.grid(column=1, row=3, sticky=(W))
        fever_combo.state(["readonly"])

        self.tiredness = StringVar()
        tk.Label(mainframe, text="Tiredness:", bg=self.bg_colour).grid(column=1, row=4, sticky=(W))
        tiredness_combo = ttk.Combobox(mainframe, width=10, textvariable=self.tiredness,
                values=('Yes', 'No'))
        tiredness_combo.grid(column=1, row=5, sticky=(W))
        tiredness_combo.state(["readonly"])

        self.dry_cough = StringVar()
        tk.Label(mainframe, text="Dry Cough:", bg=self.bg_colour).grid(column=1, row=6, sticky=(W))
        drycough_combo = ttk.Combobox(mainframe, width=10, textvariable=self.dry_cough,
                values=('Yes', 'No'))
        drycough_combo.grid(column=1, row=7, sticky=(W))
        drycough_combo.state(["readonly"])

        self.dif_breath = StringVar()
        tk.Label(mainframe, text="Difficulty Breathing:", bg=self.bg_colour).grid(column=1, row=8, sticky=(W))
        difbreath_combo = ttk.Combobox(mainframe, width=10, textvariable=self.dif_breath,
                values=('Yes', 'No'))
        difbreath_combo.grid(column=1, row=9, sticky=(W))
        difbreath_combo.state(["readonly"])

        self.sore_throat = StringVar()
        tk.Label(mainframe, text="Sore Throat:", bg=self.bg_colour).grid(column=1, row=10, sticky=(W))
        sorethroat_combo = ttk.Combobox(mainframe, width=10, textvariable=self.sore_throat,
                values=('Yes', 'No'))
        sorethroat_combo.grid(column=1, row=11, sticky=(W))
        sorethroat_combo.state(["readonly"])

        self.pains = StringVar()
        tk.Label(mainframe, text="Pains:", bg=self.bg_colour).grid(column=1, row=12, sticky=(W))
        pains_combo = ttk.Combobox(mainframe, width=10, textvariable=self.pains,
                values=('Yes', 'No'))
        pains_combo.grid(column=1, row=13, sticky=(W))
        pains_combo.state(["readonly"])

        self.nasal_cong = StringVar()
        tk.Label(mainframe, text="Nasal Congestion:", bg=self.bg_colour).grid(column=2, row=2, sticky=(W))
        nasalcong_combo = ttk.Combobox(mainframe, width=10, textvariable=self.nasal_cong,
                values=('Yes', 'No'))
        nasalcong_combo.grid(column=2, row=3, sticky=(W))
        nasalcong_combo.state(["readonly"])

        self.runny_nose = StringVar()
        tk.Label(mainframe, text="Runny Nose:", bg=self.bg_colour).grid(column=2, row=4, sticky=(W))
        runnynose_combo = ttk.Combobox(mainframe, width=10, textvariable=self.runny_nose,
                values=('Yes', 'No'))
        runnynose_combo.grid(column=2, row=5, sticky=(W))
        runnynose_combo.state(["readonly"])

        self.diarrhea = StringVar()
        tk.Label(mainframe, text="Diarrhea:", bg=self.bg_colour).grid(column=2, row=6, sticky=(W))
        diarrhea_combo = ttk.Combobox(mainframe, width=10, textvariable=self.diarrhea,
                values=('Yes', 'No'))
        diarrhea_combo.grid(column=2, row=7, sticky=(W))
        diarrhea_combo.state(["readonly"])

        self.contact = StringVar()
        tk.Label(mainframe, text="Contact:", bg=self.bg_colour).grid(column=2, row=8, sticky=(W))
        contact_combo = ttk.Combobox(mainframe, width=10, textvariable=self.contact,
                values=('Yes', 'No', 'Unsure'))
        contact_combo.grid(column=2, row=9, sticky=(W))
        contact_combo.state(["readonly"])

        self.gender = StringVar()
        tk.Label(mainframe, text="Gender:", bg=self.bg_colour).grid(column=2, row=10, sticky=(W))
        contact_combo = ttk.Combobox(mainframe, width=10, textvariable=self.gender,
                values=('Male', 'Female', 'Transgender'))
        contact_combo.grid(column=2, row=11, sticky=(W))
        contact_combo.state(["readonly"])

        self.age = StringVar()
        tk.Label(mainframe, text="Age:", bg=self.bg_colour).grid(column=2, row=12, sticky=(W))
        age_entry = ttk.Entry(mainframe, width=11, textvariable=self.age)
        age_entry.grid(column=2, row=13, sticky=(W))

        tk.Button(mainframe, text="Submit", bg=self.default_blue, fg="white", activeforeground=self.default_blue, activebackground="white",
                 command=self.get_values_predict, width=33).grid(column=1, row=14, sticky=(N,W), columnspan=2)

        # Widgets for output
        tk.Label(mainframe, text="Prediction", 
                fg=self.default_blue, bg=self.bg_colour).grid(column=3, row=2, sticky=(W), ipadx=20)

        self.severity = StringVar()
        tk.Label(mainframe, text="Severity", 
                fg="black", bg=self.bg_colour).grid(column=3, row=3, sticky=(W), ipadx=20)
        tk.Label(mainframe, textvariable=self.severity, 
                fg="black", bg=self.bg_colour).grid(column=3, row=4, sticky=(W), ipadx=20)

        self.confidence = StringVar()
        tk.Label(mainframe, text="Confidence", 
                fg="black", bg=self.bg_colour).grid(column=3, row=5, sticky=(W), ipadx=20)
        tk.Label(mainframe, textvariable=self.confidence, 
                fg="black", bg=self.bg_colour).grid(column=3, row=6, sticky=(W), ipadx=20)

        root.bind("<Return>", self.get_values_predict)

        # Adding padding and focus
        for child in mainframe.winfo_children(): 
            child.grid_configure(padx=5, pady=3)
        fever_combo.focus()
        
    # Process User Input Values and Predict
    def get_values_predict(self, *args):
        user_data = []
        
        try:
            # Fever 
            fever_val = 1 if self.fever.get() == "Yes" else 0
            user_data.append(fever_val)
            
            # Tiredness
            tired_val = 1 if self.tiredness.get() == "Yes" else 0
            user_data.append(tired_val)
            
            # Dry-Cough
            drycough_val = 1 if self.dry_cough.get() == "Yes" else 0
            user_data.append(drycough_val)
            
            # Difficulty-in-Breathing
            difbreath_val = 1 if self.dif_breath.get() == "Yes" else 0
            user_data.append(difbreath_val)
            
            # Sore-throat
            sorethroat_val = 1 if self.sore_throat.get() == "Yes" else 0
            user_data.append(sorethroat_val)
            
            # Pains
            pains_val = 1 if self.pains.get() == "Yes" else 0
            user_data.append(pains_val)
            
            # Nasal-Congestion
            nasalcong_val = 1 if self.nasal_cong.get() == "Yes" else 0
            user_data.append(nasalcong_val)
            
            # Runny-Nose
            runnynose_val = 1 if self.runny_nose.get() == "Yes" else 0
            user_data.append(runnynose_val)
            
            # Diarrhea
            diarrhea_val = 1 if self.diarrhea.get() == "Yes" else 0
            user_data.append(diarrhea_val)

            # Age
            age_num = int(self.age.get())
            if age_num >= 0 and age_num < 10:
                age_val = 0
            elif age_num >= 10 and age_num < 20:
                age_val = 1
            elif age_num >= 20 and age_num < 25:
                age_val = 2
            elif age_num >= 25 and age_num < 60:
                age_val = 3
            else:
                age_val = 4
            user_data.append(age_val)

            # Gender
            if self.gender.get() == "Transgender":
                gender_val = 0
            elif self.gender.get() == "Male":
                gender_val = 1
            else:
                gender_val = 2
            user_data.append(gender_val)
            
            # Contact
            if self.contact.get() == "No":
                contact_val = 0
            elif self.contact.get() == "Yes":
                contact_val = 1
            else:
                contact_val = 2
            user_data.append(contact_val)
            
            # Make prediction on user input
            user_in = [user_data]
            prediction = self.loaded_model.predict(user_in)
            
            # Process output
            pred_list = prediction.tolist()
            model_confidence = max(pred_list[0])
            severity_level = pred_list[0].index(model_confidence)
            model_confidence *= 100
            
            # Display output to main window
            self.severity.set(severity_level)
            self.confidence.set("{:.2f}%".format(model_confidence))
        except ValueError:
            pass
        except Exception:
            traceback.print_exc()

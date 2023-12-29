import tkinter as tk
from tkinter import ttk
from collections import OrderedDict

class PokemonCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pokemon Type Calculator")

        self.types = ('Normal', 'Fire', 'Water', 'Electric', 'Grass', 'Ice', 'Fighting', 'Poison', 'Ground',
                      'Flying', 'Psychic', 'Bug', 'Rock', 'Ghost', 'Dragon', 'Dark', 'Steel', 'Fairy')

        self.T1_var = tk.StringVar()
        self.T2_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Label
        ttk.Label(self.root, text="Type 1:").grid(row=0, column=0, padx=10, pady=5, sticky="w")

        # Type 1 Combobox
        type1_combobox = ttk.Combobox(self.root, textvariable=self.T1_var, values=self.types, state="readonly")
        type1_combobox.grid(row=0, column=1, padx=10, pady=5)

        # Label
        ttk.Label(self.root, text="Type 2:").grid(row=1, column=0, padx=10, pady=5, sticky="w")

        # Type 2 Combobox
        type2_combobox = ttk.Combobox(self.root, textvariable=self.T2_var, values=self.types + ("",), state="readonly")
        type2_combobox.grid(row=1, column=1, padx=10, pady=5)

        # Calculate Button
        ttk.Button(self.root, text="Calculate", command=self.calculate).grid(row=2, column=0, columnspan=2, pady=10)

        # Results Text
        self.results_text = tk.Text(self.root, height=10, width=40)
        self.results_text.grid(row=3, column=0, columnspan=2, padx=10)

    def calculate(self):
        T1 = self.T1_var.get()
        T2 = self.T2_var.get() if self.T2_var.get() else None

        # Perform type calculation (you can reuse your existing classify_types function here)
        weak, strong, immune, neutral = self.classify_types(T1, T2)

        # Display results in the text widget
        results_text = f"Weaknesses:\n{self.format_results(weak)}\n\n" \
                       f"Neutral:\n{self.format_results(neutral)}\n\n" \
                       f"Strong:\n{self.format_results(strong)}\n\n" \
                       f"Immune:\n{self.format_results(immune)}"

        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(tk.END, results_text)

    def classify_types(self, type1, type2=None):
        # Import the type dictionaries from valores.py
        from valores import Normal, Fire, Water, Electric, Grass, Ice, Fighting, \
            Poison, Ground, Flying, Psychic, Bug, Rock, Ghost, Dragon, Dark, Steel, Fairy

        # Create a dictionary to store the type dictionaries
        type_dict = {
            'normal': Normal, 'fire': Fire, 'water': Water, 'electric': Electric,
            'grass': Grass, 'ice': Ice, 'fighting': Fighting, 'poison': Poison,
            'ground': Ground, 'flying': Flying, 'psychic': Psychic, 'bug': Bug,
            'rock': Rock, 'ghost': Ghost, 'dragon': Dragon, 'dark': Dark,
            'steel': Steel, 'fairy': Fairy
        }

        # Get weaknesses for type1
        weaknesses_T1 = type_dict.get(type1, {})

        # If type2 is specified, combine the weaknesses with type2
        if type2:
            weaknesses_T2 = type_dict.get(type2, {})
            combined_weaknesses = {k.lower(): v * weaknesses_T2.get(k, 1) for k, v in weaknesses_T1.items()}
        else:
            combined_weaknesses = {k.lower(): v for k, v in weaknesses_T1.items()}

        # Initialize dictionaries within the method
        weak = {}
        strong = {}
        immune = {}
        neutral = {}

        # Classify based on effectiveness
        for t in self.types:
            k = t.lower()
            v = combined_weaknesses.get(k, 1.0)

            if v < 1 and v > 0:
                weak[k] = v
            elif v == 1:
                neutral[k] = v
            elif v > 1:
                strong[k] = v
            elif v == 0:
                immune[k] = v

        # Return the results
        return weak, strong, immune, neutral

    def format_results(self, result_dict):
        return "\n".join([f"{k.capitalize()}: {v}x" for k, v in result_dict.items()])


if __name__ == "__main__":
    root = tk.Tk()
    app = PokemonCalculatorApp(root)
    root.mainloop()

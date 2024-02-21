import requests
import tkinter as tk

class Quote_Generator():
    def __init__(self, root):
        self.root = root
        self.root.title("Random Quote Generator")
        self.root.configure(bg='#4b5152')

        self.label = tk.Label(root, text='Quote:', font=('Arial', 14), bg='#4b5152', fg='#09caeb')
        self.label.pack(pady=10)

        self.text_area = tk.Text(root, height=10, width=60, font=('Arial', 12), bg='#4b5152', fg='#09caeb', wrap=tk.WORD)
        self.text_area.pack(padx=5)
    
        self.fetch_button = tk.Button(root, text="Generate Quote", command= self.fetch_data, font=('Arial', 12), bg='#008CBA')
        self.fetch_button.pack(pady=10)

    def fetch_data(self):
        url = 'https://api.quotable.io/random'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            content = data.get('content', 'content not found')
            author = data.get('author')
            self.text_area.delete('1.0', tk.END)
            self.insert_centered_text(content)
            self.insert_centered_text(author)
        else:
            self.text_area.delete('1.0', tk.END)
            self.text_area.insert(tk.END, "Error: Failed to fetch data")
    
    def insert_centered_text(self, text):
        self.text_area.insert(tk.END, '\n\n' + text)
        self.text_area.tag_configure("center", justify="center")
        self.text_area.tag_add("center", "1.0", "end")


root = tk.Tk()
app = Quote_Generator(root)
root.mainloop()

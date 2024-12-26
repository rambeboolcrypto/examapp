#импортируем библи
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog, ttk
import random
class QuestionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Question Shuffler")

        self.load_button = ttk.Button(root, text="Загрузить массив вопросов и ответов", command=self.load_questions)
        self.load_button.pack(pady=10)

        self.shuffle_button = ttk.Button(root, text="Перемешать вопросы", command=self.shuffle_questions)
        self.shuffle_button.pack(pady=10)

        self.export_button = ttk.Button(root, text="Выгрузить вопросы", command=self.export_options)
        self.export_button.pack(pady=10)

        self.questions = []
        self.question_listbox = tk.Listbox(root, width=80, height=20)
        self.question_listbox.pack(pady=10)

    def load_questions(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                self.questions = [q.strip() for q in content.split("\n\n") if q.strip()]
            self.update_question_listbox()
        else:
            messagebox.showwarning("Ошибка", "Не удалось загрузить файл")

    def shuffle_questions(self):
        if self.questions:
            random.shuffle(self.questions)
            self.update_question_listbox()
        else:
            messagebox.showwarning("Ошибка", "Сначала загрузите вопросы")

    def export_options(self):
        if self.questions:
            option = messagebox.askquestion("Выгрузить вопросы", "Выгрузить всё в один файл?", icon='question')
            if option == 'yes':
                self.export_questions(single_file=True)
            else:
                self.export_questions(single_file=False)
        else:
            messagebox.showwarning("Ошибка", "Сначала загрузите и перемешайте вопросы")

    def export_questions(self, single_file):
        if single_file:
            file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
            if file_path:
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write("\n\n".join(self.questions))
                messagebox.showinfo("Успех", "Вопросы успешно выгружены")
            else:
                messagebox.showwarning("Ошибка", "Не удалось выгрузить файл")
        else:
            num_tickets = simpledialog.askinteger("Количество билетов", "Введите количество билетов")
            questions_per_ticket = simpledialog.askinteger("Вопросы в одном билете", "Введите количество вопросов в одном билете")
            if num_tickets and questions_per_ticket:
                for i in range(num_tickets):
                    file_path = filedialog.asksaveasfilename(defaultextension=f"_{i+1}.txt", filetypes=[("Text files", "*.txt")])
                    if file_path:
                        with open(file_path, 'w', encoding='utf-8') as file:
                            start = i * questions_per_ticket
                            end = start + questions_per_ticket
                            file.write("\n\n".join(self.questions[start:end]))
                messagebox.showinfo("Успех", "Вопросы успешно выгружены")
            else:
                messagebox.showwarning("Ошибка", "Неверные параметры")

    def update_question_listbox(self):
        self.question_listbox.delete(0, tk.END)
        for question in self.questions:
            self.question_listbox.insert(tk.END, question)

if __name__ == "__main__":
    root = tk.Tk()
    app = QuestionApp(root)
    root.mainloop()
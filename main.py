import tkinter as tk
from blockchain import Blockchain

BLOCK_WIDTH = 70
BLOCK_HEIGHT = 70
BLOCK_SPACING = 50
CANVAS_HEIGHT = 400
BLOCK_COLOR = "#1e2a38"
TEXT_COLOR = "#00e0ff"
ARROW_COLOR = "#00ffc3"
BG_COLOR = "#0d1b2a"
FONT = ("Consolas", 10)

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini Blockchain Futuriste")
        self.root.configure(bg=BG_COLOR)
        self.root.geometry("900x500")

        self.blockchain = Blockchain()

        # Scrollable canvas
        self.canvas_frame = tk.Frame(root, bg=BG_COLOR)
        self.canvas_frame.pack(fill="both", expand=True)

        self.canvas = tk.Canvas(self.canvas_frame, bg=BG_COLOR, height=CANVAS_HEIGHT, highlightthickness=0)
        self.canvas.pack(side="left", fill="both", expand=True)

        self.scrollbar = tk.Scrollbar(self.canvas_frame, orient="horizontal", command=self.canvas.xview)
        self.scrollbar.pack(side="bottom", fill="x")
        self.canvas.configure(xscrollcommand=self.scrollbar.set)

        self.button = tk.Button(root, text="Add a new block", command=self.add_block, bg="#1effbd", fg="black")
        self.button.pack(pady=10)

        self.display_chain()

    def add_block(self):
        self.blockchain.add_block()
        self.display_chain()

    def display_chain(self):
        self.canvas.delete("all")

        x = 50
        y = CANVAS_HEIGHT // 2 - BLOCK_HEIGHT // 2

        for i, block in enumerate(self.blockchain.chain):
            # Draw the block
            self.canvas.create_rectangle(x, y, x + BLOCK_WIDTH, y + BLOCK_HEIGHT, fill=BLOCK_COLOR, outline=ARROW_COLOR, width=2, tags=f"block_{i}")
            self.canvas.create_text(x + BLOCK_WIDTH // 2, y + 20, text=f"#{block.index}", fill=TEXT_COLOR, font=FONT, tags=f"block_{i}")
            self.canvas.create_text(x + BLOCK_WIDTH // 2, y + 40, text=block.hash[:6], fill=TEXT_COLOR, font=("Consolas", 8), tags=f"block_{i}")

            # Draw the arrow between blocks
            if i < len(self.blockchain.chain) - 1:
                self.canvas.create_line(
                    x + BLOCK_WIDTH, y + BLOCK_HEIGHT // 2,
                    x + BLOCK_WIDTH + BLOCK_SPACING - 10, y + BLOCK_HEIGHT // 2,
                    arrow="last", fill=ARROW_COLOR, width=2
                )

            # To view block's informations
            self.canvas.tag_bind(f"block_{i}", "<Button-1>", lambda event, b=block: self.show_block_info(b))

            x += BLOCK_WIDTH + BLOCK_SPACING

        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def show_block_info(self, block):
        info = tk.Toplevel(self.root)
        info.title(f"Bloc #{block.index}")
        info.configure(bg="white")
        info.geometry("400x300")

        text = tk.Text(info, wrap="word", bg="white", fg="black", font=("Consolas", 10))
        text.pack(expand=True, fill="both", padx=10, pady=10)

        text.insert(tk.END, f"Bloc #{block.index}\n")
        text.insert(tk.END, f"{'-'*30}\n")
        text.insert(tk.END, f"Timestamp : {block.timestamp}\n")
        text.insert(tk.END, f"Data      : {block.data}\n")
        text.insert(tk.END, f"Hash      : {block.hash}\n")
        text.insert(tk.END, f"Previous  : {block.previous_hash}\n")

        text.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
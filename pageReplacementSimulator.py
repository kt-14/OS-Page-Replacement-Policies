import tkinter as tk

root = tk.Tk()
root.geometry("500x400")
root.title("Page Replacement Policies")

def create_labels(window, num_pages, page_faults, hits):
    hit_ratio = hits / num_pages
    miss_ratio = 1 - hit_ratio
    page_fault_label = tk.Label(window, text=f"Page Faults: {page_faults}", font="bold", fg="white", bg="black")
    hit_label = tk.Label(window, text=f"Total Hits: {hits}", font="bold", fg="white", bg="black")
    hit_ratio_label = tk.Label(window, text=f"Hit Ratio: {hit_ratio:.2f}", font="bold", fg="white", bg="black")
    miss_ratio_label = tk.Label(window, text=f"Miss Ratio: {miss_ratio:.2f}", font="bold", fg="white", bg="black")
    page_fault_label.grid(row=1, column=1, columnspan=num_pages, padx=5, pady=5, sticky=tk.W)
    hit_label.grid(row=2, column=1, columnspan=num_pages, padx=5, pady=5, sticky=tk.W)
    hit_ratio_label.grid(row=3, column=1, columnspan=num_pages, padx=5, pady=5, sticky=tk.W)
    miss_ratio_label.grid(row=4, column=1, columnspan=num_pages, padx=5, pady=5, sticky=tk.W)

def fifo_algorithm(num_pages, reference_string, num_frames, window):
    frames = [-1] * num_frames
    page_faults = 0
    hits = 0
    frame_pointer = 0
    window.title("FIFO Algorithm")
    window.configure(background="black")

    for i in range(num_pages):
        current_page = reference_string[i]
        page_label = tk.Label(window, text=f"{current_page}", font="bold", bd=2, fg="white", bg="black", relief=tk.SOLID)
        page_label.grid(row=6, column=1+i, ipadx=20, ipady=10, sticky=tk.W)
        page_found = False

        for j in range(num_frames):
            if frames[j] == current_page:
                page_found = True
                hits += 1
                break

        if not page_found:
            frames[frame_pointer] = current_page
            frame_pointer = (frame_pointer + 1) % num_frames
            page_faults += 1

        for j in range(num_frames):
            if frames[j] == -1:
                color = "#ff0000" if not page_found else "#00cc00"
                label = tk.Label(window, text="  ", font="bold", bd=2, bg=color, relief=tk.SOLID)
                label.grid(row=7+j, column=1+i, ipadx=20, ipady=10, sticky=tk.W)
            else:
                color = "#ff0000" if not page_found else "#00cc00"
                label = tk.Label(window, text="%d" % frames[j], font="bold", bd=2, bg=color, relief=tk.SOLID)
                label.grid(row=7+j, column=1+i, ipadx=20, ipady=10, sticky=tk.W)
    
    print("FIFO Algorithm:")
    print("\nPage Faults: ", page_faults)
    print("\nTotal Hits: ", hits)
    create_labels(window, num_pages, page_faults, hits)

def lru_algorithm(num_pages, reference_string, num_frames, window):
    frames = [-1] * num_frames
    page_faults = 0
    hits = 0
    usage_order = [0] * num_frames
    window.title("LRU Algorithm")
    window.configure(background="black")

    for i in range(num_pages):
        current_page = reference_string[i]
        page_label = tk.Label(window, text=f"{current_page}", font="bold", bd=2, fg="white", bg="black", relief=tk.SOLID)
        page_label.grid(row=6, column=1+i, ipadx=20, ipady=10, sticky=tk.W)
        page_found = False

        for j in range(num_frames):
            if frames[j] == current_page:
                page_found = True
                hits += 1
                usage_order[j] = i
                break

        if not page_found:
            if -1 in frames:
                frame_to_replace = frames.index(-1)
            else:
                frame_to_replace = usage_order.index(min(usage_order))
            frames[frame_to_replace] = current_page
            usage_order[frame_to_replace] = i
            page_faults += 1

        for j in range(num_frames):
            if frames[j] == -1:
                color = "#ff0000" if not page_found else "#00cc00"
                label = tk.Label(window, text="  ", font="bold", bd=2, bg=color, relief=tk.SOLID)
                label.grid(row=7+j, column=1+i, ipadx=20, ipady=10, sticky=tk.W)
            else:
                color = "#ff0000" if not page_found else "#00cc00"
                label = tk.Label(window, text="%d" % frames[j], font="bold", bd=2, bg=color, relief=tk.SOLID)
                label.grid(row=7+j, column=1+i, ipadx=20, ipady=10, sticky=tk.W)
    
    print("LRU Algorithm:")
    print("\nPage Faults: ", page_faults)
    print("\nTotal Hits: ", hits)
    create_labels(window, num_pages, page_faults, hits)

def optimal_algorithm(num_pages, reference_string, num_frames, window):
    frames = [-1] * num_frames
    page_faults = 0
    hits = 0
    window.title("Optimal Algorithm")
    window.configure(background="black")

    for i in range(num_pages):
        current_page = reference_string[i]
        page_label = tk.Label(window, text=f"{current_page}", font="bold", bd=2, fg="white", bg="black", relief=tk.SOLID)
        page_label.grid(row=6, column=1+i, ipadx=20, ipady=10, sticky=tk.W)
        page_found = False

        if current_page in frames:
            page_found = True
            hits += 1
        else:
            if -1 in frames:
                frame_to_replace = frames.index(-1)
            else:
                future_indices = [reference_string[i+1:].index(frames[j]) if frames[j] in reference_string[i+1:] else num_pages for j in range(num_frames)]
                frame_to_replace = future_indices.index(max(future_indices))
            frames[frame_to_replace] = current_page
            page_faults += 1

        for j in range(num_frames):
            if frames[j] == -1:
                color = "#ff0000" if not page_found else "#00cc00"
                label = tk.Label(window, text="  ", font="bold", bd=2, bg=color, relief=tk.SOLID)
                label.grid(row=7+j, column=1+i, ipadx=20, ipady=10, sticky=tk.W)
            else:
                color = "#ff0000" if not page_found else "#00cc00"
                label = tk.Label(window, text="%d" % frames[j], font="bold", bd=2, bg=color, relief=tk.SOLID)
                label.grid(row=7+j, column=1+i, ipadx=20, ipady=10, sticky=tk.W)
    
    print("Optimal Algorithm:")
    print("\nPage Faults: ", page_faults)
    print("\nTotal Hits: ", hits)
    create_labels(window, num_pages, page_faults, hits)

def visualize_fifo():
    window = tk.Tk()
    reference_string = [int(x) for x in pages_entry.get().split()]
    num_frames = int(num_frames_entry.get())
    num_pages = len(reference_string)
    print("Reference string: ", reference_string, "\nFrames: ", num_frames)

    fifo_algorithm(num_pages, reference_string, num_frames, window)

def visualize_lru():
    window = tk.Tk()
    reference_string = [int(x) for x in pages_entry.get().split()]
    num_frames = int(num_frames_entry.get())
    num_pages = len(reference_string)
    print("Reference string: ", reference_string, "\nFrames: ", num_frames)

    lru_algorithm(num_pages, reference_string, num_frames, window)

def visualize_optimal():
    window = tk.Tk()
    reference_string = [int(x) for x in pages_entry.get().split()]
    num_frames = int(num_frames_entry.get())
    num_pages = len(reference_string)
    print("Reference string: ", reference_string, "\nFrames: ", num_frames)

    optimal_algorithm(num_pages, reference_string, num_frames, window)

def clear_inputs():
    pages_entry.delete(0, tk.END)
    num_frames_entry.delete(0, tk.END)

# Create input labels and entry widgets
pages_label = tk.Label(root, text="Reference String:")
pages_entry = tk.Entry(root)
num_frames_label = tk.Label(root, text="Number of Frames:")
num_frames_entry = tk.Entry(root)

# Create Buttons
visualize_fifo_button = tk.Button(root, text="Visualize FIFO", command=visualize_fifo)
visualize_lru_button = tk.Button(root, text="Visualize LRU", command=visualize_lru)
visualize_optimal_button = tk.Button(root, text="Visualize Optimal", command=visualize_optimal)
clear_button = tk.Button(root, text="Clear", command=clear_inputs)

# Layout the widgets
pages_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
pages_entry.grid(row=0, column=1, padx=10, pady=10)
num_frames_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
num_frames_entry.grid(row=1, column=1, padx=10, pady=10)
visualize_fifo_button.grid(row=2, column=0, padx=10, pady=10)
visualize_lru_button.grid(row=2, column=1, padx=10, pady=10)
visualize_optimal_button.grid(row=3, column=0, padx=10, pady=10)
clear_button.grid(row=3, column=1, padx=10, pady=10)

root.mainloop()
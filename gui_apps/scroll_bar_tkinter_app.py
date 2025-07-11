import tkinter as tk

# Create window and canvas
root = tk.Tk()
canvas_width = 320
canvas_height = 300
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg='white')
canvas.pack()

# Setup variables
radius = 10
line_y = 200

# Start and end positions to keep the circle fully visible
line_start = radius
line_end = canvas_width - radius

# Draw red line
canvas.create_line(line_start, line_y, line_end, line_y, fill='red', width=5)

# Create green circle at start of the line
x1 = line_start - radius
y1 = line_y - radius
x2 = line_start + radius
y2 = line_y + radius
circle = canvas.create_oval(x1, y1, x2, y2, width=3, fill='green')

# Add a counter text
counter = 0
text_id = canvas.create_text(
    canvas_width // 2, 100, text=f"Counter: {counter}", font=("Arial", 16), fill="black"
)

# Animation settings
total_duration_ms = 10000  # 10 seconds
interval_ms = 50           # Update every 50ms
steps = total_duration_ms // interval_ms
distance = line_end - line_start
move_step = distance / steps

step_count = 0

# Animation function
def update_motion():
    global step_count, counter

    if step_count < steps:
        canvas.move(circle, move_step, 0)
        step_count += 1

        # Update counter every 1 second (20 steps at 50ms intervals)
        if step_count % 20 == 0:
            counter += 1
            canvas.itemconfig(text_id, text=f"Counter: {counter}")

        root.after(interval_ms, update_motion) # Update after 50ms
    else:
        # Ensure circle ends exactly at the line end
        coords = canvas.coords(circle)
        current_center = (coords[0] + coords[2]) / 2
        correction = line_end - current_center
        canvas.move(circle, correction, 0)

# Start animation
update_motion()
root.mainloop()

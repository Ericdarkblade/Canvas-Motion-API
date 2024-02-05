import Canvas.events as canvas


classes = set()

canvas_events: [canvas.Canvas_Event] = canvas.parse_canvas_calendar()

for assignment in canvas_events:
    assignment: canvas.Canvas_Event  # My lsp doesn't know what class event belongs to for some reason.

    if assignment.class_code not in classes:
        classes.add(assignment.class_code)


print(classes)

undo_stack = []   # changes made so far
redo_stack = []   # changes that were undone

def show():
    if len(undo_stack) == 0:
        print("Document: (empty)")
    else:
        print("Document:", " ".join(undo_stack))

while True:
    print("\n1.Make change 2.Undo 3.Redo 4.Exit")
    ch = int(input("Enter choice: "))

    if ch == 1:
        text = input("Enter text: ")
        undo_stack.append(text)
        redo_stack = []          # new change clears redo history
        show()

    elif ch == 2:
        if len(undo_stack) == 0:
            print("Nothing to undo")
        else:
            redo_stack.append(undo_stack.pop())
            show()

    elif ch == 3:
        if len(redo_stack) == 0:
            print("Nothing to redo")
        else:
            undo_stack.append(redo_stack.pop())
            show()
    else:
        break






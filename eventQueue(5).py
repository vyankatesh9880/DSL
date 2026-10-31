queue = []

while True:
    print("\n1.Add 2.Process next 3.Display pending 4.Cancel 5.Exit")
    ch = int(input("Enter choice: "))
    if ch == 1:
        event = input("Enter event: ")
        queue.append(event)
        print("Event added")
    elif ch == 2:
        if len(queue) == 0:
            print("No events to process")
        else:
            print("Processed:", queue.pop(0))
    elif ch == 3:
        if len(queue) == 0:
            print("No pending events")
        else:
            print("Pending events:", queue)
    elif ch == 4:
        event = input("Enter event to cancel: ")
        if event in queue:
            queue.remove(event)
            print("Event cancelled")
        else:
            print("Event not found")
    else:
        break





    

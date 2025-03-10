

def manage_stage_changes(changes):
    #stack
    canceled_stack = []
    scheduled_stack = []

    #iterate over changes
    for change in changes:
        if change == "Cancel" and len(scheduled_stack) > 0:
            canceled_stack.append(scheduled_stack.pop())
        elif change == "Reschedule":
            scheduled_stack.append(canceled_stack.pop())
        else:
            scheduled_stack.append(change)
    return [letter[-1] for letter in scheduled_stack]


   


print(manage_stage_changes(["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"]))  
print(manage_stage_changes(["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"])) 
print(manage_stage_changes(["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"])) 
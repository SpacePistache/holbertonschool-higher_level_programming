#!/usr/bin/python3

def generate_invitations(template_content, attendees):
    i = 1
    for attendee in attendees:
        filename = "output_" + str(i) + ".txt"
        i += 1
        if attendee ["name"]:
            name = attendee ["name"] 
        else: name = "N/A"
        if attendee ["event_title"]:
            event_title = attendee ["event_title"]
        else: "N/A"
        if attendee ["event_date"]:
             event_date = attendee ["event_date"]
        else: "N/A"
        if attendee ["event_location"]:
            event_location = attendee ["event_location"]
        else: "N/A"
        new_content = template_content.replace("{name}", name).replace("{event_title}", event_title).replace("{event_date}", event_date).replace("{event_location}", event_location)
        with open(filename, "w") as file:
            file.write(new_content)
    
        
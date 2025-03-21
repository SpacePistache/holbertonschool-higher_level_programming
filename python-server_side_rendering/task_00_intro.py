#!/usr/bin/python3

def generate_invitations(template_content, attendees):

    if not isinstance(template_content, str):
        print("Error: Template is not a valid string.")
        return
    if not template_content.strip():
        print("Template is empty, no output files generated.")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees should be a list of dictionaries.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    i = 1
    for attendee in attendees:
        filename = "output_" + str(i) + ".txt"
        i += 1
        if attendee["name"]:
            name = attendee["name"]
        else: name = "N/A"
        if attendee["event_title"]:
            event_title = attendee ["event_title"]
        else: "N/A"
        if attendee["event_date"]:
             event_date = attendee ["event_date"]
        else: "N/A"
        if attendee["event_location"]:
            event_location = attendee["event_location"]
        else: "N/A"
        new_content = template_content.replace("{name}", name)\
            .replace("{event_title}", event_title).replace("{event_date}", event_date)\
            .replace("{event_location}", event_location)
        with open(filename, "w") as file:
            file.write(new_content)
            print(new_content)

import re

class EmailAgent:
    def process(self, content):
        sender_match = re.search(r'From: (.+)', content)
        urgency_match = re.search(r'Urgency: (high|medium|low)', content, re.IGNORECASE)

        sender = sender_match.group(1).strip() if sender_match else "unknown"
        urgency = urgency_match.group(1).strip().lower() if urgency_match else "medium"

        return {
            "sender": sender,
            "urgency": urgency,
            "thread_id": f"email_{hash(sender + urgency)}"
        }

from utils.file_utils import detect_format, read_file
from utils.openai_utils import detect_intent
from agents.email_agent import EmailAgent
from agents.json_agent import JSONAgent

class ClassifierAgent:
    def __init__(self, memory):
        self.memory = memory

    def process(self, file_path):
        fmt = detect_format(file_path)
        content = read_file(file_path)

        if fmt == "JSON":
            content_str = json.dumps(content)
        else:
            content_str = content[:1000]  # Truncate for prompt size

        intent = detect_intent(content_str)
        print(f"[Classifier] Detected format: {fmt}, intent: {intent}")

        if fmt == "Email":
            result = EmailAgent().process(content)
        elif fmt == "JSON":
            result = JSONAgent().process(content)
        else:
            result = {"message": "PDFs currently not handled beyond format detection."}

        self.memory.store(
            source=file_path,
            type_=fmt,
            intent=intent,
            extracted_values=result,
            thread_id=result.get("thread_id", "unknown")
        )

        return result

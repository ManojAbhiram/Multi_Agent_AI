class JSONAgent:
    def process(self, data):
        required_keys = ["id", "customer", "amount"]
        missing = [key for key in required_keys if key not in data]

        result = {
            "normalized_data": data,
            "missing_fields": missing,
            "thread_id": f"json_{data.get('id', 'unknown')}"
        }

        return result

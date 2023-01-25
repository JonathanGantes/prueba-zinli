
class Utils:

    @staticmethod
    def clear_string_for_excecutor(reason) -> str:
        # This Operation Deletes NewLines and Double Quotes from Exceptions
        result = " ".join(reason.split()).replace('"', "'").replace("\\", "/")
        return result

    @staticmethod
    def is_native(device:str) -> bool:
        return device in ("android", "ios")

    @staticmethod
    def clear_text_spaces(text: str) -> str:
        return " ".join(text.split())

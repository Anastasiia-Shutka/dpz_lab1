import json
from abc import ABC, abstractmethod

class OutputStrategy(ABC):
    @abstractmethod
    def log(self, message: str):
        pass

class ConsoleOutputStrategy(OutputStrategy):
    def log(self, message: str):
        print(f"[CONSOLE LOG]: {message}")

class KafkaOutputStrategy(OutputStrategy):
    def log(self, message: str):
        print(f"[KAFKA CLUSTER]: Sending message -> {message}")

class OutputFactory:
    @staticmethod
    def get_strategy() -> OutputStrategy:
        try:
            with open("config.json", "r") as f:
                config = json.load(f)
            
            strategy_type = config.get("output_type", "console").lower()
            
            if strategy_type == "kafka":
                return KafkaOutputStrategy()
            return ConsoleOutputStrategy()
        except Exception:
            return ConsoleOutputStrategy()
        
import csv
import json
from typing import Dict
from pathlib import Path
from time import strftime
from openai.types.chat.chat_completion import ChatCompletion

from openai_cost_logger.constants import DEFAULT_LOG_PATH

"""Every cost is per million tokens."""
COST_UNIT = 1_000_000

"""Header of the cost log file."""
FILE_HEADER = [
    "experiment_name",
    "model",
    "cost"
]

"""OpenAI cost logger."""
class OpenAICostLogger:
    def __init__(
        self,
        model: str,
        input_cost: float,
        output_cost: float,
        experiment_name: str,
        cost_upperbound: float = float('inf'),
        log_folder: str = DEFAULT_LOG_PATH,
        log_level: str = "detail"
    ):
        """Initialize the cost logger.

        Args:
            client (enum.ClientType): The client to use.
            model (str): The model to use.
            cost_upperbound (float): The upperbound of the cost after which an exception is raised.
            input_cost (float): The cost per million tokens for the input.
            output_cost (float): The cost per million tokens for the output.
            experiment_name (str): The name of the experiment.
            log_folder (str): The folder where to save the cost logs.
            client_args (Dict, optional): The parameters to pass to the client. Defaults to {}.
        """
        self.cost = 0
        self.n_responses = 0
        self.model = model
        self.input_cost = input_cost
        self.log_folder = log_folder
        self.output_cost = output_cost
        self.experiment_name = experiment_name
        self.cost_upperbound = cost_upperbound
        self.log_level = log_level
        self.creation_datetime = strftime("%Y-%m-%d_%H:%M:%S")
        self.filename = f"{experiment_name}_{self.creation_datetime}.json"
        self.filepath = Path(self.log_folder, self.filename)

        self.__check_existance_log_folder()
        self.__build_log_file()


    def update_cost(self, response: ChatCompletion) -> None:
        """Extract the number of input and output tokens from a chat completion response
        and update the cost. Saves experiment costs to file, overwriting it. 
           
        Args:
            response: ChatCompletion object from the model.
        """
        self.cost += self.__get_answer_cost(response)
        self.n_responses += 1
        self.__write_cost_to_json(response)
        self.__validate_cost()

        
    def get_current_cost(self) -> float:
        """Get the current cost of the cost tracker.

        Returns:
            float: The current cost.
        """
        return self.cost
    
    
    def __get_answer_cost(self, answer: Dict) -> float:
        """Calculate the cost of the answer based on the input and output tokens.

        Args:
            answer (dict): The response from the model.
        Returns:
            float: The cost of the answer.        
        """
        return (self.input_cost * answer.usage.prompt_tokens) / COST_UNIT + \
                    (self.output_cost * answer.usage.completion_tokens) / COST_UNIT
            
            
    def __validate_cost(self):
        """Check if the cost exceeds the upperbound and raise an exception if it does.

        Raises:
            Exception: If the cost exceeds the upperbound.
        """
        if self.cost > self.cost_upperbound:
            raise Exception(f"Cost exceeded upperbound: {self.cost} > {self.cost_upperbound}")


    def __write_cost_to_json(self, response: ChatCompletion) -> None:
        """Write the cost to a json file. 

        Args:
            response (ChatCompletion): The response from the model.
        """
        with open(self.filepath, 'r') as file:
            data = json.load(file)
            data["total_cost"] = self.cost
            data["total_responses"] = self.n_responses
            data["breakdown"].append(self.__build_log_breadown_entry(response))
        with open(self.filepath, 'w') as file:
            json.dump(data, file, indent=4)


    def __check_existance_log_folder(self) -> None:
        """Check if the log folder exists and create it if it does not."""
        self.filepath.parent.mkdir(parents=True, exist_ok=True)


    def __build_log_file(self) -> None:
        """Create the log file with the header."""
        log_file_template = {
            "experiment_name": self.experiment_name,
            "creation_datetime": strftime("%Y-%m-%d %H:%M:%S"),
            "model": self.model,
            "total_cost": self.cost,
            "total_responses": 0,
            "breakdown": []
        }
        with open(self.filepath, 'w') as file:
            json.dump(log_file_template, file, indent=4)

    
    def __build_log_breadown_entry(self, response: ChatCompletion) -> Dict:
        """Build a json log entry for the breakdown of the cost.

        Args:
            response (ChatCompletion): The response from the model.

        Returns:
            Dict: The json log entry.
        """
        return {
            "cost": self.__get_answer_cost(response),
            "input_tokens": response.usage.prompt_tokens,
            "output_tokens": response.usage.completion_tokens,
            "content": response.choices[0].message.content,
            "inferred_model": response.model,
            "datetime": strftime("%Y-%m-%d %H:%M:%S"),
        }
import csv
import os
from interfaces.repository_interface import IRepository


class DataLoader:
    @classmethod
    def load(self, model, repository: IRepository, filename):
        filepath = os.path.join(os.path.dirname(__file__), "data", filename)
        with open(filepath) as file:
            reader = csv.DictReader(file)
            for row in reader:
                registry = model.model_validate(row)
                repository.save(registry)

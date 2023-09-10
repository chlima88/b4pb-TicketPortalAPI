import csv
from interfaces.repository_interface import IRepository


class DataLoader:
    @classmethod
    def load(self, model, repository: IRepository, filename):
        with open(filename) as file:
            reader = csv.DictReader(file)
            for row in reader:
                # print(row)
                registry = model.model_validate(row)
                # print(registry)
                repository.save(registry)

import inspect
from dataclasses import dataclass

from typing import List

class Response:
    @classmethod
    def from_dict(cls, **kwargs):
        return cls(**{k: v for k, v in kwargs.items() if k in inspect.signature(cls).parameters})


@dataclass
class JobResponse(Response):
    model: str
    version: str
    job_id: str

@dataclass
class JobResultResponse(Response):
    status: str
    predictions: dict
    info: str

    def __str__(self):
        return f'Predictions: {self.predictions}'

@dataclass
class JobInfoResponse(Response):
    id: str
    job_id: str
    storage_path: str
    data: dict

@dataclass
class JobInfoResponses(Response):
    jobs: List[JobInfoResponse]
    def __getitem__(self, index):
        return self.jobs[index]

    def __len__(self):
        return len(self.jobs)

    def __str__(self):
        return f'Jobs: {len(self.jobs)}'

@dataclass
class ModelInfoResponse(Response):
    id: str
    name: str
    version: str
    status: str
    deployment_type: str
    create_date: str
    signature: dict
    input_example: dict
    metrics: dict
    def __str__(self):
        return f'Version {self.version} of {self.name} deployed in {self.deployment_type}'

@dataclass
class ModelResponse(Response):
    id: str
    name: str
    version: str
    deployment_type: str
    create_date: str

    def __str__(self):
        return f'Version {self.version} of {self.name} deployed in {self.deployment_type}'

@dataclass
class ModelResponses(Response):
    responses: List[ModelResponse]
    def __getitem__(self, index):
        return self.responses[index]

    def __len__(self):
        return len(self.responses)

    def __str__(self):
        return f'Models: {len(self.responses)}'

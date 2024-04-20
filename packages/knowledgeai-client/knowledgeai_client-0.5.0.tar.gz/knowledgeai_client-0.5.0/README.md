
# Avvia Intelligence - KnowledgeAI Python Client

Version: 0.5.0, (c) 2024 Arvato Systems

This library is designed to provide easy access to the KnowledgeAI backend service. It enables users to manage projects, upload documents, and perform various tasks programmatically. The client offers an intuitive interface for seamless integration into Python applications.

## Installation
```bash
pip install knowledgeai-client
```
```bash
poetry add knowledgeai-client
```

## Usage
```python
from knowledgeai import KnowledgeAIClient

# Initialize the KnowledgeAIClient
client = KnowledgeAIClient(url="https://your-knowledgeai-service.com", api_key="your_api_key")

# Uploads all files in a directory to the specified project
client.upload_directory(project_id="project_id", directory="/path/to/directory", roles="admin,user")

# Uploads multiple documents to the specified project
client.index_documents(project_id="project_id", files=["/path/to/file1.txt", "/path/to/file2.txt"], roles="user,admin")

# Indexes the specified URL to the specified project
client.index_urls(project_id="project_id", index_urls=["https://www.example.com"], roles="user")

# Lists all projects
projects = client.list_projects()
for project in projects:
    print(project.name)

# Gets the project with the specified ID
project = client.get_project(project_id=1)
print(project.name)

# Creates a new project with the specified name
project = client.create_project(project_name="New Project", prompt="x", language=IsoLanguage.ENGLISH, llm=LLM.OPENAI)
print(project.name)

# Updates the specified project
project = client.get_project(project_id=1)
project.name = "New Project Name"
response = client.update_project(project)

# Updates the configuration of the specified project
project = client.update_project_configuration(project_id=1, key=ProjectConfigKey.WELCOME_MESSAGE, value="value")

# Asks a question to the specified project
response = client.ask(project_id=1, question="What is the capital of Germany?")
print(response.answer)

# Retrieves documents for the specified project
references = client.retrieve(project_id=1, query="What is the capital of Germany?", retrieval_type=Retriever.default)
for reference in references:
    print(reference.content)
```

## Documentation

The `KnowledgeAIClient` facilitates seamless communication with the Avvia Intelligence KnowledgeAI service, allowing users to manage projects, upload documents, and perform various other tasks programmatically. It provides an intuitive interface to interact with the KnowledgeAI platform, enabling easy integration into Python applications.

### Class: KnowledgeAIClient

#### Constructor: `__init__(url: str, api_key: str, timeout: int = 30) -> None`

Initializes a new instance of the `KnowledgeAIClient` class.

- `url` (str): The URL of the KnowledgeAI service.
- `api_key` (str): The API key for authentication.
- `timeout` (int, optional): The timeout for API requests in seconds. Defaults to 30.

#### Method: `upload_directory(project_id: int, directory: str, roles: str = "user") -> None`

Convenience method to upload all files in a directory to the specified project.

- `project_id` (int): The ID of the project to upload the documents to.
- `directory` (str): The path to the directory containing the files to upload.
- `roles` (str, optional): The roles to assign to the uploaded documents. Comma-separated list. Defaults to "user".


#### Method: `index_documents(project_id: int, files: List[str], roles: str = "user") -> None`

Uploads multiple documents to the specified project.

- `project_id` (int): The ID of the project to upload the documents to.
- `files` (List[str]): A list of file paths to upload.
- `roles` (str, optional): The roles to assign to the uploaded documents. Comma-separated list. Defaults to "user".


#### Method: `index_urls(project_id: int, index_urls: List[str], roles: Optional[str]) -> None`

Indexes the specified URL to the specified project.

- `project_id` (int): The ID of the project to index the URL to.
- `index_urls` (List[str]): The URLs to index.
- `roles` (str, optional): The roles to assign to the indexed document. Comma-separated list. Defaults to "user".


#### Method: `list_projects() -> List[Project]`

Lists all projects.

Returns:
- `List[Project]`: A list of projects.


#### Method: `get_project(project_id: int, with_documents: bool = False) -> Project`

Gets the project with the specified ID.

- `project_id` (int): The ID of the project to get.
- `with_documents` (bool, optional): Whether to include the documents in the response.

Returns:
- `Project`: The project with the specified ID.


#### Method: `create_project(project_name: str, prompt: str, language: IsoLanguage = IsoLanguage.ENGLISH, llm: LLM = LLM.OPENAI) -> Project`

Creates a new project with the specified name.

- `project_name` (str): The name of the project to create.
- `language` (IsoLanguage, optional): The language of the project. Defaults to IsoLanguage.ENGLISH.
- `llm` (LLM, optional): The language model to use. Defaults to LLM.OPENAI.
- `prompt` (str, optional): The prompt to use for the project.

Returns:
- `Project`: The created project.


#### Method: `update_project(project: Project) -> Response`

Updates the specified project.

- `project` (Project): The project to update.

Returns:
- `Response`: The updated project.


#### Method: `update_project_configuration(project_id: int, key: ProjectConfigKey, value: str) -> Project`

Updates the configuration of the specified project.

- `project_id` (int): The ID of the project to update the configuration for.
- `key` (str): The key of the configuration to update.
- `value` (str): The value to update the configuration to.

Returns:
- `Project`: The updated project.


#### Method: `ask(project_id: int, question: str) -> AskResponse`

Asks a question to the specified project.

- `project_id` (int): The ID of the project to ask the question to.
- `question` (str): The question to ask.

Returns:
- `AskResponse`: The response to the question.


#### Method: `retrieve(project_id: int, query: str, retrieval_type: Retriever = Retriever.default) -> List[RetrievedDocument]`

Retrieves documents for the specified project.

- `project_id` (int): The ID of the project to retrieve documents from.
- `query` (str): The query to retrieve documents for.
- `retrieval_type` (Retriever, optional): The type of retrieval to use.

Returns:
- `List[RetrievedDocument]`: The retrieved documents.


### Schema Description

Before diving into the usage of `KnowledgeAIClient`, it's important to understand the schema used in the API. Here are the key classes and enums used:

#### ProjectConfigKey (Enum)

Defines keys for project configuration settings such as `BOTSERVICE_APP_ID`, `BOTSERVICE_APP_PASSWORD`, `BOTSERVICE_SECRET`, and `WELCOME_MESSAGE`.

#### Plan (Enum)

Represents different plans available such as `FREE`, `BASIC`, `PREMIUM`, and `ENTERPRISE`.

#### IsoLanguage (Enum)

Defines ISO language codes for languages such as `GERMAN` and `ENGLISH`.

#### LLM (Enum)

Represents different language models like `OPENAI`, `GOOGLE`, and `ANTHROPIC`.

#### AskResponse (Model)

Represents a response to a question with attributes `question`, `answer`, `source_paragraphs`, and `source_documents`.

#### Retriever (Enum)

Defines different types of retrievers such as `default`, `multiquery`, and `compression`.

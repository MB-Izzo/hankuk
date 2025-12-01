from pydantic import BaseModel, Field

class Example(BaseModel):
    korean: str = Field("The french translation of the example")
    french: str = Field("The korean translation of the example")

class Translation(BaseModel):
    translation: str = Field(description="Translation of word")
    explaination: str = Field(description="Explaination/definition of word")
    passive_form: str = Field(description="Passive form of the word")
    active_form: str = Field(description="Active form of the word")
    grammar_use: str = Field(description="How to use the word in a sentence")
    example: Example = Field(description="Some example sentences")

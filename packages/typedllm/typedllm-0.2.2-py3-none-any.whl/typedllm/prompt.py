from typing import ClassVar, Optional, Type
from typedtemplate import TypedTemplate, BaseTemplateEngine


class TypedPrompt(TypedTemplate):
    template_engine: ClassVar[BaseTemplateEngine]
    template_file: ClassVar[Optional[str]] = None
    template_string: ClassVar[Optional[str]] = None

    def __init__(
            self,
            **kwargs
    ):
        super().__init__(**kwargs)
        self._template


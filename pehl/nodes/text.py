from typing import Iterator
from .literal import Literal


class Text(Literal):
    """Text (Literal) represents a Text ([DOM]).

    Example:

    ```html
    <span>Foxtrot</span>
    ```

    Yields:

    ```javascript
    {
        type: 'element',
        tagName: 'span',
        properties: {},
        children: [{type: 'text', value: 'Foxtrot'}]
    }
    ```
    """
    
    def tree(self, depth: int = 0, prefix: str = "└") -> Iterator[str]:
        yield f"{' '*depth}{prefix} {self.type.upper()}"

    def pehl(self, indent: int = 0) -> str:
        """Build indented html string of html text.

        Returns:
            str: Built html of text
        """
        lines = self.value.split("\n")
        if len(lines) > 1:
            offset = len(lines[0]) - len(lines[0].lstrip())
            lines = [line[offset:] for line in lines]
            joiner = "\n" + f"{' '*indent}"
            out = joiner.join(lines)
        else:
            out = lines[0].strip()
            
        return ' '*indent + out

    def __str__(self) -> str:
        return self.value
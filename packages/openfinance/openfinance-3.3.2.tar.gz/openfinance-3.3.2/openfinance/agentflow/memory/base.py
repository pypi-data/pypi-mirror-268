from typing import (
    Any,
    Callable,
    Dict,
    List,
    Union
)

class Memory:
    history: List[Any] = []
    def __call__(
        self
    ) -> str:
        result = ""
        for r in self.history:
            result += r[0] + ": " + r[1] + "\n"
        return result

    def add(
        self,
        role: str,
        message: Any
    ):
        """
            Match history to different format history
        """
        if isinstance(message, str):
            self.history.append((role, message))
        elif isinstance(message, list):
            msg = ""
            for l in message:
                print(l)
                if isinstance(l, str):
                    msg += l + "\n"
                elif isinstance(l, dict):
                    msg += l["result"] + "\n"
                elif isinstance(l, list): # multi input parameters
                    for il in l:
                        if isinstance(il, str):
                            msg += il + "\n"
                        else:
                            msg += il["result"] + "\n"
            self.history.append((role, msg))
        else:
            self.history.append((role, message["result"]))

    def clear(
        self
    ):
        self.history.clear()

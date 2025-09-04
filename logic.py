def calculate(expression: str) -> str:
    try:
        expression = expression.strip()
        result = eval(expression, {"__builtins__": {}}, {})
        return str(result)
    except Exception:
        return "Ошибка: введите корректное выражение"
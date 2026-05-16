BLANK = "_"

transitions = {
    ("q0", "X"): ("q0", "X", "R"),
    ("q0", "1"): ("q_go_to_star", "X", "R"),
    ("q0", "*"): ("q_erase_left", BLANK, "L"),

    ("q_go_to_star", "X"): ("q_go_to_star", "X", "R"),
    ("q_go_to_star", "1"): ("q_go_to_star", "1", "R"),
    ("q_go_to_star", "*"): ("q_copy_y", "*", "R"),

    ("q_copy_y", "Y"): ("q_copy_y", "Y", "R"),
    ("q_copy_y", "1"): ("q_to_result", "Y", "R"),
    ("q_copy_y", "="): ("q_restore_y", "=", "L"),

    ("q_to_result", "Y"): ("q_to_result", "Y", "R"),
    ("q_to_result", "1"): ("q_to_result", "1", "R"),
    ("q_to_result", "="): ("q_append", "=", "R"),

    ("q_append", "1"): ("q_append", "1", "R"),
    ("q_append", BLANK): ("q_back_from_result", "1", "L"),

    ("q_back_from_result", "1"): ("q_back_from_result", "1", "L"),
    ("q_back_from_result", "="): ("q_back_to_star", "=", "L"),

    ("q_back_to_star", "Y"): ("q_back_to_star", "Y", "L"),
    ("q_back_to_star", "1"): ("q_back_to_star", "1", "L"),
    ("q_back_to_star", "*"): ("q_copy_y", "*", "R"),

    ("q_restore_y", "Y"): ("q_restore_y", "1", "L"),
    ("q_restore_y", "1"): ("q_restore_y", "1", "L"),
    ("q_restore_y", "*"): ("q_to_left_start", "*", "L"),

    ("q_to_left_start", "X"): ("q_to_left_start", "X", "L"),
    ("q_to_left_start", "1"): ("q_to_left_start", "1", "L"),
    ("q_to_left_start", BLANK): ("q0", BLANK, "R"),

    ("q_erase_left", "X"): ("q_erase_left", BLANK, "L"),
    ("q_erase_left", "1"): ("q_erase_left", BLANK, "L"),
    ("q_erase_left", BLANK): ("q_seek_right_operand", BLANK, "R"),

    ("q_seek_right_operand", BLANK): ("q_seek_right_operand", BLANK, "R"),
    ("q_seek_right_operand", "1"): ("q_erase_right_operand", BLANK, "R"),
    ("q_seek_right_operand", "Y"): ("q_erase_right_operand", BLANK, "R"),
    ("q_seek_right_operand", "="): ("q_accept", BLANK, "R"),

    ("q_erase_right_operand", "1"): ("q_erase_right_operand", BLANK, "R"),
    ("q_erase_right_operand", "Y"): ("q_erase_right_operand", BLANK, "R"),
    ("q_erase_right_operand", "="): ("q_accept", BLANK, "R"),
}


class TuringMachine:
    def __init__(self, tape_string, transitions, start_state="q0", accept_state="q_accept"):
        self.tape = {i: symbol for i, symbol in enumerate(tape_string)}
        self.head = 0
        self.state = start_state
        self.transitions = transitions
        self.accept_state = accept_state
        self.steps = 0

    def get_symbol(self):
        return self.tape.get(self.head, BLANK)

    def set_symbol(self, symbol):
        self.tape[self.head] = symbol

    def move_head(self, direction):
        if direction == "R":
            self.head += 1
        elif direction == "L":
            self.head -= 1

    def get_tape_string(self):
        if not self.tape:
            return ""

        min_pos = min(self.tape.keys())
        max_pos = max(self.tape.keys())

        result = ""
        for i in range(min_pos, max_pos + 1):
            result += self.tape.get(i, BLANK)

        return result.strip(BLANK)

    def get_configuration(self):
        min_pos = min(min(self.tape.keys()), self.head)
        max_pos = max(max(self.tape.keys()), self.head)

        tape_view = ""
        pointer = ""

        for i in range(min_pos, max_pos + 1):
            tape_view += self.tape.get(i, BLANK)
            pointer += "^" if i == self.head else " "

        return f"{tape_view}\n{pointer}  стан: {self.state}"

    def run(self, max_steps=100000, show_steps=False, trace_limit=40):
        if show_steps:
            print("Початкова конфігурація:")
            print(self.get_configuration())
            print()

        while self.state != self.accept_state:
            current_symbol = self.get_symbol()
            key = (self.state, current_symbol)

            if key not in self.transitions:
                raise Exception(f"Немає переходу для стану {self.state} і символу {current_symbol}")

            new_state, new_symbol, direction = self.transitions[key]

            self.set_symbol(new_symbol)
            self.move_head(direction)
            self.state = new_state
            self.steps += 1

            if show_steps and self.steps <= trace_limit:
                print(f"Крок {self.steps}:")
                print(self.get_configuration())
                print()

            if self.steps > max_steps:
                raise Exception("Перевищено максимальну кількість кроків")

        return self.get_tape_string()


def unary_number(n):
    return "1" * n


def multiply_unary(x, y, show_steps=False):
    if x < 0 or y < 0:
        raise ValueError("Числа мають бути невід'ємними")

    tape = unary_number(x) + "*" + unary_number(y) + "="

    print("Вхідні дані:")
    print(f"x = {x}, y = {y}")
    print(f"Унарний запис: {unary_number(x)} * {unary_number(y)}")
    print(f"Початкова стрічка: {tape}")
    print()

    machine = TuringMachine(tape, transitions)
    result = machine.run(show_steps=show_steps)

    print("Результат:")
    print(f"Кінцева стрічка: {result if result else 'порожня стрічка'}")
    print(f"Добуток в унарній системі: {result if result else '0'}")
    print(f"Добуток у десятковій системі: {len(result)}")
    print(f"Кількість кроків: {machine.steps}")


x = int(input("Введіть x: "))
y = int(input("Введіть y: "))

multiply_unary(x, y, show_steps=True)
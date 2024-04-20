#!/usr/bin/env python3
from sys import stdin
from argparse import ArgumentParser
from collections import deque

def literal(literal):
    def enqueue(program, cursor, tape):
        tape.appendleft(literal)
        return cursor + 1
    return enqueue

def left(program, cursor, tape):
    if len(tape) > 0:
        tape.append(tape.popleft())
    return cursor + 1

def right(program, cursor, tape):
    if len(tape) > 0:
        tape.appendleft(tape.pop())
    return cursor + 1

def begin(program, cursor, tape):
    if len(tape) == 0 or tape.pop() == 0:
        depth = 0
        while cursor < len(program):
            operation = program[cursor]
            if operation == '[':
                depth += 1
            elif operation == ']':
                depth -= 1
            if depth == 0:
                break
            cursor += 1
    return cursor + 1

def end(program, cursor, tape):
    depth = 0
    while cursor < len(program):
        operation = program[cursor]
        if operation == '[':
            depth -= 1
        elif operation == ']':
            depth += 1
        if depth == 0:
            break
        cursor -= 1
    return cursor

def step(operations, program, cursor, tape):
    operation = program[cursor]
    if operation in operations:
        return operations[operation](program, cursor, tape)
    return cursor + 1

def run(operations, program, limit):
    steps = 0
    cursor = 0
    tape = deque([])
    while cursor < len(program) and steps < limit:
        cursor = step(operations, program, cursor, tape)
        steps += 1
    if steps == limit:
        print("Execution limit reached.")
    return ''.join([str(bit) for bit in reversed(tape)])

def main():
    operations = {
        '0': literal(0),
        '1': literal(1),
        '<': left,
        '>': right,
        '[': begin,
        ']': end
    }
    parser = ArgumentParser(
        prog="fvm",
        description="An interpreter for Feather's bitcode."
    )
    parser.add_argument("-l", "--limit",
        help="The number of iterations/cycles to run the interpreter. Useful for preventing infinite loops.",
        default=pow(2, 32),
        type=int,
    )
    arguments = parser.parse_args()
    print(run(operations, stdin.read(), arguments.limit))

if __name__ == "__main__":
    main()

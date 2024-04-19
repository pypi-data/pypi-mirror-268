import argparse
import random


from .riddle import riddle_factory
from .data import data

get_riddle, get_riddles = riddle_factory(data)

def create_argparser():
    parser = argparse.ArgumentParser(description="Fetch and display riddles.")
    parser.add_argument("-c", "--count", type=int, default=1, help="Number of riddles to retrieve, defaults to 1 if not provided.")
    return parser

def main():
    parser = create_argparser()
    args = parser.parse_args()

    try:
        # Check for positive count
        if args.count < 1:
            raise ValueError("Count must be at least 1.")

        if args.count == 1:
            riddle = get_riddle()
            print(f"Riddle: {riddle['question']}")
            print(f"Answer: {riddle['answer']}")
        else:
            riddles = get_riddles(args.count)
            for idx, r in enumerate(riddles, start=1):
                print(f"Riddle {idx}: {r['question']}")
                print(f"Answer: {r['answer']}")
                if idx < len(riddles):
                    print()

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

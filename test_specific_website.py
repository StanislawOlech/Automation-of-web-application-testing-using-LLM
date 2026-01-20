import json
import argparse
from utils import parse_elements, load_specification
from test_data_generator.generate_data import generate_test_data
from website import Website


def main(json_path):
    """Main function to run the test for specific website.

    Parameters
    ----------
    json_path : str
        Path to the JSON website file.

    Description
    -----------
    This function parses website from json, generates specific test cases for it
    and then evaluates website behavior."""
    json_str = ""

    # Parse
    try:
        json_str = load_specification(json_path)
    except FileNotFoundError:
        raise Exception(f"Error: File '{json_path}' not found.")

    data = json.loads(json_str)
    spec = parse_elements(data)


    # Generate test data and website
    test_data = generate_test_data(spec,
                                   num_tests=10,
                                   num_moves=5)

    website   = Website(spec, badness=0.0)


    # Run tests and print results
    for i, test in enumerate(test_data, start=1):
        results = website.use(test)

        print(f"\n=== Test {i} ===")
        for fid, val in test:
            value = val if val is not None else "Pressed"
            print(f"{fid} | Input: {value : <32}")
        print(f"Output: {results}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-j", "--json_file", type=str, help="Path to the JSON specification file")
    args = parser.parse_args()
    main(args.json_file)
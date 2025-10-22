from specification_generator import generate_specification
from test_data_generator.generate_data import generate_test_data
from website_generator import Website
from tester import test_website
from utils import progress_bar

def main():
    """Main function to run the website testing simulation.

    Description
    -----------
    This function orchestrates the generation of website specifications, test data,
    and the evaluation of website behavior. It creates both a correctly functioning
    website and a faulty version, then tests them against the same set of inputs to
    mesure the test vectors coverage."""

    num_tests = 1 # TODO chose a suitable number
    score = 0
    badness_level = 0.5
    for test in range(num_tests):
        spec        = generate_specification()
        test_data   = generate_test_data(spec)
        website     = Website(spec)
        bad_website = Website(spec, badness_level)
        score      += test_website(website, bad_website, test_data)

        progress_bar(test+1, num_tests)

    print("All tests completed.")
    print(f"Average score: {score/num_tests:.4f}")

if __name__ == "__main__":
    main()